#!/usr/bin/env python3
"""YEDEK ANAHTAR — Bölüm 1 ANİMATİK (taslak video) üretici.

Nihai 2D sanat yerine, senaryodaki 28 planı doğru süre, kadraj, kamera hareketi, altyazı,
grafik ve ses tasarımıyla gösteren bir zamanlama ve tempo taslağıdır.
Görseller kodla çizilir (silüet/geometri), ses efektleri ve drone sentezlenir.
Seslendirme kaydı olmadığı için anlatıcı ve diyaloglar altyazı olarak verilir.

Kullanım:  python3 uretim/animatik/b1_animatik.py [--onizleme]
Çıktı:     cikti/b1-animatik.mp4
"""
import math
import re
import subprocess
import sys
import wave
from functools import lru_cache
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont
from scipy import signal

KOK = Path(__file__).resolve().parents[2]
CIKTI = KOK / "cikti"
W, H, FPS = 1080, 1920, 24
SR = 48000
ONIZLEME = "--onizleme" in sys.argv
if ONIZLEME:
    W, H = 540, 960
S = W / 1080.0  # ölçek

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"


@lru_cache(maxsize=None)
def font(size, bold=False, serif=False):
    path = FONT_SERIF if serif else (FONT_B if bold else FONT)
    return ImageFont.truetype(path, max(8, int(size * S)))


def hx(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


C = {
    "gece0": hx("0E1420"), "gece1": hx("1A2433"), "gece2": hx("2B3A4A"), "gri": hx("5C6773"),
    "termo": hx("CFE3F2"), "led": hx("E6ECEF"), "kirik": hx("E8E4DC"), "mese": hx("8A7A66"),
    "mese_k": hx("5E5244"), "yesil": hx("3F5446"), "kadife": hx("2F4A3A"), "bal": hx("C9A45C"),
    "ceviz": hx("3B2A20"), "okr": hx("B8913A"), "lacivert": hx("1F2A44"), "bej": hx("BFAE8E"),
    "ten": hx("C8A288"), "ten_k": hx("9C7A63"), "krem": hx("EFE6D2"), "kirmizi": hx("B0302C"),
    "kagit": hx("F1ECE2"), "kalem": hx("4A4A4A"), "yesil_duvar": hx("2E4436"),
}


def p(x, y):
    return (int(x * S), int(y * S))


def box(x0, y0, x1, y1):
    return [int(x0 * S), int(y0 * S), int(x1 * S), int(y1 * S)]


def grad(top, bottom, w=1080, h=1920):
    t = np.linspace(0, 1, int(h * S))[:, None, None]
    a = np.array(top, float)[None, None, :]
    b = np.array(bottom, float)[None, None, :]
    arr = (a * (1 - t) + b * t).repeat(int(w * S), axis=1)
    return Image.fromarray(arr.astype(np.uint8), "RGB")


def glow(img, cx, cy, r, color, blur=60, strength=1.0):
    lay = Image.new("RGB", img.size, (0, 0, 0))
    d = ImageDraw.Draw(lay)
    col = tuple(int(c * strength) for c in color)
    d.ellipse(box(cx - r, cy - r, cx + r, cy + r), fill=col)
    lay = lay.filter(ImageFilter.GaussianBlur(blur * S))
    return ImageChops.screen(img, lay)


def blur(img, r):
    return img.filter(ImageFilter.GaussianBlur(r * S))


def ease(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


def lerp(a, b, t):
    return a + (b - a) * t


def kamera(img, t, z0=1.0, z1=1.0, c0=(0.5, 0.5), c1=(0.5, 0.5), e=True):
    """img: büyük taban görsel. t: 0..1. z: yakınlaştırma (1 = tüm görselin W/H oranlı en büyük kesiti)."""
    tt = ease(t) if e else t
    z = lerp(z0, z1, tt)
    cx = lerp(c0[0], c1[0], tt) * img.width
    cy = lerp(c0[1], c1[1], tt) * img.height
    base = min(img.width / W, img.height / H)
    cw, ch = W * base / z, H * base / z
    l = max(0, min(img.width - cw, cx - cw / 2))
    tp = max(0, min(img.height - ch, cy - ch / 2))
    return img.resize((W, H), Image.BILINEAR, box=(l, tp, l + cw, tp + ch))


# ---------------------------------------------------------------- figürler

def bust(d, cx, cy, sc, body, head=None, hair=None, back=False):
    """Basit omuz-baş silüeti. cx,cy: boyun tabanı."""
    head = head or C["ten_k"]
    d.rounded_rectangle(box(cx - 190 * sc, cy, cx + 190 * sc, cy + 520 * sc), radius=int(120 * sc * S), fill=body)
    d.rectangle(box(cx - 38 * sc, cy - 50 * sc, cx + 38 * sc, cy + 20 * sc), fill=head)
    d.ellipse(box(cx - 92 * sc, cy - 270 * sc, cx + 92 * sc, cy - 30 * sc), fill=head)
    if hair:
        if back:
            d.ellipse(box(cx - 96 * sc, cy - 276 * sc, cx + 96 * sc, cy - 40 * sc), fill=hair)
        else:
            d.chord(box(cx - 96 * sc, cy - 280 * sc, cx + 96 * sc, cy - 120 * sc), 180, 360, fill=hair)


def figure(d, cx, fy, sc, body, head=None, hair=None, legs=None, back=False):
    """Ayakta tam boy silüet. fy: ayak tabanı."""
    head = head or C["ten_k"]
    legs = legs or tuple(max(0, c - 25) for c in body)
    hgt = 1700 * sc
    top = fy - hgt
    d.rounded_rectangle(box(cx - 70 * sc, fy - 820 * sc, cx - 8 * sc, fy), radius=int(25 * sc * S), fill=legs)
    d.rounded_rectangle(box(cx + 8 * sc, fy - 820 * sc, cx + 70 * sc, fy), radius=int(25 * sc * S), fill=legs)
    d.rounded_rectangle(box(cx - 130 * sc, top + 260 * sc, cx + 130 * sc, fy - 760 * sc), radius=int(70 * sc * S), fill=body)
    d.ellipse(box(cx - 78 * sc, top, cx + 78 * sc, top + 210 * sc), fill=head)
    if hair:
        if back:
            d.ellipse(box(cx - 82 * sc, top - 4 * sc, cx + 82 * sc, top + 190 * sc), fill=hair)
        else:
            d.chord(box(cx - 82 * sc, top - 6 * sc, cx + 82 * sc, top + 120 * sc), 180, 360, fill=hair)


def kneel(d, cx, fy, sc, body, head=None, hair=None):
    head = head or C["ten_k"]
    d.rounded_rectangle(box(cx - 160 * sc, fy - 160 * sc, cx + 120 * sc, fy), radius=int(60 * sc * S), fill=tuple(max(0, c - 25) for c in body))
    d.rounded_rectangle(box(cx - 120 * sc, fy - 700 * sc, cx + 120 * sc, fy - 120 * sc), radius=int(70 * sc * S), fill=body)
    d.ellipse(box(cx - 78 * sc, fy - 920 * sc, cx + 78 * sc, fy - 710 * sc), fill=head)
    if hair:
        d.chord(box(cx - 82 * sc, fy - 926 * sc, cx + 82 * sc, fy - 800 * sc), 180, 360, fill=hair)


AYLA_SAC = hx("3A2418")
MERT_SAC = hx("141414")

# ---------------------------------------------------------------- koridor (perspektif)

class Proj:
    def __init__(self, f=1000, cx=540, cy=960, eye=1.5):
        self.f, self.cx, self.cy, self.eye = f, cx, cy, eye

    def __call__(self, x, y, z):
        return (int((self.cx + self.f * x / z) * S), int((self.cy - self.f * (y - self.eye) / z) * S))

    def quad(self, d, pts, fill, outline=None, width=1):
        d.polygon([self(*q) for q in pts], fill=fill, outline=outline)


def koridor(gece=True, kabine=True, kisi=None, alev=False):
    """Doğu ucundan batıya (giriş kapısına) bakış. Sağ = kuzey duvarı. Taban 1188x2112."""
    big = 1.1
    img = Image.new("RGB", (int(W * big), int(H * big)), C["gece0"] if gece else C["kirik"])
    pr = Proj(f=1000 * big, cx=540 * big, cy=960 * big)
    d = ImageDraw.Draw(img)
    z0, zL, zE = 0.35, 3.6, 7.0  # yakın, alçak tavan başlangıcı, uç
    if gece:
        wallL, wallR, floor, ceil, beam, far = hx("121B27"), hx("1A2533"), hx("161A20"), hx("0F1620"), hx("1C2735"), hx("0C1119")
    else:
        wallL, wallR, floor, ceil, beam, far = hx("CFC9BE"), hx("DDD7CC"), C["mese"], hx("E6E1D8"), hx("D2CCC1"), hx("C8C1B5")
    hw = 0.6
    pr.quad(d, [(-hw, 0, z0), (hw, 0, z0), (hw, 0, zE), (-hw, 0, zE)], floor)
    # parke çizgileri
    for i in range(1, 12):
        x = -hw + i * (2 * hw / 12)
        d.line([pr(x, 0, z0), pr(x, 0, zE)], fill=tuple(max(0, c - 18) for c in floor), width=max(1, int(2 * S)))
    for zz, top in ((z0, 3.1), (zL, 2.1)):
        z_end = zL if zz == z0 else zE
        pr.quad(d, [(-hw, 0, zz), (-hw, top, zz), (-hw, top, z_end), (-hw, 0, z_end)], wallL)
        pr.quad(d, [(hw, 0, zz), (hw, top, zz), (hw, top, z_end), (hw, 0, z_end)], wallR)
        pr.quad(d, [(-hw, top, zz), (hw, top, zz), (hw, top, z_end), (-hw, top, z_end)], ceil)
    pr.quad(d, [(-hw, 2.1, zL), (hw, 2.1, zL), (hw, 3.1, zL), (-hw, 3.1, zL)], beam)
    pr.quad(d, [(-hw, 0, zE), (hw, 0, zE), (hw, 2.1, zE), (-hw, 2.1, zE)], far)
    # giriş kapısı (ceviz)
    pr.quad(d, [(-0.42, 0, zE), (0.42, 0, zE), (0.42, 2.0, zE), (-0.42, 2.0, zE)], hx("2A1E17") if gece else C["ceviz"])
    # sol duvar (güney): kombi dolabı (x0-1 -> z 6..7), banyo kapısı (z 4.7..5.4), mutfak kapısı (z 1.7..2.5)
    def lkapi(za, zb, top, col):
        pr.quad(d, [(-hw, 0, za), (-hw, top, za), (-hw, top, zb), (-hw, 0, zb)], col)
    dark = hx("0A0F16") if gece else hx("BDB6AA")
    lkapi(6.0, 6.85, 2.0, hx("101720") if gece else hx("EEEAE2"))
    # panjur çizgileri
    for k in range(10):
        yy = 0.2 + k * 0.18
        d.line([pr(-hw, yy, 6.05), pr(-hw, yy, 6.8)], fill=dark, width=max(1, int(2 * S)))
    lkapi(4.7, 5.4, 2.0, hx("111925") if gece else hx("F2EFE8"))
    lkapi(1.7, 2.5, 2.05, hx("0D131C") if gece else hx("E9E4DA"))
    # sağ duvar (kuzey): oturma odası kapısı (z 2.1..3.0, buzlu cam), termostat (z 3.5), ayakkabılık (z 4.2..5.2)
    def rquad(za, zb, y0, y1, col):
        pr.quad(d, [(hw, y0, za), (hw, y1, za), (hw, y1, zb), (hw, y0, zb)], col)
    rquad(2.1, 3.0, 0, 2.1, hx("1E2B3C") if gece else hx("D9DEE0"))
    rquad(2.15, 2.95, 0.15, 1.95, hx("2B3D52") if gece else hx("E4EAEC"))
    if kabine:
        # ayakkabılık: ön yüz (x = hw-0.35) ve üst
        xa = hw - 0.35
        pr.quad(d, [(xa, 0, 4.2), (xa, 0.9, 4.2), (xa, 0.9, 5.2), (xa, 0, 5.2)], hx("3A3128") if gece else hx("B49A72"))
        pr.quad(d, [(xa, 0.9, 4.2), (hw, 0.9, 4.2), (hw, 0.9, 5.2), (xa, 0.9, 5.2)], hx("4A3F33") if gece else hx("C8AE86"))
        pr.quad(d, [(xa, 0, 4.2), (xa, 0.9, 4.2), (hw, 0.9, 4.2), (hw, 0, 4.2)], hx("2C251E") if gece else hx("A08860"))
    # kapak (alçak tavanda, sağa yakın) — zar zor
    hatch_col = tuple(max(0, c - 6) for c in ceil)
    hz0, hz1, hx0, hx1 = 4.5, 5.1, 0.0, 0.55
    pts = [pr(hx0, 2.1, hz0), pr(hx1, 2.1, hz0), pr(hx1, 2.1, hz1), pr(hx0, 2.1, hz1)]
    d.line(pts + [pts[0]], fill=hatch_col, width=max(1, int(2 * S)))
    # termostat
    tx = pr(hw, 1.5, 3.5)
    tsz = int(26 * big * S)
    d.rectangle([tx[0] - tsz, tx[1] - tsz, tx[0] + int(tsz * 0.5), tx[1] + tsz], fill=hx("D8E8F2") if gece else hx("F5F5F2"))
    if gece:
        img = glow(img, tx[0] / S - 10, tx[1] / S, 120, C["termo"], blur=70, strength=0.55)
        img = glow(img, tx[0] / S - 10, tx[1] / S, 36, C["termo"], blur=14, strength=0.9)
        # buzlu camdan sokak ışığı
        cx_, cy_ = pr(hw, 1.1, 2.55)
        img = glow(img, cx_ / S, cy_ / S, 160, hx("7F97B0"), blur=90, strength=0.35)
    if alev:
        ax, ay = pr(-hw, 0.9, 6.4)
        img = glow(img, ax[0] / S + 20, ay[1] / S, 90, hx("FF7A1A"), blur=50, strength=0.8)
    d = ImageDraw.Draw(img)
    if kisi:
        kisi(d, pr)
    return img


def termostat_pos(big=1.1):
    pr = Proj(f=1000 * big, cx=540 * big, cy=960 * big)
    x, y = pr(0.6, 1.5, 3.5)
    return x / (W * big), y / (H * big)


# ---------------------------------------------------------------- telefon ve grafik yardımcıları

def telefon_ekrani(img, x, y, w, h, satirlar, baslik="Termostat", parlak=1.0):
    d = ImageDraw.Draw(img)
    d.rounded_rectangle(box(x, y, x + w, y + h), radius=int(40 * S), fill=hx("05070A"))
    d.rounded_rectangle(box(x + 14, y + 14, x + w - 14, y + h - 14), radius=int(30 * S), fill=tuple(int(c * parlak) for c in hx("1B2633")))
    cy = y + 90
    d.rounded_rectangle(box(x + 40, cy, x + w - 40, cy + 170), radius=int(24 * S), fill=tuple(int(c * parlak) for c in hx("2E3E50")))
    d.text(p(x + 70, cy + 22), baslik, font=font(30, bold=True), fill=tuple(int(c * parlak) for c in hx("DDE8F0")))
    for i, s in enumerate(satirlar):
        d.text(p(x + 70, cy + 70 + i * 44), s, font=font(32), fill=tuple(int(c * parlak) for c in hx("CFE3F2")))
    return img


def altyazi(img, metin):
    d = ImageDraw.Draw(img)
    satirlar = metin.split("\n")
    f = font(46)
    y0 = 1240
    for i, s in enumerate(satirlar):
        tw = d.textlength(s, font=f) / S
        x = 540 - tw / 2
        y = y0 + i * 64
        for dx, dy in ((-3, 0), (3, 0), (0, -3), (0, 3), (-2, -2), (2, 2), (-2, 2), (2, -2)):
            d.text(p(x + dx, y + dy), s, font=f, fill=(0, 0, 0))
        d.text(p(x, y), s, font=f, fill=(245, 245, 245))
    return img


def etiket(img, metin, x=60, y=150, boyut=30, renk=(220, 220, 220)):
    d = ImageDraw.Draw(img)
    d.text(p(x + 2, y + 2), metin, font=font(boyut), fill=(0, 0, 0))
    d.text(p(x, y), metin, font=font(boyut), fill=renk)
    return img


# ---------------------------------------------------------------- planlar

class Plan:
    def __init__(self, pid, sure, fn):
        self.pid, self.sure, self.fn = pid, sure, fn


def plan_s01():
    def build():
        img = grad(C["gece0"], hx("0A0E15"))
        d = ImageDraw.Draw(img)
        # yatak ve uyuyanlar (odak dışı)
        d.rounded_rectangle(box(-100, 980, 1180, 1500), radius=int(80 * S), fill=hx("1C2532"))
        d.ellipse(box(150, 900, 420, 1060), fill=hx("2A3442"))
        d.ellipse(box(560, 880, 840, 1050), fill=hx("2A3442"))
        d.rounded_rectangle(box(100, 1000, 980, 1250), radius=int(90 * S), fill=hx("27313F"))
        img = blur(img, 18)
        d = ImageDraw.Draw(img)
        # komodin
        d.rectangle(box(0, 1450, 1080, 1920), fill=hx("1A140F"))
        d.rectangle(box(0, 1440, 1080, 1470), fill=hx("2A2018"))
        # su bardağı
        d.rectangle(box(800, 1260, 900, 1450), fill=hx("1E2A36"))
        return img

    base = build()

    def fn(t, tl):
        on = ease((tl - 0.5) / 0.3)
        img = base.copy()
        img = glow(img, 540, 1400, 420, C["termo"], blur=120, strength=0.35 * on)
        img = telefon_ekrani(img, 300, 700, 480, 760, ["03:10 · Manuel ayar", "22°C → 23°C"], parlak=0.15 + 0.85 * on)
        return kamera(img, tl / 4, 1.0, 1.02)
    return Plan("B1-S01", 4, fn)


def plan_s02():
    base = koridor(gece=True, kabine=True)
    tp = termostat_pos()

    def fn(t, tl):
        if tl >= 4.5:
            img = Image.new("RGB", (W, H), C["kirik"])
            d = ImageDraw.Draw(img)
            f = font(84)
            s = "Y E D E K   A N A H T A R"
            tw = d.textlength(s, font=f) / S
            d.text(p(540 - tw / 2, 900), s, font=f, fill=C["gri"])
            return img
        return kamera(base, tl / 5, 1.0, 1.06, (0.5, 0.5), (lerp(0.5, tp[0], 0.25), lerp(0.5, tp[1], 0.25)))
    return Plan("B1-S02", 5, fn)


def bina(gun=True, uzun=True):
    hh = 3300 if uzun else 1920
    img = grad(hx("8E969C") if gun else C["gece0"], hx("B4B8B8") if gun else C["gece1"], 1080, hh)
    d = ImageDraw.Draw(img)
    # karşı binalar silüeti
    d.rectangle(box(0, 900, 120, hh), fill=hx("7E8286"))
    d.rectangle(box(960, 760, 1080, hh), fill=hx("7A7E82"))
    # bina
    bx0, bx1, top = 150, 930, 640
    d.polygon([p(bx0 - 30, top), p(540, top - 260), p(bx1 + 30, top)], fill=hx("7A4A36"))
    d.rectangle(box(bx0, top, bx1, hh - 520), fill=hx("D6CDB8"))
    floors = 4
    fh = (hh - 520 - top) / floors
    for f_ in range(floors):
        y = top + f_ * fh + 120
        for i in range(4):
            x = bx0 + 60 + i * 190
            karanlik = (f_ == 0 and i < 2)  # en üst kat, sol yarı = Daire 7
            col = hx("1B2027") if karanlik else hx("59636B")
            d.rectangle(box(x, y, x + 120, y + 230), fill=col)
            d.rectangle(box(x - 8, y + 230, x + 128, y + 246), fill=hx("BDB3A0"))
    # kapı
    d.rectangle(box(470, hh - 830, 610, hh - 520), fill=C["ceviz"])
    d.text(p(430, hh - 880), "IHLAMUR APT. 1978", font=font(22, bold=True), fill=hx("4A5A6A"))
    # sokak
    d.rectangle(box(0, hh - 520, 1080, hh), fill=hx("4C4F52"))
    for k in range(40):
        yy = hh - 500 + (k % 8) * 62
        xx = (k * 137) % 1080
        d.ellipse(box(xx, yy, xx + 70, yy + 30), outline=hx("3E4144"), width=max(1, int(2 * S)))
    # kepenkli dükkân (sağ alt)
    d.rectangle(box(960, hh - 830, 1080, hh - 520), fill=hx("6A6E70"))
    for k in range(10):
        d.line([p(960, hh - 820 + k * 30), p(1080, hh - 820 + k * 30)], fill=hx("5A5E60"), width=max(1, int(2 * S)))
    return img


def plan_s03():
    base = bina()
    hh = base.height / S

    def fn(t, tl):
        img = base.copy()
        d = ImageDraw.Draw(img)
        fy = hh - 140
        k = ease(tl / 8)
        # Mert koliyle, kapıya yürür
        mx = 380 + 60 * k
        figure(d, mx, fy, 0.22, C["lacivert"], hair=MERT_SAC)
        d.rectangle(box(mx - 55, fy - 300, mx + 55, fy - 200), fill=hx("A68A5E"))
        # Ayla bitkiyle, başını kaldırır
        figure(d, 700, fy, 0.2, hx("3E4A36"), hair=AYLA_SAC)
        d.ellipse(box(670, fy - 260, 730, fy - 200), fill=hx("2F5A34"))
        d.rectangle(box(685, fy - 210, 715, fy - 180), fill=hx("8A5A3A"))
        d.rectangle(box(250, fy - 60, 320, fy), fill=hx("A68A5E"))
        # martı
        gx = 1100 - 1300 * (tl / 8)
        d.line([p(gx, 900), p(gx + 25, 885), p(gx + 50, 900)], fill=hx("30353A"), width=max(1, int(4 * S)))
        # yağmur
        rng = np.random.default_rng(int(tl * 24))
        for _ in range(60):
            x = rng.uniform(0, 1080)
            y = rng.uniform(0, hh)
            d.line([p(x, y), p(x - 4, y + 30)], fill=hx("A6AEB4"), width=1)
        fr = kamera(img, tl / 8, 1.0, 1.0, (0.5, 1 - (1920 / hh) / 2), (0.5, (1920 / hh) / 2 + 0.05))
        return etiket(fr, "5 gün önce", 60, 150, 34)
    return Plan("B1-S03", 8, fn)


def sahanlik_bg():
    img = grad(hx("C9C1AE"), hx("A69C88"))
    d = ImageDraw.Draw(img)
    d.rectangle(box(0, 1100, 1080, 1920), fill=C["yesil_duvar"])
    d.rectangle(box(0, 1090, 1080, 1110), fill=hx("23352A"))
    return img


def plan_s04a():
    def fn(t, tl):
        img = blur(sahanlik_bg(), 20)
        d = ImageDraw.Draw(img)
        # avuç
        d.ellipse(box(180, 900, 900, 1600), fill=C["ten"])
        for i, ang in enumerate((-30, -10, 10, 30)):
            x = 330 + i * 120
            d.rounded_rectangle(box(x, 700 + abs(ang) * 3, x + 100, 1050), radius=int(50 * S), fill=C["ten"])
        d.rounded_rectangle(box(780, 1100, 1000, 1220), radius=int(55 * S), fill=C["ten"])
        # gümüş yüzük sağ işaret parmağı
        d.rectangle(box(330, 960, 430, 985), fill=hx("C8CCD0"))
        # anahtarlar düşüş
        k = ease(tl / 0.6)
        oy = (1 - k) * -500 + math.sin(min(1, tl / 0.6) * math.pi) * -20
        d.ellipse(box(470, 1080 + oy, 610, 1220 + oy), outline=hx("A0A6AC"), width=int(10 * S))
        d.rounded_rectangle(box(380, 1180 + oy, 620, 1230 + oy), radius=int(20 * S), fill=hx("B8BEC4"))
        d.rounded_rectangle(box(420, 1250 + oy, 660, 1300 + oy), radius=int(20 * S), fill=hx("9AA0A6"))
        ang = min(1, max(0, (tl - 1.5) / 1.5)) * 25
        bx = 450 + ang
        d.rounded_rectangle(box(bx, 1320 + oy, bx + 260, 1375 + oy), radius=int(20 * S), fill=hx("B08A3C"))
        d.text(p(bx + 60, 1332 + oy), "SARI ANAHTAR", font=font(18, bold=True), fill=hx("6A5020"))
        # Hikmet'in eli yukarıdan çekilir
        hy = -200 - 400 * ease((tl - 0.8) / 1.2)
        d.rounded_rectangle(box(420, hy, 720, hy + 520), radius=int(60 * S), fill=C["bej"])
        d.rounded_rectangle(box(450, hy + 480, 700, hy + 700), radius=int(60 * S), fill=hx("C49A80"))
        d.rectangle(box(640, hy + 600, 690, hy + 630), fill=hx("C9A13A"))
        return img
    return Plan("B1-S04a", 4, fn)


def plan_s04b():
    def fn(t, tl):
        img = sahanlik_bg()
        d = ImageDraw.Draw(img)
        # Daire 7 kapı pervazı (solda)
        d.rectangle(box(0, 300, 260, 1920), fill=C["ceviz"])
        d.text(p(120, 700), "7", font=font(60, bold=True), fill=hx("C9A13A"))
        bust(d, 690, 1050, 1.25, C["bej"], head=hx("C98E7A"))
        # kel tepe, yan saçlar, bıyık, gölgeli göz çukurları
        d.chord(box(570, 700, 810, 830), 180, 360, fill=hx("D79E89"))
        d.rectangle(box(575, 820, 600, 920), fill=hx("9C9C9C"))
        d.rectangle(box(780, 820, 805, 920), fill=hx("9C9C9C"))
        gaze = 1 if 2.0 < tl < 3.5 else 0
        for ex in (640, 740):
            d.ellipse(box(ex - 30, 840, ex + 30, 880), fill=hx("4A3028"))
            d.ellipse(box(ex - 10 - 12 * gaze, 852, ex + 6 - 12 * gaze, 868), fill=hx("1A1210"))
        d.rounded_rectangle(box(630, 930, 750, 965), radius=int(14 * S), fill=hx("8E8E8E"))
        konus = 1.0 <= tl <= 3.0
        mo = 10 if konus and int(tl * 8) % 2 == 0 else 3
        d.rectangle(box(660, 975, 720, 975 + mo), fill=hx("5A3028"))
        # tespih (sağ el, göğüs hizası)
        d.ellipse(box(720, 1300, 900, 1420), fill=hx("B48C70"))
        n = int(tl * 6)
        for i in range(9):
            a = (i + n) / 9 * math.pi * 2
            x = 810 + 70 * math.cos(a)
            y = 1440 + 30 * math.sin(a) + 40
            d.ellipse(box(x - 12, y - 12, x + 12, y + 12), fill=hx("6E4A1E"))
        # sert üst ışık
        img = glow(img, 690, 200, 300, (90, 90, 70), blur=120, strength=0.6)
        j = (math.sin(tl * 3.1) * 0.003, math.cos(tl * 2.3) * 0.003)
        return kamera(img, 0, 1.03, 1.03, (0.5 + j[0], 0.5 + j[1]), (0.5 + j[0], 0.5 + j[1]))
    return Plan("B1-S04b", 5, fn)


def plan_s05a():
    def fn(t, tl):
        img = sahanlik_bg()
        d = ImageDraw.Draw(img)
        # Daire 8 kapısı, zincirli aralık
        d.rectangle(box(280, 300, 800, 1920), fill=C["ceviz"])
        d.text(p(500, 700), "8", font=font(60, bold=True), fill=hx("C9A13A"))
        d.rectangle(box(760, 300, 800, 1920), fill=C["bal"])
        img = glow(img, 790, 1000, 180, C["bal"], blur=80, strength=0.6)
        d = ImageDraw.Draw(img)
        # Ayla arkadan (ön plan, odak dışı)
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0))
        dl = ImageDraw.Draw(lay)
        bust(dl, 180 + 10 * ease(tl / 4), 1500, 1.6, hx("3E4A36"), hair=AYLA_SAC, back=True)
        lay = lay.filter(ImageFilter.GaussianBlur(10 * S))
        img.paste(lay, (0, 0), lay)
        return kamera(img, tl / 4, 1.0, 1.04, (0.5, 0.5), (0.58, 0.5))
    return Plan("B1-S05a", 4, fn)


def plan_s05b():
    def fn(t, tl):
        img = Image.new("RGB", (W, H), C["ceviz"])
        d = ImageDraw.Draw(img)
        kapan = ease((tl - 3.5) / 1.5)
        gap_w = 330 * (1 - kapan)
        x0 = 540 - gap_w / 2
        x1 = 540 + gap_w / 2
        if gap_w > 4:
            strip = Image.new("RGB", (W, H), C["bal"])
            ds = ImageDraw.Draw(strip)
            # yüz şeridi
            ds.rectangle(box(300, 0, 800, 1920), fill=hx("D8B7A0"))
            ds.ellipse(box(380, 560, 700, 880), outline=hx("5A3A22"), width=int(16 * S))  # gözlük camı
            ds.ellipse(box(470, 650, 610, 790), fill=hx("F2EEE6"))
            ds.ellipse(box(510, 690, 570, 750), fill=hx("6A4A2A"))
            for k in range(6):
                ds.line([p(330, 950 + k * 30), p(520, 940 + k * 34)], fill=hx("B8977F"), width=max(1, int(3 * S)))
            ds.rectangle(box(330, 1350, 800, 1420), fill=hx("D9B83A"))  # mezura
            konus = 0.8 <= tl <= 3.8
            mo = 18 if konus and int(tl * 7) % 2 == 0 else 6
            ds.rectangle(box(420, 1150, 640, 1150 + mo), fill=hx("7A4A3A"))
            mask = Image.new("L", (W, H), 0)
            ImageDraw.Draw(mask).rectangle(box(x0, 0, x1, 1920), fill=255)
            img.paste(strip, (0, 0), mask)
            d = ImageDraw.Draw(img)
            # zincir
            for k in range(8):
                cx = x0 - 60 + k * ((gap_w + 120) / 7)
                d.ellipse(box(cx - 22, 980 - 12, cx + 22, 980 + 12), outline=hx("C9A13A"), width=int(6 * S))
        return img
    return Plan("B1-S05b", 5, fn)


def oturma(gun=True, koltuk="pencere", bant=False, gece=False, lamba=False):
    """Oturma odası, koridor kapısından kuzeye (pencerelere) bakış."""
    if gece:
        img = grad(hx("101722"), hx("0B1018"))
    else:
        img = grad(hx("D9D4CA"), hx("C4BEB3"))
    d = ImageDraw.Draw(img)
    # zemin
    d.polygon([p(0, 1300), p(1080, 1300), p(1080, 1920), p(0, 1920)], fill=hx("2A2622") if gece else C["mese"])
    for k in range(14):
        d.line([p(540 + (k - 7) * 30, 1300), p(540 + (k - 7) * 160, 1920)], fill=hx("221F1C") if gece else hx("7A6B58"), width=max(1, int(2 * S)))
    # pencereler
    for wx in (300, 650):
        col = hx("2E4258") if gece else hx("E9EEF0")
        d.rectangle(box(wx, 420, wx + 220, 900), fill=col)
        d.rectangle(box(wx + 105, 420, wx + 115, 900), fill=hx("C9C3B8") if not gece else hx("1E2836"))
        d.rectangle(box(wx - 40, 380, wx, 1000), fill=hx("3D4148") if not gece else hx("161C26"))
        d.rectangle(box(wx + 220, 380, wx + 260, 1000), fill=hx("3D4148") if not gece else hx("161C26"))
        d.rectangle(box(wx, 1040, wx + 220, 1110), fill=hx("EDEDED") if not gece else hx("2A3340"))
    # kitaplık (sol, batı duvarı)
    d.polygon([p(0, 250), p(170, 330), p(170, 1300), p(0, 1420)], fill=hx("ECE8E0") if not gece else hx("1C2330"))
    for k in range(6):
        y = 380 + k * 160
        d.line([p(0, y - 40), p(170, y)], fill=hx("BDB7AC") if not gece else hx("151B26"), width=int(8 * S))
    # dört soluk iz (kitaplığın önü)
    for (ix, iy) in ((210, 1420), (330, 1400), (240, 1520), (370, 1500)):
        d.ellipse(box(ix - 18, iy - 9, ix + 18, iy + 9), fill=hx("6A5B48") if not gece else hx("1A1714"))
    # kanepe (doğu duvarı, sağ)
    d.rounded_rectangle(box(860, 1050, 1080, 1460), radius=int(30 * S), fill=hx("7A7E82") if not gece else hx("222831"))
    # monstera
    d.ellipse(box(560, 900, 720, 1080), fill=hx("2F5A34") if not gece else hx("1A2A20"))
    d.rectangle(box(610, 1080, 670, 1180), fill=hx("8A5A3A") if not gece else hx("2A2018"))
    if bant:
        d.rectangle(box(330, 1250, 600, 1530), outline=hx("E8D9A8"), width=int(10 * S))
    if koltuk == "pencere":
        _koltuk(d, 465, 1440, 1.0, gece)
    elif koltuk == "kitaplik":
        _koltuk(d, 290, 1500, 1.05, gece)
    if gece:
        img = glow(img, 530, 700, 400, hx("6F86A0"), blur=140, strength=0.35)
    if lamba:
        img = glow(img, 980, 1000, 300, hx("F0C987"), blur=120, strength=0.6)
    return img


def _koltuk(d, cx, by, sc, gece=False):
    col = C["kadife"] if not gece else hx("17241C")
    d.rounded_rectangle(box(cx - 150 * sc, by - 330 * sc, cx + 150 * sc, by - 60 * sc), radius=int(50 * sc * S), fill=col)
    d.rounded_rectangle(box(cx - 190 * sc, by - 180 * sc, cx + 190 * sc, by - 40 * sc), radius=int(40 * sc * S), fill=tuple(max(0, c - 12) for c in col))
    for lx in (-150, 150):
        d.rectangle(box(cx + lx * sc - 10, by - 50 * sc, cx + lx * sc + 10, by), fill=hx("3B2A20"))


def plan_s06a():
    def fn(t, tl):
        img = oturma(koltuk="pencere")
        d = ImageDraw.Draw(img)
        k = ease(tl / 1.5)
        figure(d, 700 - 60 * k, 1700, 0.55, C["okr"], hair=AYLA_SAC, legs=hx("3C3C40"))
        return img
    return Plan("B1-S06a", 4, fn)


def plan_s06b():
    def fn(t, tl):
        img = oturma(koltuk=None)
        d = ImageDraw.Draw(img)
        kneel(d, 420, 1720, 0.7, C["lacivert"], hair=MERT_SAC)
        dx = 4 if 0.5 < tl < 1.5 and int(tl * 30) % 2 else 0
        d.rectangle(box(540 + dx, 1200, 660 + dx, 1250), fill=hx("2A2A2A"))
        d.rectangle(box(560 + dx, 1250, 600 + dx, 1330), fill=hx("C0392B"))
        return kamera(img, 0, 1.15, 1.15, (0.4, 0.62), (0.4, 0.62))
    return Plan("B1-S06b", 3, fn)


def mutfak(gece=False):
    img = grad(hx("CDD3D6"), hx("B6BDC1"))
    d = ImageDraw.Draw(img)
    d.rectangle(box(0, 0, 1080, 1100), fill=hx("E8EAEA"))
    for r in range(18):
        for c_ in range(12):
            off = 45 if r % 2 else 0
            d.rectangle(box(c_ * 90 + off, r * 45 + 200, c_ * 90 + off + 86, r * 45 + 241), outline=hx("D0D4D4"))
    d.rectangle(box(620, 180, 980, 640), fill=hx("D7DDE0"))
    d.rectangle(box(790, 180, 810, 640), fill=hx("BFC6CA"))
    d.rectangle(box(0, 1100, 1080, 1180), fill=hx("8C8F90"))
    d.rectangle(box(0, 1180, 1080, 1920), fill=hx("F2F1EC"))
    for c_ in range(5):
        d.rectangle(box(c_ * 216 + 10, 1210, c_ * 216 + 206, 1880), outline=hx("D5D3CC"), width=int(4 * S))
    return img


def plan_s06c():
    def fn(t, tl):
        img = mutfak()
        d = ImageDraw.Draw(img)
        bust(d, 330, 1150, 1.0, C["okr"], hair=AYLA_SAC)
        # Ayla şakağa iki parmak
        a = math.sin(tl * 3) * 6
        d.rounded_rectangle(box(390 + a, 900, 430 + a, 1020), radius=int(18 * S), fill=C["ten"])
        bust(d, 760, 1120, 1.05, C["lacivert"], hair=MERT_SAC)
        d.rectangle(box(800, 960, 850, 1060), fill=hx("C8D8E0"))  # su bardağı
        konus = 1.0 <= tl <= 2.0
        mo = 12 if konus and int(tl * 8) % 2 == 0 else 4
        d.rectangle(box(735, 1000, 785, 1000 + mo), fill=hx("5A3028"))
        return img
    return Plan("B1-S06c", 3, fn)


def kupa(d, cx, cy, sc, aci):
    """aci: kulp yönü derece (0 = sağ, 180 = sol)."""
    d.ellipse(box(cx - 170 * sc, cy + 230 * sc, cx + 170 * sc, cy + 290 * sc), fill=hx("9A9A94"))
    on_arka = math.sin(math.radians(aci))
    hxp = cx + math.cos(math.radians(aci)) * 200 * sc
    if on_arka < 0:
        d.ellipse(box(hxp - 70 * sc, cy - 60 * sc, hxp + 70 * sc, cy + 150 * sc), outline=C["krem"], width=int(34 * sc * S))
    d.rectangle(box(cx - 160 * sc, cy - 150 * sc, cx + 160 * sc, cy + 260 * sc), fill=C["krem"])
    d.ellipse(box(cx - 160 * sc, cy + 200 * sc, cx + 160 * sc, cy + 290 * sc), fill=C["krem"])
    d.ellipse(box(cx - 160 * sc, cy - 190 * sc, cx + 160 * sc, cy - 110 * sc), fill=hx("D9CFBA"))
    d.arc(box(cx - 160 * sc, cy - 190 * sc, cx + 160 * sc, cy - 110 * sc), 0, 180, fill=C["lacivert"], width=int(10 * sc * S))
    if on_arka >= 0:
        d.ellipse(box(hxp - 70 * sc, cy - 60 * sc, hxp + 70 * sc, cy + 150 * sc), outline=C["krem"], width=int(34 * sc * S))
        d.line([p(hxp - 20 * sc, cy - 40 * sc), p(hxp - 5 * sc, cy)], fill=hx("8A7A60"), width=max(1, int(3 * S)))


def plan_s07a():
    def fn(t, tl):
        img = blur(mutfak(), 14)
        d = ImageDraw.Draw(img)
        d.rectangle(box(0, 1200, 1080, 1920), fill=hx("8C8F90"))
        kupa(d, 540, 1100, 1.2, 180)
        return img
    return Plan("B1-S07a", 4, fn)


def eskiz_kagit(img=None):
    img = img or Image.new("RGB", (W, H), C["kagit"])
    d = ImageDraw.Draw(img)
    rng = np.random.default_rng(3)
    for _ in range(4000):
        x, y = rng.uniform(0, 1080), rng.uniform(0, 1920)
        d.point(p(x, y), fill=hx("E2DCD0"))
    return img


def plan_s07b():
    def fn(t, tl):
        img = eskiz_kagit()
        d = ImageDraw.Draw(img)
        k = C["kalem"]
        w = max(1, int(4 * S))
        d.line([p(80, 1200), p(1000, 1200)], fill=k, width=w)
        d.line([p(80, 1250), p(1000, 1250)], fill=k, width=w)
        d.rectangle(box(380, 820, 700, 1190), outline=k, width=w)
        d.ellipse(box(380, 780, 700, 860), outline=k, width=w)
        d.ellipse(box(690, 900, 840, 1110), outline=k, width=int(6 * S))  # kulp SAĞDA
        for i in range(12):
            d.line([p(400 + i * 24, 900), p(420 + i * 24, 1180)], fill=hx("9A9A9A"), width=1)
        d.text(p(820, 1700), "4.11", font=font(30, serif=True), fill=hx("8A8A8A"))
        return img
    return Plan("B1-S07b", 3, fn)


def plan_s07c():
    def fn(t, tl):
        img = blur(mutfak(), 14)
        d = ImageDraw.Draw(img)
        d.rectangle(box(0, 1200, 1080, 1920), fill=hx("8C8F90"))
        k = ease(tl / 1.6)
        aci = 180 - 180 * k
        kupa(d, 540, 1100, 1.2, aci)
        # el
        hx_ = 540 + math.cos(math.radians(aci)) * 240
        d.rounded_rectangle(box(hx_ - 80, 700, hx_ + 80, 1000), radius=int(60 * S), fill=C["ten"])
        d.rectangle(box(hx_ - 90, 560, hx_ + 90, 720), fill=C["okr"])
        d.rectangle(box(hx_ - 50, 820, hx_ + 10, 842), fill=hx("C8CCD0"))
        return img
    return Plan("B1-S07c", 3, fn)


def koridor_giris_gun(ayla=True, mert_t=None):
    """Girişten doğuya bakış (kabine solda/kuzey). Basit çizim."""
    img = grad(hx("DCD6CB"), hx("C9C2B6"))
    d = ImageDraw.Draw(img)
    vx, vy = 540, 900
    d.polygon([p(0, 0), p(1080, 0), p(700, 700), p(380, 700)], fill=hx("E6E1D8"))
    d.polygon([p(0, 1920), p(1080, 1920), p(700, 1150), p(380, 1150)], fill=C["mese"])
    d.polygon([p(0, 0), p(380, 700), p(380, 1150), p(0, 1920)], fill=hx("DDD7CC"))
    d.polygon([p(1080, 0), p(700, 700), p(700, 1150), p(1080, 1920)], fill=hx("CFC9BE"))
    d.rectangle(box(380, 700, 700, 1150), fill=hx("D2CCC1"))
    d.line([p(0, 330), p(1080, 330)], fill=hx("C8C2B8"), width=int(6 * S))  # kiriş
    # ayakkabılık sol duvar
    d.polygon([p(140, 1150), p(300, 1060), p(300, 1300), p(140, 1430)], fill=hx("B49A72"))
    d.polygon([p(140, 1150), p(300, 1060), p(360, 1070), p(200, 1165)], fill=hx("C8AE86"))
    # termostat sol duvar
    d.rectangle(box(318, 860, 340, 900), fill=hx("F5F5F2"))
    # sağ duvar: banyo kapısı, kombi panjuru
    d.polygon([p(820, 380), p(940, 300), p(940, 1460), p(820, 1300)], fill=hx("F2EFE8"))
    if ayla:
        figure(d, 380, 1520, 0.6, C["okr"], hair=AYLA_SAC, legs=hx("3C3C40"))
    if mert_t is not None:
        sc = lerp(0.55, 1.4, mert_t)
        fx = lerp(560, 120, mert_t)
        figure(d, fx, lerp(1450, 2400, mert_t), sc, C["lacivert"], hair=MERT_SAC)
    return img


def plan_s08a():
    def fn(t, tl):
        mt = ease(tl / 4.2) if tl < 4.2 else None
        return koridor_giris_gun(ayla=True, mert_t=mt)
    return Plan("B1-S08a", 5, fn)


def plan_s08b():
    def fn(t, tl):
        img = Image.new("RGB", (W, H), C["mese"])
        d = ImageDraw.Draw(img)
        for k in range(30):
            y = k * 70
            d.line([p(0, y), p(1080, y + 200)], fill=hx("7A6B58"), width=max(1, int(3 * S)))
            d.line([p(0, y + 35), p(-200, y + 400)], fill=hx("7A6B58"), width=max(1, int(2 * S)))
        for off in (0, 70):
            d.line([p(200 + off, 1920), p(620 + off, 300)], fill=hx("C2B49E"), width=int(8 * S))
        d.rectangle(box(500, 0, 1080, 380), fill=hx("B49A72"))
        img = glow(img, 600, 900, 200, (60, 55, 45), blur=80, strength=0.5)
        return img
    return Plan("B1-S08b", 3, fn)


def plan_s08c():
    base = Image.new("RGB", (W, int(H * 1.8)), hx("E6E1D8"))
    d = ImageDraw.Draw(base)
    d.rectangle(box(0, 1920 * 0.8, 1080, 1920 * 1.8), fill=hx("D8D2C7"))  # duvar alt kısım
    d.line([p(0, 1920 * 0.8), p(1080, 1920 * 0.8)], fill=hx("C2BCB1"), width=int(6 * S))
    d.line([p(0, 160), p(1080, 160)], fill=hx("CBC5BA"), width=int(10 * S))  # kiriş
    d.rectangle(box(380, 520, 700, 840), outline=hx("DAD4C9"), width=max(1, int(3 * S)))
    base = base.filter(ImageFilter.GaussianBlur(1))

    def fn(t, tl):
        u = min(1.0, tl / 1.5)
        return kamera(base, u, 1.0, 1.0, (0.5, 0.72), (0.5, 0.28))
    return Plan("B1-S08c", 3, fn)


def eskiz_duvari(img, n=12, yuvarlak=None):
    d = ImageDraw.Draw(img)
    k = C["kalem"]
    for i in range(n):
        r, c_ = divmod(i, 3)
        x0, y0 = 60 + c_ * 330, 260 + r * 360
        d.rectangle(box(x0, y0, x0 + 300, y0 + 320), fill=C["kagit"])
        tip = c_
        if tip == 0:  # koridor
            d.line([p(x0 + 20, y0 + 20), p(x0 + 130, y0 + 140)], fill=k)
            d.line([p(x0 + 280, y0 + 20), p(x0 + 170, y0 + 140)], fill=k)
            d.line([p(x0 + 20, y0 + 300), p(x0 + 130, y0 + 200)], fill=k)
            d.line([p(x0 + 280, y0 + 300), p(x0 + 170, y0 + 200)], fill=k)
            d.rectangle(box(x0 + 130, y0 + 140, x0 + 170, y0 + 200), outline=k)
            d.rectangle(box(x0 + 40 + (30 if r > 0 else 0), y0 + 210, x0 + 90 + (30 if r > 0 else 0), y0 + 260), outline=k)
        elif tip == 1:  # mutfak
            d.line([p(x0 + 20, y0 + 200), p(x0 + 280, y0 + 200)], fill=k)
            d.rectangle(box(x0 + 120, y0 + 130, x0 + 170, y0 + 198), outline=k)
            hxp = x0 + 190 if r == 0 else x0 + 100
            d.ellipse(box(hxp - 12, y0 + 145, hxp + 12, y0 + 180), outline=k)
        else:  # oturma
            d.rectangle(box(x0 + 40, y0 + 40, x0 + 120, y0 + 160), outline=k)
            d.rectangle(box(x0 + 170, y0 + 40, x0 + 250, y0 + 160), outline=k)
            d.rectangle(box(x0 + 110, y0 + 200, x0 + 190, y0 + 270), outline=k)
        if yuvarlak and i in yuvarlak:
            d.ellipse(box(x0 + 20, y0 + 160, x0 + 140, y0 + 290), outline=C["kirmizi"], width=int(6 * S))
    return img


def plan_s09a():
    def fn(t, tl):
        img = grad(hx("6F6A60"), hx("4C4842"), 1500, 1920)
        img = eskiz_duvari(img, 12, yuvarlak=[3, 4] + ([7] if tl > 4 else []))
        d = ImageDraw.Draw(img)
        bust(d, 1300, 1450, 1.0, C["okr"], hair=AYLA_SAC, back=True)
        img = glow(img, 1350, 300, 300, hx("F0C987"), blur=120, strength=0.5)
        return kamera(img, tl / 6, 1.0, 1.0, (0.36, 0.5), (0.64, 0.5))
    return Plan("B1-S09a", 6, fn)


def plan_s09b():
    def fn(t, tl):
        i = min(2, int(tl / (5 / 3)))
        local = (tl - i * 5 / 3) / (5 / 3)
        img = eskiz_kagit()
        d = ImageDraw.Draw(img)
        k = C["kalem"]
        w = max(1, int(5 * S))
        if i == 0:
            d.rectangle(box(380, 820, 700, 1190), outline=k, width=w)
            d.ellipse(box(240, 900, 390, 1110), outline=k, width=w)
            d.ellipse(box(180, 840, 450, 1170), outline=C["kirmizi"], width=int(10 * S))
        elif i == 1:
            d.rectangle(box(250, 1000, 830, 1060), outline=k, width=w)
            d.rectangle(box(400, 1060, 560, 1300), outline=k, width=w)
            d.ellipse(box(330, 980, 640, 1360), outline=C["kirmizi"], width=int(10 * S))
        else:
            d.line([p(100, 300), p(450, 800)], fill=k, width=w)
            d.line([p(980, 300), p(630, 800)], fill=k, width=w)
            d.line([p(100, 1700), p(450, 1150)], fill=k, width=w)
            d.line([p(980, 1700), p(630, 1150)], fill=k, width=w)
            d.rectangle(box(450, 800, 630, 1150), outline=k, width=w)
            d.rectangle(box(300, 1180, 470, 1400), outline=k, width=w)
            d.ellipse(box(240, 1120, 540, 1460), outline=C["kirmizi"], width=int(10 * S))
        return kamera(img, local, 1.0, 1.05)
    return Plan("B1-S09b", 5, fn)


def plan_s10():
    def fn(t, tl):
        lamba = tl < 8.0
        img = oturma(koltuk="pencere", bant=tl > 2, gece=not lamba, lamba=lamba)
        if lamba:
            img = Image.blend(img, Image.new("RGB", img.size, hx("2A2622")), 0.35)
        d = ImageDraw.Draw(img)
        # Mert arka planda kanepede (odak dışı) + telefon ışığı
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0))
        dl = ImageDraw.Draw(lay)
        bust(dl, 960, 1150, 0.55, C["lacivert"], hair=MERT_SAC)
        lay = lay.filter(ImageFilter.GaussianBlur(6 * S))
        img.paste(lay, (0, 0), lay)
        bak = 3.5 < tl < 5.0
        img = glow(img, 930, 1080 if not bak else 1060, 60, C["termo"], blur=30, strength=0.6)
        d = ImageDraw.Draw(img)
        # Ayla ön planda dizlerinin üstünde
        kneel(d, 330, 1900, 0.9, C["okr"] if lamba else hx("4A3B1A"), hair=AYLA_SAC)
        return kamera(img, 0, 1.0, 1.0)
    return Plan("B1-S10", 9, fn)


def plan_s11():
    def fn(t, tl):
        img = Image.new("RGB", (W, H), (2, 3, 5))
        d = ImageDraw.Draw(img)
        on = tl >= 1.0
        d.rounded_rectangle(box(300, 700, 780, 1180), radius=int(30 * S), fill=hx("1A2430"))
        d.rounded_rectangle(box(340, 760, 740, 1060), radius=int(16 * S), fill=hx("BFD8EA") if on else hx("A9C4D8"))
        sayi = "23" if on else "22"
        f = font(190, bold=True)
        tw = d.textlength(sayi, font=f) / S
        d.text(p(540 - tw / 2, 790), sayi, font=f, fill=hx("1A2A3A"))
        d.text(p(640, 830), "°C", font=font(50), fill=hx("1A2A3A"))
        img = glow(img, 540, 910, 380, C["termo"], blur=120, strength=0.5 if on else 0.38)
        return img
    return Plan("B1-S11", 7, fn)


def plan_s12a():
    def fn(t, tl):
        img = oturma(koltuk=None, bant=True)
        img = Image.blend(img, Image.new("RGB", img.size, hx("8A93A0")), 0.18)
        d = ImageDraw.Draw(img)
        figure(d, 540, 1780, 0.75, hx("BFC3C6"), hair=AYLA_SAC, legs=hx("A9ADB0"))
        d.rectangle(box(400, 900, 680, 1100), fill=C["okr"])
        j = math.sin(tl * 40) * 2
        d.rectangle(box(600 + j, 1080, 650 + j, 1140), fill=hx("F0EDE6"))
        return img
    return Plan("B1-S12a", 3, fn)


def plan_s12b():
    def fn(t, tl):
        img = Image.new("RGB", (W, H), C["mese"])
        d = ImageDraw.Draw(img)
        for k in range(40):
            d.line([p(0, k * 60), p(1080, k * 60 + 180)], fill=hx("7A6B58"), width=max(1, int(2 * S)))
        d.rectangle(box(220, 600, 860, 1350), outline=hx("E8D9A8"), width=int(22 * S))
        img = glow(img, 540 + 60 * tl, 400, 500, (90, 95, 100), blur=150, strength=0.4)
        return img
    return Plan("B1-S12b", 3, fn)


def plan_s12c():
    base = Image.new("RGB", (W, int(H * 2.2)), C["mese"])
    d = ImageDraw.Draw(base)
    for k in range(80):
        d.line([p(0, k * 60), p(1080, k * 60 + 180)], fill=hx("7A6B58"), width=max(1, int(2 * S)))
    for i in range(4):
        x = 330 + i * 120
        d.line([p(x, 0), p(x + (i - 1.5) * 20, 1920 * 2.2)], fill=hx("C6B9A3"), width=int(7 * S))
    d.rectangle(box(0, 0, 1080, 260), fill=hx("ECE8E0"))

    def fn(t, tl):
        return kamera(base, tl / 4, 1.0, 1.0, (0.5, 0.78), (0.5, 0.25), e=False)
    return Plan("B1-S12c", 4, fn)


def plan_s12d():
    def fn(t, tl):
        img = oturma(koltuk="kitaplik", bant=True)
        return kamera(img, tl / 3, 1.25, 1.27, (0.35, 0.65), (0.35, 0.65))
    return Plan("B1-S12d", 3, fn)


def plan_s12e():
    def fn(t, tl):
        img = Image.new("RGB", (W, H), C["mese"])
        d = ImageDraw.Draw(img)
        for k in range(40):
            d.line([p(0, k * 60), p(1080, k * 60 + 180)], fill=hx("7A6B58"), width=max(1, int(2 * S)))
        d.ellipse(box(420, 1360, 660, 1460), fill=hx("4E4134"))  # çukur
        if tl < 1.0:
            lift = 120 * ease(tl / 1.0)
        elif tl < 2.5:
            lift = 120
        else:
            lift = 120 * (1 - ease((tl - 2.5) / 0.15))
        y = 1410 - lift
        d.rectangle(box(470, 300, 610, y), fill=hx("3B2A20"))
        d.rectangle(box(300, 0, 900, 320), fill=C["kadife"])
        d.rounded_rectangle(box(620, 380, 880, 620), radius=int(60 * S), fill=C["ten"])
        d.rectangle(box(640, 450, 700, 475), fill=hx("C8CCD0"))
        return img
    return Plan("B1-S12e", 4, fn)


def plan_s13():
    big = Image.new("RGB", (W, int(H * 1.9)), C["mese"])
    d = ImageDraw.Draw(big)
    hh = 1920 * 1.9
    for k in range(70):
        d.line([p(0, k * 60), p(1080, k * 60 + 180)], fill=hx("7A6B58"), width=max(1, int(2 * S)))
    _koltuk(d, 300, hh - 500, 1.0)
    kneel(d, 560, hh - 330, 0.55, hx("BFC3C6"), hair=AYLA_SAC)
    # koridor kapısı ve karanlık
    d.rectangle(box(280, 0, 800, 900), fill=hx("0C1119"))
    d.rectangle(box(250, 860, 830, 920), fill=hx("D2CCC1"))
    d.rectangle(box(280, 900, 800, 1100), fill=hx("2A3442"))
    big = Image.blend(big, Image.new("RGB", big.size, hx("8A93A0")), 0.12)

    def fn(t, tl):
        return kamera(big, tl / 8, 1.0, 1.05, (0.5, 0.74), (0.5, 0.27))
    return Plan("B1-S13", 8, fn)


def plan_s14():
    yuz = Image.new("RGB", (W, H), hx("8A93A0"))
    d = ImageDraw.Draw(yuz)
    bust(d, 540, 1250, 2.2, C["okr"], head=C["ten"], hair=AYLA_SAC)
    d.ellipse(box(430, 880, 490, 920), fill=hx("2A1A12"))
    d.ellipse(box(590, 880, 650, 920), fill=hx("2A1A12"))
    d.ellipse(box(445, 935, 455, 945), fill=hx("5A3A2A"))  # sol göz altı ben (izleyiciye göre sağda değil: karakterin solu = kadrajın sağı)
    yuz = yuz.filter(ImageFilter.GaussianBlur(18 * S))
    yuz = Image.blend(yuz, Image.new("RGB", yuz.size, (0, 0, 0)), 0.7)

    def fn(t, tl):
        img = yuz.copy()
        if tl >= 0.5:
            d2 = ImageDraw.Draw(img)
            satirlar = [("AYLA NE YAPMALI?", 58, True, 560),
                        ("A — Mert'e söylemeden", 46, False, 760), ("gizli bir kamera kur.", 46, False, 820),
                        ("B — Mert'e her şeyi anlat,", 46, False, 960), ("bu gece birlikte uyanık kalın.", 46, False, 1020)]
            for s, sz, b, y in satirlar:
                f = font(sz, bold=b)
                tw = d2.textlength(s, font=f) / S
                d2.text(p(540 - tw / 2, y), s, font=f, fill=(240, 240, 240))
            f = font(36)
            s = "Yorumlara A ya da B yaz."
            tw = d2.textlength(s, font=f) / S
            d2.text(p(540 - tw / 2, 1400), s, font=f, fill=(190, 190, 190))
        return img
    return Plan("B1-S14", 14, fn)


PLANLAR = [plan_s01, plan_s02, plan_s03, plan_s04a, plan_s04b, plan_s05a, plan_s05b, plan_s06a,
           plan_s06b, plan_s06c, plan_s07a, plan_s07b, plan_s07c, plan_s08a, plan_s08b, plan_s08c,
           plan_s09a, plan_s09b, plan_s10, plan_s11, plan_s12a, plan_s12b, plan_s12c, plan_s12d,
           plan_s12e, plan_s13, plan_s14]


# ---------------------------------------------------------------- altyazı

def srt_oku(path):
    txt = path.read_text(encoding="utf-8").strip()
    out = []
    for blk in re.split(r"\n\s*\n", txt):
        lines = blk.strip().splitlines()
        m = re.match(r"(\d+):(\d+):(\d+),(\d+) --> (\d+):(\d+):(\d+),(\d+)", lines[1])
        g = list(map(int, m.groups()))
        a = g[0] * 3600 + g[1] * 60 + g[2] + g[3] / 1000
        b = g[4] * 3600 + g[5] * 60 + g[6] + g[7] / 1000
        out.append((a, b, "\n".join(lines[2:])))
    return out


# ---------------------------------------------------------------- son işlem

def vinyet():
    y, x = np.ogrid[0:H, 0:W]
    r = np.sqrt(((x - W / 2) / (W / 2)) ** 2 + ((y - H / 2) / (H / 2)) ** 2)
    v = np.clip(1.0 - 0.45 * np.clip(r - 0.55, 0, None) ** 1.4, 0.5, 1.0)
    return v[:, :, None].astype(np.float32)


def taneler(n=6):
    rng = np.random.default_rng(7)
    return [rng.normal(0, 7, (H, W, 1)).astype(np.float32) for _ in range(n)]


# ---------------------------------------------------------------- ses

def db(x):
    return 10 ** (x / 20)


class Ses:
    def __init__(self, dur):
        self.n = int(dur * SR)
        self.buf = np.zeros(self.n, np.float32)
        self.rng = np.random.default_rng(11)

    def ekle(self, t, x, seviye_db):
        i = int(t * SR)
        x = x * db(seviye_db)
        j = min(self.n, i + len(x))
        if i < self.n:
            self.buf[i:j] += x[: j - i]

    def gurultu(self, sure):
        return self.rng.standard_normal(int(sure * SR)).astype(np.float32)

    @staticmethod
    def filtre(x, tip, f, order=4):
        sos = signal.butter(order, f, btype=tip, fs=SR, output="sos")
        return signal.sosfilt(sos, x).astype(np.float32)

    @staticmethod
    def zarf(n, a, r, sustain=None):
        e = np.ones(n, np.float32)
        ai = max(1, int(a * SR))
        ri = max(1, int(r * SR))
        e[:ai] = np.linspace(0, 1, ai)
        if ri < n:
            e[-ri:] *= np.linspace(1, 0, ri)
        return e

    @staticmethod
    def norm(x):
        m = np.max(np.abs(x)) or 1
        return x / m

    def yankili(self, x, gecikme=0.045, geri=0.35, n=5):
        out = np.concatenate([x, np.zeros(int(gecikme * SR * n))]).astype(np.float32)
        for k in range(1, n + 1):
            i = int(gecikme * SR * k)
            out[i:i + len(x)] += x * (geri ** k)
        return out

    # --- sesler
    def tik(self):
        n = int(0.025 * SR)
        x = self.gurultu(0.025) * np.exp(-np.linspace(0, 40, n))
        x = self.filtre(x, "bandpass", [1800, 4500], 2)
        t = np.arange(n) / SR
        x += 0.6 * np.sin(2 * np.pi * 2600 * t) * np.exp(-t * 300)
        return self.norm(self.yankili(x, 0.018, 0.25, 3))

    def fuss(self, sure=2.5):
        n = int(sure * SR)
        g = self.filtre(self.gurultu(sure), "lowpass", 1600)
        env = np.concatenate([np.linspace(0, 1, int(0.15 * SR)), np.exp(-np.linspace(0, 3, n - int(0.15 * SR)))])
        t = np.arange(n) / SR
        hum = (np.sin(2 * np.pi * 62 * t) + 0.5 * np.sin(2 * np.pi * 124 * t) + 0.3 * np.sin(2 * np.pi * 248 * t))
        hum *= np.clip(t / 0.6, 0, 1) * 0.5
        return self.norm(g * env * 1.2 + hum)

    def hum(self, sure):
        n = int(sure * SR)
        t = np.arange(n) / SR
        mod = 1 + 0.12 * np.sin(2 * np.pi * 0.8 * t)
        x = (np.sin(2 * np.pi * 62 * t) + 0.6 * np.sin(2 * np.pi * 124 * t) + 0.35 * np.sin(2 * np.pi * 248 * t)
             + 0.2 * np.sin(2 * np.pi * 372 * t)) * mod
        x += 0.15 * self.filtre(self.gurultu(sure), "lowpass", 400)
        return (self.norm(x) * self.zarf(n, 0.5, 0.5)).astype(np.float32)

    def oda(self, sure, f=500):
        x = self.filtre(self.gurultu(sure), "lowpass", f)
        return self.norm(x) * self.zarf(int(sure * SR), 0.3, 0.3)

    def gicirt(self, sure=1.2):
        n = int(sure * SR)
        t = np.arange(n) / SR
        f = 380 + 120 * np.sin(2 * np.pi * 1.3 * t) + 40 * self.filtre(self.gurultu(sure), "lowpass", 30)
        ph = np.cumsum(2 * np.pi * f / SR)
        x = signal.sawtooth(ph) * (0.6 + 0.4 * (self.rng.random(n) > 0.7))
        x = self.filtre(x.astype(np.float32), "bandpass", [250, 2200], 2)
        return self.norm(x) * self.zarf(n, 0.15, 0.4)

    def sungur(self, sure=1.5, f=900):
        n = int(sure * SR)
        x = self.filtre(self.gurultu(sure), "lowpass", f)
        am = 0.5 + 0.5 * np.abs(np.sin(2 * np.pi * 7 * np.arange(n) / SR))
        return self.norm(x * am) * self.zarf(n, 0.08, 0.3)

    def sinirti(self, n_ses=7, sure=0.7):
        x = np.zeros(int(sure * SR), np.float32)
        for _ in range(n_ses):
            i = self.rng.integers(0, len(x) - int(0.15 * SR))
            m = int(0.15 * SR)
            t = np.arange(m) / SR
            fr = self.rng.uniform(2500, 6000)
            x[i:i + m] += np.sin(2 * np.pi * fr * t) * np.exp(-t * 40)
        return self.norm(x)

    def tok(self, f=80, sure=0.25, klik=0.5):
        n = int(sure * SR)
        t = np.arange(n) / SR
        x = np.sin(2 * np.pi * f * t * (1 - 0.3 * t / sure)) * np.exp(-t * 18)
        c = self.gurultu(sure) * np.exp(-t * 300) * klik
        return self.norm(x + self.filtre(c, "lowpass", 3000))

    def kapi_klik(self):
        return self.norm(np.concatenate([self.tok(110, 0.2, 0.2), self.tik()[: int(0.03 * SR)] * 0.8]))

    def martı(self):
        sure = 0.7
        n = int(sure * SR)
        t = np.arange(n) / SR
        f = 1300 - 500 * t / sure + 60 * np.sin(2 * np.pi * 9 * t)
        x = np.sin(np.cumsum(2 * np.pi * f / SR)) * self.zarf(n, 0.05, 0.3)
        return self.norm(x)

    def matkap(self, sure=1.0):
        n = int(sure * SR)
        t = np.arange(n) / SR
        x = signal.square(2 * np.pi * 190 * t) * 0.4 + 0.3 * self.filtre(self.gurultu(sure), "bandpass", [800, 3000], 2)
        return self.norm(x) * self.zarf(n, 0.05, 0.1)

    def bant(self):
        x = self.filtre(self.gurultu(0.35), "highpass", 1500)
        return self.norm(x) * self.zarf(len(x), 0.01, 0.2)

    def adimlar(self, sayi, aralik=0.5):
        out = np.zeros(int((sayi * aralik + 0.3) * SR), np.float32)
        for k in range(sayi):
            s = self.tok(95, 0.18, 0.4) * 0.8
            i = int(k * aralik * SR)
            out[i:i + len(s)] += s
        return out

    def drone(self, sure, f0=73.42, giris=3.0, cikis=0.05):
        n = int(sure * SR)
        t = np.arange(n) / SR
        vib = 1 + 0.004 * np.sin(2 * np.pi * 4.8 * t)
        ph = np.cumsum(2 * np.pi * f0 * vib / SR)
        x = sum((0.9 ** k) * np.sin(ph * k) / k for k in range(1, 9))
        x += 0.15 * self.filtre(self.gurultu(sure), "bandpass", [100, 600], 2)
        x = self.filtre(x.astype(np.float32), "lowpass", 900)
        return (self.norm(x) * self.zarf(n, giris, cikis)).astype(np.float32)

    def radyo(self, sure):
        n = int(sure * SR)
        x = np.zeros(n, np.float32)
        notlar = [294, 330, 349, 392, 349, 330, 294, 262]
        nl = int(0.45 * SR)
        for k in range(n // nl):
            f = notlar[k % len(notlar)]
            t = np.arange(nl) / SR
            x[k * nl:(k + 1) * nl] = np.sin(2 * np.pi * f * t) * self.zarf(nl, 0.03, 0.2)
        return self.filtre(self.norm(x), "lowpass", 1800)


def ses_olustur(sure):
    s = Ses(sure)
    # zaman kodlu ses planı (05a, bölüm 4.3'ten)
    s.ekle(0.0, s.oda(4.0, 300), -50)
    s.ekle(0.5, s.filtre(s.gurultu(0.3), "bandpass", [2000, 6000]) * s.zarf(int(0.3 * SR), 0.05, 0.2), -46)
    s.ekle(1.0, s.filtre(s.tik(), "lowpass", 6000), -26)
    s.ekle(2.0, s.fuss(2.0), -34)
    s.ekle(3.0, s.hum(5.5), -42)
    s.ekle(4.0, s.oda(4.5, 400), -46)
    s.ekle(6.5, s.gicirt(1.1), -32)
    # 8.5–9.0 sessizlik
    s.ekle(9.0, s.oda(8.0, 1200), -36)
    s.ekle(9.5, s.martı(), -30)
    s.ekle(10.0, s.bant(), -34)
    s.ekle(11.0, s.adimlar(6, 0.55), -32)
    s.ekle(17.0, s.oda(9.0, 700), -44)
    s.ekle(18.0, s.sinirti(9, 0.7), -24)
    tes = np.zeros(int(5 * SR), np.float32)
    for k in range(25):
        c = s.tok(1400, 0.05, 0.9) * 0.7
        i = int(k * 0.2 * SR)
        tes[i:i + len(c)] += c
    s.ekle(21.0, tes, -36)
    s.ekle(26.0, s.filtre(s.gurultu(0.6), "bandpass", [1500, 5000], 2) * s.zarf(int(0.6 * SR), 0.1, 0.3), -40)
    s.ekle(26.5, s.radyo(8.0), -46)
    s.ekle(33.5, s.tok(70, 0.4, 0.3), -28)
    s.ekle(34.6, s.kapi_klik(), -26)
    s.ekle(35.0, s.oda(7.0, 900), -42)
    s.ekle(35.5, s.sungur(0.8, 500), -32)
    s.ekle(39.5, s.matkap(1.0), -36)
    s.ekle(42.0, s.hum(13.0) * 0.6, -50)
    s.ekle(42.5, s.filtre(s.gurultu(0.8), "lowpass", 3000) * s.zarf(int(0.8 * SR), 0.1, 0.3), -40)
    s.ekle(53.0, s.sungur(0.4, 2500), -30)
    s.ekle(54.5, s.sungur(1.0, 600), -34)
    s.ekle(55.0, s.oda(11.0, 500), -46)
    s.ekle(56.0, s.adimlar(4, 0.45), -32)
    s.ekle(59.5, s.tok(75, 0.4, 0.3), -26)
    s.ekle(59.9, s.kapi_klik(), -28)
    s.ekle(60.5, s.adimlar(5, 0.4) * np.linspace(1, 0.1, len(s.adimlar(5, 0.4))), -38)
    s.ekle(66.0, s.oda(11.0, 900), -44)
    s.ekle(66.0, s.drone(19.0, giris=3.0, cikis=0.02), -34)
    s.ekle(70.0, s.sungur(0.8, 3000), -34)
    s.ekle(77.0, s.oda(9.0, 600), -44)
    saat = np.zeros(int(8 * SR), np.float32)
    for k in range(8):
        c = s.tok(2000, 0.04, 1.0)
        saat[int(k * SR):int(k * SR) + len(c)] += c
    s.ekle(77.0, saat, -40)
    for k, tt in enumerate((78.0, 80.0, 82.5)):
        s.ekle(tt, s.bant(), -30)
    s.ekle(85.0, s.tik()[: int(0.02 * SR)], -28)
    s.ekle(86.0, s.oda(5.0, 250), -54)
    s.ekle(87.0, s.tik(), -18)
    s.ekle(88.0, s.fuss(2.5), -26)
    s.ekle(89.0, s.hum(2.0), -40)
    s.ekle(89.5, s.sungur(1.5, 450), -28)
    # 91–93 mutlak sessizlik
    s.ekle(93.0, s.oda(15.0, 900), -44)
    s.ekle(94.0, s.sinirti(4, 0.5), -40)
    s.ekle(108.5, s.tok(70, 0.3, 0.4), -16)
    s.ekle(109.5, s.drone(6.8, f0=73.42, giris=1.5, cikis=0.02), -26)
    s.ekle(114.0, s.tik()[: int(0.02 * SR)], -42)
    s.ekle(115.0, s.hum(1.5), -42)
    s.ekle(118.0, s.hum(14.0), -40)
    s.ekle(131.5, s.tik(), -24)
    x = s.buf
    pk = np.max(np.abs(x))
    if pk > 0.89:
        x = x * (0.89 / pk)
    return x


def wav_yaz(path, x):
    st = np.stack([x, x], axis=1)
    pcm = (np.clip(st, -1, 1) * 32767).astype(np.int16)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())


# ---------------------------------------------------------------- ana

def main():
    CIKTI.mkdir(exist_ok=True)
    planlar = [f() for f in PLANLAR]
    toplam = sum(pl.sure for pl in planlar)
    assert abs(toplam - 132) < 1e-6, toplam
    alt = srt_oku(KOK / "uretim" / "altyazi" / "b1.srt")
    vin = vinyet()
    tane = taneler()
    wav = CIKTI / "b1-animatik-ses.wav"
    wav_yaz(wav, ses_olustur(toplam))
    hedef = CIKTI / ("b1-animatik-onizleme.mp4" if ONIZLEME else "b1-animatik.mp4")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
           "-r", str(FPS), "-i", "-", "-i", str(wav), "-c:v", "libx264", "-preset", "medium", "-crf", "26", "-maxrate", "4M", "-bufsize", "8M",
           "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(hedef)]
    ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    kare = 0
    t0 = 0.0
    for pl in planlar:
        n = int(round(pl.sure * FPS))
        for i in range(n):
            tl = i / FPS
            t = t0 + tl
            img = pl.fn(t, tl)
            if img.size != (W, H):
                img = img.resize((W, H))
            for a, b, m in alt:
                if a <= t < b:
                    img = altyazi(img, m)
            img = etiket(img, "ANİMATİK · TASLAK", 760, 70, 22, (150, 150, 150))
            arr = np.asarray(img, np.float32) * vin + tane[kare % len(tane)]
            ff.stdin.write(np.clip(arr, 0, 255).astype(np.uint8).tobytes())
            kare += 1
        t0 += pl.sure
        print(f"  {pl.pid:10s} {pl.sure:5.1f} sn  (t={t0:6.1f})", flush=True)
    ff.stdin.close()
    ff.wait()
    # Seslendirme olmadığı için ses tasarımı göreli seviyelerde kaldı. Telefonda duyulabilir olsun diye
    # bütün miks -20 LUFS'e normalize edilir (nihai miks hedefi seslendirmeyle -14 LUFS).
    gecici = hedef.with_suffix(".tmp.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(hedef), "-c:v", "copy",
                    "-af", "loudnorm=I=-20:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "192k",
                    "-movflags", "+faststart", str(gecici)], check=True)
    gecici.replace(hedef)
    print(f"{kare} kare -> {hedef.relative_to(KOK)}")


if __name__ == "__main__":
    main()
