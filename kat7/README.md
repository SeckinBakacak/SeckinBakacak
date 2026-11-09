# KAT 7 — Etkileşimli Korku Dizisi

> Altı katlı bir apartmanın asansöründe yedinci bir düğme var.
> Üstü bantla kapatılmış. Ve her gece 03:17'de biri o banta dokunuyor.

## Format (her bölüm)

| Bölüm | Süre | İçerik |
|---|---|---|
| Kanca | 0–3 sn | Bölümün en ürkütücü karesi + tek cümle |
| Önceki bölümde | 3–12 sn | Geçen bölümün son 2-3 karesi, "◂◂ ÖNCEKİ BÖLÜMDE" bandı |
| Siz seçtiniz | 12–16 sn | İki seçenek kartı, kazanan parlıyor, "ÇOĞUNLUK DEDİ" |
| Hikâye | 16–110 sn | "Sen" diliyle anlatım, 12–20 sahne |
| Cliffhanger | 110–120 sn | Kırmızı yazı, sert kesme, ekran kararıyor |
| Seçim ekranı | 120–130 sn | "SEN OLSAN NE YAPARDIN?" + 2 kart + 5-3-1 sayaç + "YORUMA YAZ ↓" |

## Görsel kurallar

- **Oran:** 9:16, 1080x1920
- **Stil:** düz 2D vektör, kalın koyu kontur, yüzler basit (nokta göz), arka plan koyu lacivert / kahverengi, hafif film greni
- **Altyazı:** ekranın alt üçte birinde, kalın büyük harf, beyaz; anlatılan kelime **sarı** yanar, kritik kelime **kırmızı**
- **Diyalog kutusu:** üstte siyah kutu, solda renkli çizgi, üstünde konuşan: `KAMERA · 03:17`, `ELİF`, `REMZİ'NİN NOTU`
- **Zaman damgası:** sağ alt köşe, monospace: `◷ KAT 7 · GECE 03:17`
- **Tekrar eden motif:** güvenlik monitörü (yeşilimsi, tarama çizgili) — her bölümde bir kayıt izlenir
- **Ses:** tek anlatıcı (fısıltıya yakın, sakin erkek/kadın sesi), alçak drone müzik, her sahne geçişinde "tık", asansör "dıt" sesi

## Karakterler (AI görsel promptlarında sabit tut)

| Karakter | Görünüş (prompt tarifi) |
|---|---|
| **Sen** — yeni gece bekçisi | hiç yüzü gösterilmez; lacivert bekçi montu, el feneri, sırttan |
| **Remzi Efendi** — eski bekçi, kayıp | 60'larında, gri bıyık, kasket, kahverengi yelek |
| **Nermin Hanım** — yönetici, 5. kat | beyaz topuz, mor hırka, yuvarlak gözlük |
| **7. kattaki** | asla net gösterilmez; asansör camında yalnızca siluet |

## Stil promptu (her görsele ekle)

```
flat 2D vector illustration, thick dark outlines, simple shapes, minimal faces with dot eyes,
dark muted palette (navy, brown, desaturated yellow), subtle film grain, eerie atmosphere,
vertical 9:16, no text
```

## Sezon haritası

| # | Başlık | Seçim |
|---|---|---|
| 1 | İki Kural | Asansörü aç / 5. kata koş |
| 2 | (seçime göre) | — |
| 3 | Nermin Hanım'ın kapısı | — |
| 4 | Remzi'nin defteri | — |
| 5 | Yedinci kat | — |

Her bölüm yorumlardaki çoğunluğa göre yazılır.

## Otomatik üretim (`uretim/`)

Yeni bölüm için `uretim/bolum01.json` dosyasını kopyala (`bolum02.json`), sahneleri yaz ve çalıştır:

```
cd kat7/uretim && ./uret.sh bolum02
```

- `bolumXX.json`: sahneler (`v` görsel, `say` seslendirme, `*kelime*` kırmızı altyazı, `head` üst başlık, `box` diyalog kutusu, `stamp` zaman damgası, `sfx` efekt) ve seçim kartları
- `ses.py`: ElevenLabs seslendirmesi (Brian, eleven_v4, Türkçe), kelime zamanlamaları, müzik ve efekt miksajı. Ses dosyaları `cache/` klasöründe tutulur, aynı metin için tekrar kredi harcanmaz
- `sahne.html`: tüm çizimler (SVG) ve altyazı/diyalog katmanları
- `render.mjs`: kareleri çizip ffmpeg ile 1080x1920 MP4 çıkarır
