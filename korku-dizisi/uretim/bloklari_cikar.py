#!/usr/bin/env python3
"""Master prompt dosyalarindan (03a, 03b, 03c) bloklari cikarir ve bloklar.json olarak yazar.

Tek dogruluk kaynagi master .md dosyalaridir. Bir blok degisirse bu betik yeniden calistirilir.
Kullanim:  python3 uretim/bloklari_cikar.py
"""
import json
import re
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
ROW_CODE = re.compile(r"`([^`]+)`")


def fence_after(lines, start):
    """start satirindan sonra gelen ilk ``` blogunun icerigini tek satir olarak dondurur."""
    i = start
    while not lines[i].startswith("```"):
        i += 1
    j = i + 1
    buf = []
    while not lines[j].startswith("```"):
        buf.append(lines[j].strip())
        j += 1
    return " ".join(x for x in buf if x)


def son_kod(row):
    kodlar = ROW_CODE.findall(row)
    return kodlar[-1] if kodlar else None


def main():
    b = {}
    a = (KOK / "03a-karakterler-master-prompt.md").read_text(encoding="utf-8").splitlines()
    for i, ln in enumerate(a):
        if ln.startswith("## 0. GLOBAL STYLE BLOCK"):
            b["STYLE"] = fence_after(a, i)
        elif ln.startswith("## 0.1 GLOBAL NEGATIVE"):
            b["NEG"] = fence_after(a, i)
        elif ln.startswith("### CHARACTER BLOCK — "):
            ad = ln.split("— ", 1)[1].strip()
            b[f"CHAR:{ad}"] = fence_after(a, i)
        elif ln.startswith("## 7. NURTEN"):
            b["CHAR:NURTEN"] = fence_after(a, i)
        m = re.match(r"^\| \*\*([A-Z]-[A-ZİĞÜŞÖÇ]+)\*\* \|", ln)
        if m:
            b[f"OUT:{m.group(1)}"] = son_kod(ln)
        m = re.match(r"^\| \*\*(F-\d)\*\* \| (.+?) \|", ln)
        if m:
            b[f"FOTO:{m.group(1)}"] = m.group(2)
    # H-DIS ozel: "H-ANA outfit plus ..." ifadesini genislet
    if "OUT:H-DIŞ" in b and b["OUT:H-DIŞ"].startswith("H-ANA outfit"):
        b["OUT:H-DIŞ"] = b["OUT:H-ANA"] + ", " + b["OUT:H-DIŞ"].replace("H-ANA outfit plus ", "")

    m_ = (KOK / "03b-mekanlar-master-prompt.md").read_text(encoding="utf-8").splitlines()
    aktif = None
    for i, ln in enumerate(m_):
        mm = re.match(r"^### (L\d\d) ", ln)
        if mm:
            aktif = mm.group(1)
            if aktif != "L14":
                b[f"LOC:{aktif}"] = fence_after(m_, i)
            continue
        if ln.startswith("## "):
            aktif = None
        if aktif:
            t = re.match(r"^\| (T-[A-ZİĞÜŞÖÇ0-9-]+) \|", ln)
            if t:
                b[f"TIME:{aktif}:{t.group(1)}"] = son_kod(ln)
            l14 = re.match(r"^\| (L14-[A-Z]) \|", ln)
            if l14:
                b[f"LOC:{l14.group(1)}"] = son_kod(ln)

    c = (KOK / "03c-referans-gorsel-talimatlari.md").read_text(encoding="utf-8").splitlines()
    for ln in c:
        p = re.match(r"^\| (P-\d\d) \|", ln)
        if p and son_kod(ln):
            kodlar = ROW_CODE.findall(ln)
            if p.group(1) == "P-03":
                # P-03 iki parcali: duvar termostati + telefon arayuzu
                b["PROP:P-03"] = kodlar[0]
                b["PROP:P-03-UI"] = kodlar[1]
            else:
                b[f"PROP:{p.group(1)}"] = kodlar[-1]

    hedef = KOK / "uretim" / "bloklar.json"
    hedef.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{len(b)} blok yazildi -> {hedef.relative_to(KOK)}")


if __name__ == "__main__":
    main()
