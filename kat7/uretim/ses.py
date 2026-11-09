"""Seslendirme (ElevenLabs, önbellekli) + zaman çizelgesi + ses miksajı.
Kullanım: python3 ses.py bolum01.json cikti_klasoru
"""
import base64, hashlib, json, os, subprocess, sys
import numpy as np

SR = 44100
PAD = 0.35          # sahne sonu boşluk
LEAD = 0.15         # sahne başı boşluk

spec_path, out = sys.argv[1], sys.argv[2]
spec = json.load(open(spec_path))
base = os.path.dirname(os.path.abspath(spec_path))
ep = os.path.splitext(os.path.basename(spec_path))[0]
cache = os.path.join(base, "cache", ep)
os.makedirs(cache, exist_ok=True); os.makedirs(out, exist_ok=True)
key = os.environ.get("ELEVENLABS_API_KEY", "proxy-injected")

def tts(text):
    cfg = spec["ses"]
    h = hashlib.sha1(json.dumps([text, cfg], ensure_ascii=False).encode()).hexdigest()[:12]
    mp3, js = os.path.join(cache, h + ".mp3"), os.path.join(cache, h + ".json")
    if not os.path.exists(mp3):
        body = json.dumps({"text": text, **{k: v for k, v in cfg.items() if k != "voice_id"}})
        r = subprocess.run(["curl", "-sS", "--fail-with-body",
            f"https://api.elevenlabs.io/v1/text-to-speech/{cfg['voice_id']}/with-timestamps",
            "-H", f"xi-api-key: {key}", "-H", "Content-Type: application/json", "-d", body],
            capture_output=True, check=True)
        d = json.loads(r.stdout)
        open(mp3, "wb").write(base64.b64decode(d["audio_base64"]))
        json.dump(d["alignment"], open(js, "w"))
        print("  TTS:", text[:50])
    return mp3, json.load(open(js))

def decode(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).copy()

def words_from(al):
    ch, st, en = al["characters"], al["character_start_times_seconds"], al["character_end_times_seconds"]
    words, cur = [], None
    for c, s, e in zip(ch, st, en):
        if c.isspace():
            if cur: words.append(cur); cur = None
            continue
        if cur is None: cur = {"w": "", "s": s, "e": e}
        cur["w"] += c; cur["e"] = e
    if cur: words.append(cur)
    return words

scenes, t, clips = [], 0.0, []
for sc in spec["sahneler"]:
    raw_words = sc["say"].split()
    clean = sc["say"].replace("*", "")
    mp3, al = tts(clean)
    audio = decode(mp3)
    dur_a = len(audio) / SR
    ws = words_from(al)
    for i, w in enumerate(ws):
        w["red"] = i < len(raw_words) and "*" in raw_words[i]
        w["s"] += t + LEAD; w["e"] += t + LEAD
    dur = LEAD + dur_a + PAD + sc.get("extra", 0)
    clips.append((t + LEAD, audio))
    scenes.append({**sc, "start": t, "end": t + dur, "words": ws, "narrEnd": t + LEAD + dur_a})
    t += dur
total = t + 0.4

# ---------- ses miksajı ----------
n = int(total * SR); tt = np.arange(n) / SR
mix = np.zeros(n, np.float32)
rng = np.random.default_rng(7)
# drone
lfo = 0.6 + 0.4 * np.sin(2 * np.pi * 0.07 * tt)
drone = (np.sin(2*np.pi*55*tt) + 0.6*np.sin(2*np.pi*82.6*tt) + 0.35*np.sin(2*np.pi*110.7*tt)) * lfo
brown = np.cumsum(rng.standard_normal(n)); brown -= np.convolve(brown, np.ones(4410)/4410, "same"); brown /= np.abs(brown).max()
mix += 0.035 * drone / 2 + 0.05 * brown
fade = np.minimum(1, tt / 2.0) * np.minimum(1, (total - tt) / 1.5); mix *= fade

def add(sig, at, gain=1.0):
    i = int(at * SR); j = min(n, i + len(sig))
    if i < n: mix[i:j] += gain * sig[: j - i]

def env(d, k): x = np.arange(int(d*SR))/SR; return x, np.exp(-x*k)
x, e = env(1.6, 3.2); ding = (np.sin(2*np.pi*880*x) + 0.4*np.sin(2*np.pi*1760*x) + 0.2*np.sin(2*np.pi*2640*x)) * e * np.minimum(1, x/0.004)
x, e = env(2.5, 1.6); boom = np.sin(2*np.pi*(48 - 14*x)*x) * e + 0.3*rng.standard_normal(len(x))*np.exp(-x*9)
x, e = env(0.03, 160); tick = rng.standard_normal(len(x)) * e
x, e = env(0.08, 60); clk = (np.sin(2*np.pi*1900*x) + 0.5*rng.standard_normal(len(x))) * e

for s in scenes:
    add(tick, s["start"], 0.12)
    for name, frac in s.get("sfx", []):
        add({"ding": ding, "boom": boom}[name], s["start"] + frac * (s["end"] - s["start"]), 0.22 if name == "ding" else 0.55)
    if s["v"] == "choice":
        for k in range(5):
            add(clk, s["narrEnd"] + 0.4 + k, 0.35)
for at, a in clips:
    add(a, at, 1.0)
mix /= max(1.0, np.abs(mix).max() / 0.95)
pcm = (mix * 32767).astype("<i2").tobytes()
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "s16le", "-ar", str(SR), "-ac", "1", "-i", "-",
                os.path.join(out, "ses.wav")], input=pcm, check=True)
json.dump({"title": spec["baslik"], "choice": spec.get("secim"), "total": total, "scenes": scenes},
          open(os.path.join(out, "timeline.json"), "w"), ensure_ascii=False)
print(f"Süre: {total:.1f} sn, sahne: {len(scenes)}")
