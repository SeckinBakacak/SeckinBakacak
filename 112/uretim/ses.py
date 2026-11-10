"""Çok sesli seslendirme (ElevenLabs, önbellekli), telefon/telsiz efektleri,
ortam sesleri, efektler ve zaman çizelgesi.  Kullanım: python3 ses.py bolum01.json cikti/"""
import base64, hashlib, json, os, re, subprocess, sys
import numpy as np

SR = 44100
spec_path, out = sys.argv[1], sys.argv[2]
spec = json.load(open(spec_path))
base = os.path.dirname(os.path.abspath(spec_path))
cache = os.path.join(base, "cache"); os.makedirs(cache, exist_ok=True); os.makedirs(out, exist_ok=True)
key = os.environ.get("ELEVENLABS_API_KEY", "proxy-injected")
rng = np.random.default_rng(11)

def tts(text, voice):
    cfg = {**spec["model"], "voice_id": voice}
    h = hashlib.sha1(json.dumps([text, cfg], ensure_ascii=False).encode()).hexdigest()[:12]
    mp3, js = os.path.join(cache, h + ".mp3"), os.path.join(cache, h + ".json")
    if not os.path.exists(mp3):
        body = json.dumps({"text": text, **spec["model"]})
        r = subprocess.run(["curl", "-sS", "--fail-with-body",
            f"https://api.elevenlabs.io/v1/text-to-speech/{voice}/with-timestamps",
            "-H", f"xi-api-key: {key}", "-H", "Content-Type: application/json", "-d", body], capture_output=True)
        if r.returncode: sys.exit(r.stdout.decode() + r.stderr.decode())
        d = json.loads(r.stdout)
        open(mp3, "wb").write(base64.b64decode(d["audio_base64"])); json.dump(d["alignment"], open(js, "w"))
        print("  TTS:", text[:60])
    return mp3, json.load(open(js))

def decode(path, af=None):
    cmd = ["ffmpeg", "-v", "error", "-i", path]
    if af: cmd += ["-af", af]
    cmd += ["-f", "f32le", "-ac", "1", "-ar", str(SR), "-"]
    return np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, dtype=np.float32).copy()

FX = {
    "phone": "highpass=f=320,lowpass=f=3300,acompressor=threshold=0.1:ratio=6:attack=5:release=60,volume=1.6",
    "radio": "highpass=f=450,lowpass=f=2700,acompressor=threshold=0.08:ratio=10:attack=2:release=40,volume=2.2",
}

def words_from(al, t0):
    ws, cur, in_tag = [], None, False
    for c, s, e in zip(al["characters"], al["character_start_times_seconds"], al["character_end_times_seconds"]):
        if c == "[": in_tag = True
        if in_tag:
            if c == "]": in_tag = False
            continue
        if c.isspace():
            if cur: ws.append(cur); cur = None
            continue
        if cur is None: cur = {"w": "", "s": s + t0, "e": e + t0}
        cur["w"] += c; cur["e"] = e + t0
    if cur: ws.append(cur)
    return ws

# ---------- sentez efektleri ----------
def env(d, k): x = np.arange(int(d * SR)) / SR; return x, np.exp(-x * k)
def bp_noise(d, lo, hi):
    n = rng.standard_normal(int(d * SR)); f = np.fft.rfft(n); fr = np.fft.rfftfreq(len(n), 1 / SR)
    f[(fr < lo) | (fr > hi)] = 0; y = np.fft.irfft(f, len(n)); return y / (np.abs(y).max() + 1e-9)
def ring():
    x = np.arange(int(1.0 * SR)) / SR
    tone = (np.sin(2*np.pi*1400*x) * 0.6 + np.sin(2*np.pi*1750*x) * 0.4) * (np.sin(2*np.pi*18*x) > 0)
    gate = ((x < .38) | ((x > .5) & (x < .88))).astype(float)
    return tone * gate * np.minimum(1, x / .01)
def squelch(): x, e = env(.18, 18); return bp_noise(.18, 800, 4000) * e
def hangup():
    x = np.arange(int(1.6 * SR)) / SR
    return np.sin(2*np.pi*425*x) * ((x % .4) < .2) * .6
def radio_music(d):
    x = np.arange(int(d * SR)) / SR; y = np.zeros_like(x)
    notes = [392, 440, 494, 440, 392, 330, 349, 392]
    for i, f in enumerate(notes * 4):
        t0 = i * .45; m = (x >= t0) & (x < t0 + .42); xx = x[m] - t0
        y[m] += np.sin(2*np.pi*f*xx) * np.exp(-xx * 3) + .3*np.sin(2*np.pi*2*f*xx) * np.exp(-xx * 5)
    y = y * (0.6 + 0.4*np.sin(2*np.pi*.7*x)) + .25 * bp_noise(d, 1000, 6000) * (rng.random(len(x)) > .97)
    return y * np.minimum(1, (d - x) / .05)
def boom(): x, e = env(3.0, 1.3); return np.sin(2*np.pi*(52 - 18*x)*x) * e + .25*bp_noise(3.0, 20, 300)*np.exp(-x*4)
def heart():
    x = np.arange(int(4 * SR)) / SR; y = np.zeros_like(x)
    for b in np.arange(0, 4, .85):
        for o, a in ((0, 1), (.16, .7)):
            m = (x >= b + o) & (x < b + o + .15); xx = x[m] - b - o
            y[m] += a * np.sin(2*np.pi*55*xx) * np.exp(-xx * 30)
    return y
def glitch(): return bp_noise(.35, 300, 9000) * .8

# ---------- yerleşim ----------
scenes, t, voice_clips, line_clips = [], 0.0, [], []
for sc in spec["sahneler"]:
    lead, gap = sc.get("lead", 0.3), 0.35
    cur = t + lead; words, segs = [], []
    for who, text in sc["lines"]:
        v = spec["sesler"][who]
        raw = [w for w in text.split() if not w.startswith("[")]
        clean = text.replace("*", "")
        mp3, al = tts(clean, v["voice_id"])
        a = decode(mp3, FX.get(v.get("fx")))
        if v.get("fx") == "phone": a = a + 0.012 * bp_noise(len(a) / SR, 500, 3000)
        ws = words_from(al, cur)
        for i, w in enumerate(ws): w["red"] = i < len(raw) and "*" in raw[i]
        words += ws
        dur = len(a) / SR
        if v.get("fx") == "radio":
            voice_clips.append((cur - .2, squelch() * .5)); voice_clips.append((cur + dur + .02, squelch() * .5))
        voice_clips.append((cur, a))
        if who != "anlatici": line_clips.append((cur, a))
        segs.append({"who": who, "s": cur, "e": cur + dur, "text": re.sub(r"\[[^\]]*\]\s*", "", clean),
                     "label": v.get("label"), "color": v.get("color")})
        cur += dur + gap
    end = cur - gap + sc.get("tail", 0.35) + sc.get("extra", 0)
    scenes.append({**sc, "start": t, "end": end, "words": words, "segs": segs, "narrEnd": cur - gap})
    t = end
total = t + 0.5
n = int(total * SR); tt = np.arange(n) / SR
voice = np.zeros(n, np.float32); line = np.zeros(n, np.float32); bed = np.zeros(n, np.float32)
def add(buf, sig, at, g=1.0):
    i = int(at * SR)
    if i < 0: sig = sig[-i:]; i = 0
    j = min(n, i + len(sig))
    if i < n: buf[i:j] += g * sig[: j - i]
for at, a in voice_clips: add(voice, a, at)
for at, a in line_clips: add(line, a, at)

# ortam sesleri (sahne geçişlerinde yumuşak)
amb = {
    "wind": bp_noise(total, 150, 900) * (0.55 + 0.45*np.sin(2*np.pi*.13*tt) * np.sin(2*np.pi*.05*tt + 1)) * .10,
    "office": (np.sin(2*np.pi*100*tt) * .012 + bp_noise(total, 2000, 7000) * .006 + bp_noise(total, 80, 400) * .02),
    "engine": (np.sin(2*np.pi*38*tt) * .6 + np.sin(2*np.pi*76*tt) * .3) * .05 + bp_noise(total, 60, 300) * .05,
}
x, e = env(.03, 200); tick = bp_noise(.03, 2000, 6000) * e
for k in np.arange(0, total, 1.0): add(amb["office"], tick * .05, k)
for s in scenes:
    a = s.get("amb", "none")
    if a in amb:
        i, j = int(s["start"] * SR), int(s["end"] * SR); m = np.zeros(n); m[i:j] = 1
        k = int(.25 * SR); m = np.convolve(m, np.ones(k) / k, "same")
        bed += (amb[a] * m).astype(np.float32)
drone = (np.sin(2*np.pi*49*tt) + .5*np.sin(2*np.pi*73.6*tt)) * (.6 + .4*np.sin(2*np.pi*.06*tt)) * .02
bed += drone.astype(np.float32)

sfx = np.zeros(n, np.float32)
for s in scenes:
    add(sfx, glitch() * .05, s["start"] - .05)
    for name, frac in s.get("sfx", []):
        at = s["start"] + frac if name in ("ring",) else s["start"] + frac * (s["end"] - s["start"])
        if name == "ring": add(sfx, ring(), at, .16)
        elif name == "radio":
            cut = next((w["s"] for w in s["words"] if w["w"].lower().startswith("kesil")), s["end"] - 1.2)
            rm = radio_music(cut - at + .1) * .05; add(sfx, rm, at); add(line, rm * 3, at)
            add(sfx, glitch() * .3, cut); add(sfx, hangup(), cut + .25, .08)
        elif name == "boom": add(sfx, boom(), at, .5)
        elif name == "heart": add(sfx, heart(), at, .7)
    if s["v"] == "choice":
        x, e = env(.08, 60); clk = (np.sin(2*np.pi*1900*x) + .5*rng.standard_normal(len(x))) * e
        for k in range(5): add(sfx, clk, s["narrEnd"] + .4 + k, .3)
    for sg in s["segs"]:
        if sg["who"] == "rizaphone": add(sfx, glitch(), sg["s"] - .25, .25)

mix = voice + bed + sfx
fade = np.minimum(1, tt / .5) * np.minimum(1, (total - tt) / .8)
mix = mix * fade; mix /= max(1.0, np.abs(mix).max() / .95)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "s16le", "-ar", str(SR), "-ac", "1", "-i", "-", os.path.join(out, "ses.wav")],
               input=(mix * 32767).astype("<i2").tobytes(), check=True)

# dalga formu için zarf (60 Hz): sadece hat sesleri
hop = SR // 60; m = len(line) // hop
envl = np.sqrt((line[: m * hop].reshape(m, hop) ** 2).mean(1)); envl = np.clip(envl / (np.percentile(envl[envl > 0], 98) + 1e-9), 0, 1.2)
envv = np.sqrt((voice[: m * hop].reshape(m, hop) ** 2).mean(1)); envv = np.clip(envv / (np.percentile(envv[envv > 0], 98) + 1e-9), 0, 1.2)
json.dump({"title": spec["baslik"], "choice": spec.get("secim"), "total": total, "scenes": scenes,
           "envLine": [round(float(v), 3) for v in envl], "envVoice": [round(float(v), 3) for v in envv]},
          open(os.path.join(out, "timeline.json"), "w"), ensure_ascii=False)
print(f"Süre: {total:.1f} sn, sahne: {len(scenes)}")
