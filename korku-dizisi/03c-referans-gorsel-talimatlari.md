# AŞAMA 3-C — KARAKTER VE MEKÂN REFERANS GÖRSELİ ÜRETİM TALİMATLARI (Dosya E)

**Dizi:** YEDEK ANAHTAR

**Amaç:** Bütün sahne görselleri üretilmeden önce her karakter ve kritik mekân için **onaylı referans sayfaları** hazırlamak. Sonraki bütün görseller bu referanslara bağlanarak üretilecek. Referans onaylanmadan sahne üretimine geçilmez.

---

## 1. ÜRETİM SIRASI (zorunlu)

1. **Stil çerçevesi:** Tek bir "stil test karesi" üretilir: L03 koridor, T-GECE-0310 ışığında, karakter yok. Çizgi kalınlığı, gölgeleme, renk ve doku bu karede onaylanır. Bu kare **STİL-REF-01** olur. Sonraki her üretimde stil referansı olarak kullanılır.
2. **Karakter ana referansı:** Her karakter için, nötr ifadeli tek bir yüz portresi ve tam boy önden görünüş. Onaylanan kare **[KARAKTER]-REF-01** olur.
3. **Karakter sayfaları:** Dönüş (turnaround), ifadeler, kıyafetler, eller ve aksesuarlar. Hepsi REF-01'e bağlı üretilir.
4. **Karakter yan yana boy karşılaştırması** (line-up).
5. **Mekân referansları:** Her mekân için bir geniş plan "master" kare ve bir de ters açı kare.
6. **Prop (eşya) sayfası.**
7. **Onay ve kilitleme:** Onaylanan her görselin dosya adı, kullanılan seed değeri ve promptu `referans-kayit` tablosuna (bölüm 7) işlenir.

---

## 2. TUTARLILIK TEKNİĞİ (hangi araç kullanılırsa kullanılsın)

| Yöntem | Uygulama |
|--------|----------|
| **Karakter referansı / image prompt** | Her sahne promptuna o karakterin REF-01 görseli karakter referansı olarak eklenir (Midjourney `--cref`/`--oref`, benzeri araçlarda "character reference" / "subject reference", Flux/SD'de IP-Adapter). |
| **Stil referansı** | Her promptta STİL-REF-01 stil referansı olarak eklenir (`--sref` veya muadili). |
| **Sabit seed** | Referans sayfaları için seed kaydedilir. Aynı karakterin farklı pozlarında aynı seed denenir. |
| **LoRA (önerilir)** | Uzun üretim için her ana karakterin onaylı referans setinden (15–25 görsel: dönüş, ifade, kıyafet) bir karakter LoRA'sı eğitilir. Tetikleyici kelimeler: `aylaDMR`, `mertDMR`, `kenanSRI`, `saadetUNL`, `hikmetAKS`. |
| **Blokları değiştirmeme** | CHARACTER BLOCK ve OUTFIT BLOCK kelimesi kelimesine kopyalanır. |
| **Tek karede en fazla 2 karakter** | Mümkünse aynı karede ikiden fazla konuşan karakter üretilmez. Üç kişilik sahneler katman (compositing) ile birleştirilir. |
| **Eller** | Kenan'ın elleri her zaman ayrı bir "el referansı" görseliyle kontrol edilir. Gerekirse inpainting ile düzeltilir. |
| **Kontrol (opsiyonel)** | Kamera açısı ve poz için ControlNet (OpenPose / depth) ya da kaba bir 3D blokaj kullanılır. Mekân geometrisi için L03 ve L09'un kaba 3D maketi önerilir. |

---

## 3. KARAKTER REFERANS SAYFASI ŞABLONU

Her karakter için **5 sayfa** üretilir. Sayfalar yatay (16:9) model-sheet formatındadır. Bu sayfalar yalnızca iç kullanım içindir.

### Sayfa 1 — TURNAROUND (dönüş)
```
[GLOBAL STYLE BLOCK — but replace "vertical 9:16 composition" with "horizontal character model sheet, plain light grey background, even neutral studio lighting, no shadows on background"]
character turnaround reference sheet of [CHARACTER BLOCK], wearing [MAIN OUTFIT BLOCK],
five full-body views in a row at the same scale: front view, three-quarter front view, side profile view (facing left), three-quarter back view, back view,
neutral standing pose, arms relaxed at the sides, neutral expression, consistent proportions and clothing across all views,
thin horizontal guide lines at head, shoulder, waist and knee height, clean linework, flat neutral colors with light cel shading
[GLOBAL NEGATIVE]
```

### Sayfa 2 — İFADELER (8 kare, omuz çekimi)
```
facial expression reference sheet of [CHARACTER BLOCK], head and shoulders only, same angle (three-quarter front) in all panels,
eight panels in a 4x2 grid: [EXPRESSION LIST], consistent face structure and features in every panel, plain light grey background, neutral lighting
```

| Karakter | İfade listesi (8) |
|----------|-------------------|
| **Ayla** | nötr · sessiz dikkat (bir şeyi fark ediyor) · şüphe (kaşlar çatık, dudak ısırma) · korku (gözler açık, nefes tutulmuş) · bastırılmış ağlama · kararlılık · bitkinlik/baş ağrısı (alnını tutuyor) · panik (B6) |
| **Mert** | nötr · zoraki gülümseme · savunmacı öfke · utanç (göz kaçırma) · küçümseyen şüphe · korku · uykulu sersemlik (CO) · bilinç kaybı (gözler kapalı, yüz gevşek) |
| **Kenan** | nötr/boş bakış · bir şeyi dinlerken donmuş · şefkatli özen (eşya düzeltirken) · bulanık şaşkınlık · korkmuş hayvan bakışı · fısıltıyla "Nurten?" (dudaklar aralık) · kısa bir berraklık anı · bilinç kaybı |
| **Saadet** | nötr sertlik · kapı aralığından gözlem · hüzünlü anı · gizlenen korku · suçluluk · koruyucu sertlik ("Girme.") · yorgunluk · sessiz ağlama |
| **Hikmet** | kibar sahte gülümseme · göz kaçırma · gizlenen panik · soğuk öfke · yalan söylerken rahat görünme · tavana kaçamak bakış · tespih çekerken gerginlik · yakalanmış korku |

### Sayfa 3 — KIYAFETLER
```
outfit reference sheet of [CHARACTER BLOCK], full body front view, [N] versions side by side in identical pose and scale:
(1) [OUTFIT A], (2) [OUTFIT B], (3) [OUTFIT C] ..., each labeled with a small code tag, plain light grey background
```
- Ayla: A-EV · A-GECE · A-DIŞ · A-EPİLOG
- Mert: M-İŞ · M-EV · M-GECE · M-EPİLOG
- Kenan: K-ANA · K-ESKİ (42 yaş) · K-HASTANE
- Saadet: S-EV · S-GECE · S-DIŞ
- Hikmet: H-ANA · H-DIŞ

### Sayfa 4 — ELLER VE AKSESUARLAR (yakın çekim)
```
hands and accessories close-up reference sheet of [CHARACTER BLOCK], six panels: [LIST], highly accurate anatomy, exactly five digits per hand unless specified
```
| Karakter | Paneller |
|----------|----------|
| Ayla | sağ el, gümüş yüzük ve mürekkep lekeleriyle · sol el, alyansla · kurşun kalem tutarken · eskiz defteri, kapalı ve açık · yuvarlak gözlük · kupayı tutarken |
| Mert | sol bilek, saat ve alyansla · telefonu tutarken · sağ kaş yara izi, yakın çekim · ensesini ovuştururken · yumruk · çekiç tutarken (B6) |
| **Kenan** | **sol el, üstten (işaret parmağının üst boğumu yok, yuvarlak eski yara izi)** · **sol el, avuç içi** · **sol el, kameraya uzanırken (B2-A karesi)** · sağ el, yağlı çizgilerle · boynundaki ipli anahtar · gri atkı, açılmış hâlde, kırmızı şerit ve örgü dokusuyla |
| Saadet | ellerindeki lekeler ve yüksük nasırı · altın bilezik · zincirli gözlük · mezura · örtülü tabağı tutarken · kapı zincirini tutarken |
| Hikmet | sağ el, kehribar tespihle · sol serçe parmak mühür yüzükle · araba anahtarı · asma kilidi takarken (B5-A) |

> **KENAN EL KURALI:** Sol işaret parmağı **ilk eklemden (distal falanks) kesik**, uç yuvarlanmış ve kapanmış. Tırnak yok. Diğer dört parmak tam. Bu kural her karede kontrol edilir. Yanlış üretilen kareler inpainting ile düzeltilmeden kullanılmaz.

### Sayfa 5 — HAREKET VE DURUŞ
```
pose and body language reference sheet of [CHARACTER BLOCK] wearing [MAIN OUTFIT], six full-body poses: [LIST], consistent proportions
```
| Karakter | Pozlar |
|----------|--------|
| Ayla | yürürken (dikkatli) · çömelip yerdeki izlere bakarken · masada çizerken · kapı deliğinden bakarken · Mert'i sürüklerken (B6/F1) · yerde dizlerinin üstünde |
| Mert | işe gidiyormuş gibi kapıdan çıkarken · kanepede telefona bakarken · kapaktan yukarı tırmanırken · kollarını kavuşturmuş tartışırken · kanepede baygın · arabada ön koltukta |
| Kenan | kambur, sessiz yürürken · kapaktan inerken (bacakları önce) · koltuğu eski yerine çekerken · termostatı çevirirken · duvara yaslanıp yere kayarken · depoda emeklerken |
| Saadet | kapı aralığından bakarken (zincir takılı) · tabakla merdiven çıkarken · çay koyarken · Ayla'yı kolundan tutarken (F1) |
| Hikmet | anahtar uzatırken · arabada otururken (gözetleme) · koridorda tavana bakarken · polisle konuşurken |

---

## 4. LINE-UP (boy karşılaştırması)
```
character height line-up reference, plain light grey background with horizontal height lines every 10 cm from 150 to 190 cm,
five characters standing side by side in their main outfits, front view, neutral pose, same scale:
SAADET (155 cm), AYLA (166 cm), HIKMET (172 cm), KENAN (176 cm but stooped, appears 170 cm), MERT (181 cm),
[each CHARACTER BLOCK in short form]
```
> **Kontrol:** Kenan kamburluğu yüzünden Hikmet'le neredeyse aynı boyda görünür. Mert her zaman en uzun, Saadet en kısa olandır.

---

## 5. MEKÂN REFERANS SAYFALARI

Her kritik mekân için şu görseller üretilir:

| Mekân | Görseller |
|-------|-----------|
| **L03 Koridor** | (1) Girişten doğuya bakış · (2) Doğu uçtan girişe (batıya) bakış · (3) Kapağın tam altından yukarı bakış · (4) Kapak açık, aşağıdan · (5) Termostatın yakın çekimi · (6) Kombi dolabı açık, turuncu alev |
| **L04 Oturma odası** | (1) Kapıdan pencerelere (kuzey) · (2) Pencerelerden kitaplığa (batı) · (3) Parkedeki 4 izin üstten görünüşü, koltuksuz ve koltuklu |
| **L06 Yatak odası** | (1) Kapıdan yatağa · (2) Yatağın yanından kapıya (koridorun karanlığı) |
| **L07 Banyo** | (1) Kapıdan lavabo ve ayna · (2) Diş fırçası bardağı, 2 fırçalı ve 3 fırçalı |
| **L09 Depo** | (1) Kapaktan yukarı başını uzatan birinin bakış açısı (fener) · (2) Nurten köşesi · (3) Baca borusu eklemi · (4) Panel ve metal kutu |
| **L02 Sahanlık** | (1) Daire 7 kapısından Daire 8 kapısına · (2) Yarım kat yukarıdaki çatı kapısı, kilitsiz ve asma kilitli |
| **L01 Sokak** | (1) Arabanın içinden binaya · (2) Binanın önünden geniş plan, gece · (3) Gündüz |
| **L11 Bodrum** | (1) Koridor · (2) Kömürlük 7'nin içi |
| **L12 Saadet** | (1) Oturma odası geniş plan · (2) F-1 fotoğrafının duvardaki yeri |

**Mekân kuralları:**
- Her mekân için **"master geniş plan"** onaylanır. Sonraki bütün sahnelerde arka planlar bu planın kırpımı ya da açı varyasyonu olur.
- **L03 ve L09** için kaba bir 3D maket (Blender ya da SketchUp, 1:1 ölçü) hazırlanması önerilir. Kamera açıları maketten alınıp depth/line referansı olarak kullanılır. Böylece kapak, ayakkabılık, termostat ve kapıların yeri hiçbir karede değişmez.

---

## 6. PROP (EŞYA) REFERANS SAYFASI

```
prop reference sheet, plain light grey background, each object drawn in the series' cinematic 2D style with consistent lighting, labeled with code tags
```
| Kod | Eşya | Tanım |
|-----|------|-------|
| P-01 | Anahtar halkası | `a simple steel key ring with three keys: a long silver building door key, a modern silver cylinder apartment key, and an old worn brass key stamped with tiny letters "SARI ANAHTAR"` |
| P-02 | Ayla'nın kupası | `cream ceramic mug with a thin navy blue rim and a hairline crack on the handle` |
| P-03 | Termostat + uygulama ekranı | `square white digital wall thermostat with a blue-white backlit display showing "23°C"` + phone UI: `minimal dark-mode thermostat app log list, entries "03:10 · Manuel ayar · 22°C → 23°C"` |
| P-04 | Eskiz defteri | `black A5 hardcover sketchbook with an elastic band, pages of precise pencil drawings of an apartment interior` |
| P-05 | Wi-Fi kamera | `small white round consumer Wi-Fi security camera with a tiny blue status light` |
| P-06 | Diş fırçası bardağı | `clear glass toothbrush cup with two new toothbrushes (one teal, one white) and one old worn toothbrush with splayed faded red bristles` |
| P-07 | Metal kutu | `dented green-painted metal box 40x25x20 cm with a small padlock and a faded yellow "SARI ANAHTAR" sticker` |
| P-08 | Gri atkı | `long hand-knitted grey wool scarf with one single dark red stripe near one end, slightly pilled` |
| P-09 | Hikmet'in notu | `a small torn piece of lined paper taped to a door, handwritten in blue ballpoint: "Kilit değişti. Eşyaların bodrumda. — H.A."` |
| P-10 | Kenan'ın notu | `a scrap of brown paper with shaky pencil handwriting: "Nurten üşür. Kaloriferi kısmayın."` |
| P-11 | Kopya anahtar | `a single freshly cut shiny silver key, sharp new edges, lying on a light oak surface` |
| P-12 | Saadet'in tabağı | `a white plate covered with a white cloth embroidered with small blue flowers` |
| P-13 | Asma kilit | `a new heavy brass padlock on a grey metal attic door latch` |
| P-14 | Ayla'nın notu | `a sheet torn from a sketchbook with neat handwriting: "Kenan Bey. Sizi biliyoruz. Konuşmak istiyoruz."` |
| P-15 | 214 anahtar | `an open green metal box filled with hundreds of old keys, each tied with a small paper tag handwritten with an address` |
| P-16 | Saadet'in zarfı | `a small yellowed envelope and an old brass key with a faded red thread tied to it` |
| P-17 | Fotoğraflar F-1 – F-4 | bkz. 03a, bölüm 7 |
| P-18 | Morfin kutuları | `empty white pharmaceutical boxes with simple generic labels and no real brand names, neatly stacked in a pyramid` |

> **Telefon arayüzü kuralı:** Bütün telefon ekranlarında (WhatsApp benzeri mesajlar, termostat uygulaması, arama sonuçları) gerçek marka logoları kullanılmaz. Sade, kurgusal ve okunaklı bir arayüz tasarlanır, bütün dizi boyunca aynı kalır. Ekran metinleri görsel üretim aracıyla değil, **montajda grafik olarak** eklenir. Yapay zekânın yazı hatalarını önlemenin yolu bu.

---

## 7. REFERANS KAYIT TABLOSU (doldurulacak)

| Ref kodu | Açıklama | Araç / model | Seed | Dosya adı | Onay tarihi | Not |
|----------|----------|--------------|------|-----------|-------------|-----|
| STİL-REF-01 | Koridor stil karesi | | | | | |
| AYLA-REF-01 | Ayla portre + önden | | | | | |
| MERT-REF-01 | | | | | | |
| KENAN-REF-01 | | | | | | |
| KENAN-EL-01 | Sol el, kesik parmak | | | | | |
| SAADET-REF-01 | | | | | | |
| HIKMET-REF-01 | | | | | | |
| L03-MASTER | | | | | | |
| L09-MASTER | | | | | | |
| … | | | | | | |

---

## 8. REFERANS ONAY KONTROL LİSTESİ

Her referans görsel için:
- [ ] Yüz yapısı CHARACTER BLOCK ile birebir uyuşuyor mu (ben, yara izi, bıyık, sakal)?
- [ ] Göz rengi ve saç doğru mu?
- [ ] Boy oranı line-up'la tutarlı mı?
- [ ] İmza rengi doğru tonda mı?
- [ ] Eller anatomik olarak doğru mu? Kenan'ın sol işaret parmağı doğru mu?
- [ ] Aksesuarlar doğru elde mi (Ayla: gümüş yüzük **sağ** işaret parmağında, Hikmet: tespih **sağ** elde, mühür yüzük **sol** serçe parmakta)?
- [ ] Stil STİL-REF-01 ile aynı mı? Anime, 3D ya da çocuk estetiği sızmış mı?
- [ ] Mekânda kapı, pencere ve nesne konumları kat planıyla aynı mı?
- [ ] Görselde yapay zekâ hatası var mı (bozuk metin, kaynaşmış nesneler, anlamsız detaylar)?
