#!/usr/bin/env python3
"""Bir bolumun plan listesinden (uretim/sahneler/bX.json) tam gorsel ve animasyon promptlarini uretir.

Bloklar uretim/bloklar.json'dan (master .md dosyalarindan cikarilan) kelimesi kelimesine alinir.
Kullanim:  python3 uretim/prompt_olustur.py b1
Cikti:     05-uretim-<bolum>-tam-promptlar.md  (korku-dizisi/ altinda)
"""
import json
import sys
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
KISA_STIL = ("cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, "
             "realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, "
             "vertical 9:16")
KENAN_NEG_ESKI = "missing fingers (except where specified), "
KENAN_NEG_YENI = "extra fingers on left hand, complete left index finger, "


def blok(b, anahtar):
    if anahtar not in b:
        raise SystemExit(f"HATA: '{anahtar}' blogu bloklar.json icinde yok")
    return b[anahtar]


def gorsel_prompt(b, p):
    parca = [blok(b, "STYLE")]
    if p.get("loc"):
        parca.append(blok(b, f"LOC:{p['loc']}"))
        if p.get("time"):
            parca.append(blok(b, f"TIME:{p['loc']}:{p['time']}"))
    for ad, kiyafet in p.get("chars", []):
        parca.append(f"{blok(b, f'CHAR:{ad}')}, wearing {blok(b, f'OUT:{kiyafet}')}")
    for pr in p.get("props", []):
        if pr.startswith("FOTO:"):
            continue
        parca.append(blok(b, f"PROP:{pr}"))
    parca.append(f"SHOT: {p['kadraj']}. {p['tarif']}")
    poz = ", ".join(x.strip().rstrip(",") for x in parca)

    neg = blok(b, "NEG")
    if any(ad == "KENAN" for ad, _ in p.get("chars", [])):
        neg = neg.replace(KENAN_NEG_ESKI, KENAN_NEG_YENI)
    if p.get("ek_negatif"):
        neg = f"{neg}, {p['ek_negatif']}"
    return poz, neg


def kisa_prompt(p):
    refs = [f"{ad} (character reference {ad.replace('İ', 'I')}-REF-01, outfit {k})" for ad, k in p.get("chars", [])]
    yer = f"location {p['loc']}" + (f" {p['time']}" if p.get("time") else "") if p.get("loc") else ""
    parca = [KISA_STIL, p["kadraj"], p["tarif"]]
    if yer:
        parca.append(yer + " (location reference " + p["loc"] + "-MASTER)")
    if refs:
        parca.append("characters: " + "; ".join(refs))
    return ", ".join(parca)


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Kullanim: python3 uretim/prompt_olustur.py b1")
    kod = sys.argv[1].lower()
    b = json.loads((KOK / "uretim" / "bloklar.json").read_text(encoding="utf-8"))
    ep = json.loads((KOK / "uretim" / "sahneler" / f"{kod}.json").read_text(encoding="utf-8"))

    toplam = sum(p["sure"] for p in ep["planlar"] if p["tip"] != "grafik")
    out = [f"# {ep['bolum']} — \"{ep['baslik']}\" · TAM GÖRSEL VE ANİMASYON PROMPTLARI",
           "",
           "> Bu dosya `uretim/prompt_olustur.py` tarafından otomatik üretilir. **Elle düzenlemeyin.** "
           f"Değişiklik için `uretim/sahneler/{kod}.json` ya da master `03*` dosyaları düzenlenip betik yeniden çalıştırılır.",
           "",
           f"**Plan sayısı:** {len(ep['planlar'])} · **Görsel planların toplam süresi:** {toplam} sn "
           f"(hedef {ep['sure_sn']} sn) · **Biçim:** 9:16, 1080×1920 (üretimde 2160×3840 önerilir)",
           ""]
    if abs(toplam - ep["sure_sn"]) > 0.01:
        out.append(f"> ⚠️ **SÜRE UYUŞMAZLIĞI:** planlar {toplam} sn, hedef {ep['sure_sn']} sn.")
        out.append("")
    for p in ep["planlar"]:
        out.append(f"---\n\n## {p['id']}  ·  {p['sahne']}  ·  {p['zaman']}  ·  {p['sure']} sn")
        out.append("")
        if p["tip"] == "grafik":
            out.append(f"**GRAFİK (görsel üretimi yok):** {p['tarif']}")
            out.append("")
            continue
        poz, neg = gorsel_prompt(b, p)
        meta = []
        if p.get("loc"):
            meta.append(f"Mekân `{p['loc']}`" + (f" · `{p['time']}`" if p.get("time") else ""))
        if p.get("chars"):
            meta.append("Karakter " + ", ".join(f"`{a}` ({k})" for a, k in p["chars"]))
        if p.get("props"):
            meta.append("Eşya/ref " + ", ".join(f"`{x}`" for x in p["props"]))
        out.append(" · ".join(meta) if meta else "—")
        out.append("")
        out.append("**GÖRSEL PROMPT (pozitif)**")
        out.append("```text\n" + poz + "\n```")
        out.append("**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)")
        out.append("```text\n" + kisa_prompt(p) + "\n```")
        out.append("**NEGATİF PROMPT**")
        out.append("```text\n" + neg + "\n```")
        out.append("**ANİMASYON PROMPTU (image-to-video)**")
        out.append("```text\n" + p["animasyon"] + f". Duration {p['sure']} seconds. Keep character faces, clothing and "
                   "proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, "
                   "limited animation on twos (12 fps character motion), camera: " + p["kamera"].split("·")[-1].strip() + "\n```")
        out.append(f"- **Kamera:** {p['kamera']}")
        out.append(f"- **Teknik:** {p['teknik']}")
        if p.get("grafik"):
            out.append(f"- **Montaj grafiği:** {p['grafik']}")
        if any(x.startswith("FOTO:") for x in p.get("props", [])):
            out.append("- **Referans:** Kompozisyon için F-1 fotoğraf görseli yanına konup karşılaştırılacak.")
        out.append("")
    hedef = KOK / f"05-uretim-{kod}-tam-promptlar.md"
    hedef.write_text("\n".join(out), encoding="utf-8")
    print(f"{len(ep['planlar'])} plan, {toplam} sn -> {hedef.name}")


if __name__ == "__main__":
    main()
