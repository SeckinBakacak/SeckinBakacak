# 112 — Etkileşimli Korku Dizisi

> Gece üçte gelen bir çağrı. Arayan yedi yaşında bir kız.
> Verdiği adres, otuz yıl önce yanıp kül olmuş bir ev.

**İlham:** *The Guilty*, *Black Phone* (tek mekân, telefon başında büyüyen gerilim)
**Varlık:** Tanıdık seslerle insanı çağıran cin. Folklordaki "gece adınla çağrılırsan dönüp bakma" inancı. Asla görünmez, sadece duyulur.
**Ton:** Gerçek bir çağrı kaydı dosyası izleniyormuş gibi: arayüzler, ses dalgaları, telsiz kayıtları, saat damgaları.

## Karakterler (4)

| Karakter | Kim | Görünüş (çizim tarifi) |
|---|---|---|
| **Selin** | 28, çağrı operatörü, 3 aydır gece vardiyasında | omuz hizası kahverengi saç, kulaklık-mikrofon seti, lacivert 112 polarlı |
| **Hakan** | 56, vardiya amiri, 30 yıldır bu masada | kır saç, kalın kır bıyık, gözlük, gri hırka, elinde hep çay |
| **Rıza** | 45, ambulans şoförü | kısa siyah saç, sakal, reflektörlü kırmızı-lacivert ambulans montu |
| **Nur** | 7, arayan kız | **asla gösterilmez**, sadece ses dalgası olarak var |

## Mekânlar

1. **Çağrı merkezi dış:** karlı gece, tek katlı beton bina, tabelada "112 ACİL ÇAĞRI MERKEZİ · KARAAĞAÇ", kapıda tek ambulans, turuncu sokak lambası
2. **Çağrı merkezi iç:** iki masa, her masada 3 monitör, duvar saati, Türk bayrağı, pencereden kar
3. **Çağrı ekranı (arayüz):** "GELEN ÇAĞRI", numara, süre sayacı, form alanları, ses dalgası
4. **Harita ekranı:** köy yolları, dere, kırmızı konum noktası
5. **Köy yolu:** gece, kar, çıplak ağaçlar, ambulans farları ve mavi-kırmızı tepe lambası
6. **Yanık ev:** çatısız, kömürleşmiş taş duvarlar, karla örtülü, kapı boşluğu

## Görsel ve ses dili

- **Geçişler:** ses dalgası düz çizgiye inerek kesme · telsiz cızırtısıyla kesme · beyaz gürültü (glitch) · siyaha kararma · ambulans ışığı flaşı
- **Diyalog kutuları:** konuşanın adı ve kaynağı yazar: `HAT 1 · NUR`, `TELSİZ · RIZA`, `HAKAN`
- **Damga:** sağ altta `◷ KARAAĞAÇ 112 · 03:00:12`
- **Ses:** anlatıcı Brian (v4). Karakter replikleri ayrı seslerle okunur, telefon/telsiz efektiyle (bant daraltma, cızırtı)

## Sezon taslağı

| # | Başlık | Ne oluyor |
|---|---|---|
| 1 | İlk Çağrı | Nur arıyor, adres yanık ev. İkinci çağrıda arkadan Rıza'nın sesi geliyor. Oysa Rıza Selin'in yanında. |
| 2 | (seçime göre) | Kayıt dinlenir ya da Nur'la konuşma sürer. Kayıtta Nur'un arkasında bir üçüncü ses var. |
| 3 | 1994 | Hakan'ın sırrı: o gece çağrıyı alan oydu ve "şaka" sanıp ekip göndermedi. |
| 4 | Adınla Çağırır | Ses artık merkezdeki herkesin sesini taklit ediyor. Kim gerçekten konuşuyor? |
| 5 | Son Çağrı | Selin kendi sesinin aradığını duyuyor: "112 Acil, dinliyorum." |

## Üretim (`uretim/`)

```
cd 112/uretim && ./uret.sh bolum01
```

- `bolumXX.json`: sahneler. `lines` içinde `[konuşan, metin]` çiftleri; `*kelime*` kırmızı altyazı, `[whispers]` fısıltı. `sesler` bölümünde her karakterin ElevenLabs sesi ve efekti (`phone` telefon hattı, `radio` telsiz)
- `ses.py`: çok sesli seslendirme, telefon/telsiz filtreleri, telsiz cızırtısı, zil, kapanma sesi, ortam sesleri (rüzgâr, ofis, motor), dalga formu verisi
- `sahne.html`: tüm çizimler ve arayüzler; `render.mjs`: 1080x1920 MP4
