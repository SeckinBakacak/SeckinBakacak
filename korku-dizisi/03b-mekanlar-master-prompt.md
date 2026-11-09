# AŞAMA 3-B — MEKÂNLAR VE MASTER LOCATION PROMPT (Dosya D)

**Dizi:** YEDEK ANAHTAR

**Kullanım:** Görsel promptu şu sırayla birleştirilir:

```
[GLOBAL STYLE BLOCK] + [LOCATION BLOCK] + [TIME-OF-DAY BLOCK] + [karakterler] + [sahne] + [GLOBAL NEGATIVE]
```

GLOBAL STYLE ve NEGATIVE blokları için bkz. `03a-karakterler-master-prompt.md`. Ölçüler metre cinsinden.

---

## 0. YÖN VE KOORDİNAT SİSTEMİ (bütün dizi için sabit)

- **Kuzey = Ihlamur Sokak.** Binanın ön cephesi sokağa bakar.
- **Güney = arka avlu ve ışıklık.**
- Daire 7 binanın **doğu yarısında**. **Sokaktan binaya bakan biri için Daire 7 en üst katın SOL yarısıdır.**
- Daire içi koordinatlar: x = batıdan doğuya (0 → 10,0), y = güneyden kuzeye (0 → 8,5).
- **Sabit kural:** Daire 7'ye girince koridor **doğuya** doğru uzanır. Banyo ve kombi dolabı **sağda** (güney), ayakkabılık, termostat ve oturma odası kapısı **solda** (kuzey) kalır.

---

## 1. BİNA KESİTİ VE BAĞLANTILAR

```
                  ÇATI (kırma çatı, kiremit)
        ┌────────────────────────────────────────────┐
        │              ÇATI ARASI (L10)               │ ← su deposu, kirişler, toz
        │   [metal çatı kapısı]◄── yarım kat merdiven  │
3. KAT  │  DAİRE 8 (Saadet)  │SAHANLIK│  DAİRE 7 (L03–L09) │ ← en üst kat
        │                    │ (L02)  │ [asma tavan depo L09] │
2. KAT  │  Daire 6           │        │  Daire 5           │
1. KAT  │  Daire 4           │MERDİVEN│  Daire 3           │
ZEMİN   │  Daire 2           │        │  Daire 1           │
        │           [bina giriş kapısı — kuzey]            │
BODRUM  │  KÖMÜRLÜKLER 1–8 (L11)  ·  sayaçlar  ·  çamaşırlık│
        └────────────────────────────────────────────┘
        ↑ KUZEY: IHLAMUR SOKAK (L01)
```

**Gizli bağlantı (hikâyenin anahtarı):**
`Daire 7 koridor tavanı (kapak) → Asma tavan depo (L09) → depo batı duvarındaki sökülebilir panel → Çatı arası (L10) → metal çatı kapısı → 3. kat sahanlığın yarım kat üstü (L02)`

Kenan bu yolla daireye uğramadan binaya girip çıkabiliyor. Saadet'in tabağı metal çatı kapısının önüne bırakılıyor.

---

## 2. DAİRE 7 — KAT PLANI (en kritik harita)

```
                           KUZEY — IHLAMUR SOKAK (cephe)
 x=0.0                                   x=5.6                              x=10.0
y=8.5 ┌──────[P1]──────────────[P2]───────┬────────────[P3]───────────────────┐
      │                                    │                                   │
      │  OTURMA ODASI (L04)                │  YATAK ODASI (L06)                │
      │  5.6 × 4.9 m                       │  4.4 × 4.9 m                      │
      │                                    │                                   │
      │  [KOLTUK — parkedeki 4 iz]         │  [ÇİFT KİŞİLİK YATAK, başı DOĞU]  │
      │  [kanepe]  [kitaplık: BATI duvarı] │  [gardırop: BATI duvarı]          │
      │                                    │                                   │
y=3.6 ├──────────[AYK]──[T]──[K-O]─────────┴──[K-Y]───────┬────────────────────┤
      │      ┌─────────────┐                              │                    │
 GİRİŞ═[KAPI]│ ▣ KAPAK     │   KORİDOR (L03) 7.0 × 1.2 m  [K-Ç] ÇALIŞMA ODASI  │
 (L02)│      └─────────────┘                              │  (L08) 3.0 × 3.6   │
y=2.4 ├─[KOMBİ]──┬──[K-B]──┬──────────[K-M]───────────────┤                    │
      │  dolap   │ BANYO   │   MUTFAK (L05) 3.6 × 2.4 m   │  [Ayla'nın masası] │
      │  1.0×0.8 │ (L07)   │                              │                    │
      │          │ 2.4×2.4 │                              │                    │
y=0.0 └──────────┴─────────┴──────────[P4]────────────────┴───────[P5]─────────┘
       ◄──── ASMA TAVAN DEPO (L09) x=0–3.4, y=0–3.6 ────►
                           GÜNEY — ARKA AVLU / IŞIKLIK
```

**Lejant ve kesin konumlar:**

| Kod | Öğe | Konum |
|-----|-----|-------|
| KAPI | Daire giriş kapısı (koyu ceviz, çelik, iki kilitli) | Batı duvarı, y=2.4–3.6 · **içe ve sağa (güneye) açılır** |
| KOMBİ | Gömme kombi dolabı, beyaz panjur kapaklı | Koridorun güney duvarı, x=0.0–1.0 · girişte hemen sağda |
| K-B | Banyo kapısı (beyaz ahşap, buzlu camlı) | Koridorun güney duvarı, x=1.6–2.3 |
| ▣ KAPAK | Asma tavan kapağı, 60×60 cm | Koridor tavanı, x=1.9–2.5, y=2.9–3.5 · **koridor ortasının biraz kuzeyinde** |
| AYK | Ayakkabılık (açık meşe, 100×35×90 cm) | Koridorun kuzey duvarı, x=1.8–2.8 · **kapağın tam altında** |
| T | Termostat (beyaz, kare, dijital ekran) | Koridorun kuzey duvarı, x=3.5, yerden 1.50 m |
| K-O | Oturma odası kapısı (çift kanatlı, buzlu camlı, genelde açık) | Koridorun kuzey duvarı, x=4.0–4.9 |
| K-M | Mutfak kapısı (beyaz ahşap, genelde açık) | Koridorun güney duvarı, x=4.5–5.3 |
| K-Y | Yatak odası kapısı (beyaz ahşap) | Koridorun kuzey duvarı, x=6.0–6.9 |
| K-Ç | Çalışma odası kapısı | Koridorun doğu uç duvarı (x=7.0) |
| P1, P2 | Oturma odası pencereleri (2 adet, 1.2×1.6 m, tül + koyu gri perde) | Kuzey cephe, sokağa bakar |
| P3 | Yatak odası penceresi (1.2×1.6 m, kalın perde) | Kuzey cephe, sokağa bakar |
| P4 | Mutfak penceresi (0.9×1.2 m) | Güney, avluya bakar |
| P5 | Çalışma odası penceresi | Güney, avluya bakar |

**Tavan yükseklikleri:** Daire genelinde 3.10 m. **Koridorun x=0–3.4 arası ve banyo: asma tavan nedeniyle 2.10 m.** Koridor x=3.4'ten sonra yine 3.10 m. Bu tavan farkı koridor görsellerinde **mutlaka görünmelidir** (alçak bölümden yüksek bölüme geçen bir kiriş çizgisi).

**Kalıcı nesne konumları (değişmez):**
- Kitaplık: oturma odası batı duvarı (B2-A'daki gizli kamera burada, 3. raf).
- Kanepe: oturma odası, doğu duvarına yaslı, pencerelere dik.
- Koltuk (yeşil kadife, eski): Ayla onu pencere önüne koyar. Kenan her gece parkedeki 4 izin üstüne geri çeker: **x≈1.5, y≈6.0, kitaplığın önü.**
- Yatak: başı doğu duvarında. Ayla pencere tarafında (kuzey), Mert kapı tarafında (güney) yatar.
- Diş fırçası bardağı: banyo lavabosunun sol köşesi.

---

## 3. MASTER LOCATION PROMPT'LAR

### L01 — IHLAMUR SOKAK VE APARTMAN DIŞ CEPHESİ
**Mimari:** 1978 yapımı, 4 katlı (zemin + 3), betonarme, kirli krem sıvalı bir apartman. Ön cephede her katta 4 pencere, ortada küçük balkonsuz merdiven penceresi şeridi. Kapı üstünde mozaik harflerle "IHLAMUR APT. 1978". Çatı kiremit kaplı. Sokak dar (5 m), Arnavut kaldırımı, iki yanda park etmiş arabalar, karşıda benzer eski binalar ve kapalı bir köşe dükkânı (eski SARI ANAHTAR, kepenk inik, soluk tabela izi).
**Işık:** Sokak lambası soğuk beyaz LED (turuncu sodyum değil!). Gündüz gri kasım bulutu.
**Ses:** Uzak trafik, martı, kepenk sesi, gece köpek havlaması.
```
LOCATION L01: a narrow Istanbul back street with worn cobblestones, 5 meters wide, cars parked on both sides,
a 1978 four-storey concrete apartment building with dirty cream plaster facade, four windows per floor,
small mosaic sign "IHLAMUR APT. 1978" above a heavy dark wooden entrance door with frosted glass,
terracotta tiled pitched roof with a small dormer, old black electrical cables crossing the street,
across the street similar aging buildings and a closed corner shop with its metal shutter down and a faded ghost outline of an old sign,
cold white LED street lamp on a wall bracket
```
**Saate göre:**
| Kod | Prompt |
|-----|--------|
| T-GÜN | `overcast grey November daylight, flat soft light, wet cobblestones, muted colors` |
| T-AKŞAM | `dusk, deep blue sky, a few windows lit warm, street lamp just turned on, cold blue shadows` |
| T-GECE | `3 AM, near-total darkness, only the cold white LED street lamp and one or two lit windows, thin mist, black wet cobblestones reflecting light` |

### L02 — MERDİVEN BOŞLUĞU, 3. KAT SAHANLIĞI VE ÇATI KAPISI
**Mimari:** Dar (1.1 m) mozaik basamaklı merdiven, siyah ferforje korkuluk, ahşap tırabzan. Duvarlar yarıya kadar koyu yeşil yağlı boya, üstü kirli krem. 3. kat sahanlığı 2.2×2.0 m. **Batıda Daire 8 kapısı, doğuda Daire 7 kapısı, yüz yüze.** Sahanlıktan yarım kat (8 basamak) yukarıda, dar bir platformda 0.8×1.2 m'lik **gri metal çatı kapısı** (paslı menteşeler, B5-A'dan sonra asma kilitli).
**Işık:** Tavanda zaman ayarlı otomatik ışık (sarımsı-beyaz ampul, **90 saniyede söner**, düğmesinde kırmızı LED). Yarım kattaki küçük pencereden gelen soğuk ışık.
**Ses:** Otomatik ışık rölesinin tık sesi, ayak sesi yankısı, rüzgârın çatı kapısını hafifçe sarsması.
```
LOCATION L02: narrow apartment stairwell of an old 1970s Istanbul building, terrazzo mosaic stairs 1.1 m wide,
black wrought-iron railing with a worn wooden handrail, walls painted dark green oil paint up to waist height and dirty cream above,
third-floor landing 2.2 x 2 m with two facing dark walnut apartment doors, door "8" on the west side and door "7" on the east side,
brass door numbers, a doormat in front of each, a small timer light switch glowing red,
eight more steps rising to a narrow upper platform with a small grey metal attic door 0.8 x 1.2 m with rusty hinges
```
| Kod | Prompt |
|-----|--------|
| T-IŞIK-AÇIK | `bare yellowish-white bulb on the ceiling, harsh top light, deep shadows under the stairs` |
| T-IŞIK-KAPALI | `timer light off, near darkness, only cold moonlight from a small stairwell window and the tiny red glow of the light switch` |

### L03 — DAİRE 7 GİRİŞ KORİDORU *(en çok kullanılan mekân)*
**Mimari:** 7.0×1.2 m. Batıdaki giriş kapısından doğudaki çalışma odasına uzanır. İlk 3.4 metre alçak (2.10 m asma tavan), sonra 3.10 m. Duvarlar kırık beyaz yeni boya (yeni boyanın altından eski bir kat yer yer seziliyor). Zemin eski meşe balıksırtı parke, girişte gri bir paspas.
**Kritik öğeler:** Kapak (tavanla aynı beyaz, kenarlarında ince gri kurum gölgesi, B4'e kadar fark edilmez). Altında ayakkabılık, üstünde anahtarlık kâsesi. Termostat. Sağda kombi dolabı (beyaz panjur kapak). Tavanda tek bir yuvarlak opal plafonyer.
**Işık:** Plafonyer (sıcak beyaz). Geceleri yalnızca **termostat ekranının soğuk mavi-beyaz ışığı** ve oturma odasından sızan sokak lambası ışığı.
**Ses:** Termostatın röle "tık"ı, kombinin ateşleme sesi ve uğultusu, parke gıcırtısı, asma tavandan gelen ince tıkırtılar.
```
LOCATION L03: a narrow 7 m long, 1.2 m wide entrance corridor in an old Istanbul apartment, freshly painted off-white walls,
worn oak herringbone parquet floor, dark walnut front door at the west end with two locks,
the first 3.4 m of the corridor has a LOWERED CEILING at 2.10 m (a built-in loft above), then the ceiling rises to 3.10 m with a visible beam line,
in the lowered ceiling a nearly invisible 60x60 cm square hatch painted the same white as the ceiling with a faint grey soot shadow along its edges,
directly below the hatch against the LEFT (north) wall a light oak shoe cabinet 90 cm tall with a small ceramic key bowl on top,
a small square white digital wall thermostat on the left wall at 1.5 m height,
on the RIGHT (south) wall near the entrance a built-in white louvered closet door hiding a combi boiler, next to it a white bathroom door with frosted glass,
on the left wall a double glazed door to the living room, at the far east end a closed white door
```
| Kod | Prompt |
|-----|--------|
| T-GÜN | `soft grey daylight spilling from the open living room door, ceiling light off, calm` |
| T-AKŞAM | `warm white round opal ceiling light on, homely but slightly too bright, hard shadows under the loft ceiling` |
| T-GECE-0310 | `3:10 AM, all lights off, the ONLY light is the cold blue-white glow of the thermostat display on the wall and faint cold street light leaking from the living room, the hatch above is a dark square edge barely visible, deep blue-black shadows` |
| T-ALEV | `the louvered boiler closet slightly open, a small intense ORANGE flame glow flickering through the slats, the only saturated warm color in the frame` |

### L04 — OTURMA ODASI
**Mimari:** 5.6×4.9 m, 3.10 m tavan, alçı kartonpiyer. Kuzeyde sokağa bakan iki pencere (P1, P2), beyaz tül ve koyu gri perde. Parke koridordakinin devamı. **Kitaplığın önünde parkede 4 soluk, koyu çukur iz** (eski koltuğun yeri).
**Mobilya:** Batı duvarında boydan beyaz kitaplık (yarısı kitap, yarısı taşınma kolileri). Eski yeşil kadife koltuk. Doğu duvarında gri kumaş kanepe. Önünde alçak ceviz sehpa. Pencere önünde Ayla'nın büyük bitkisi (monstera). Duvarda henüz asılmamış, yere dayalı çerçeveler.
**Işık:** Gündüz pencerelerden gri ışık. Akşam yer lambası (sıcak sarı). Gece sokak lambasının soğuk beyaz ışığı tülden süzülür ve tavanda pencere desenleri oluşturur.
**Ses:** Sokak sesleri, saat tik-takı (duvar saati, kitaplık üstünde), kalorifer peteğinin çıtırtısı.
```
LOCATION L04: a spacious old Istanbul living room 5.6 x 4.9 m with 3.10 m high ceilings and simple plaster crown molding,
two tall windows on the north wall facing the street with white sheer curtains and heavy dark grey drapes,
worn oak herringbone parquet with FOUR FAINT DARK DENTED MARKS in front of the bookshelf where an old armchair stood for years,
a tall white bookshelf along the west wall half filled with books and half with unopened moving boxes, a wall clock on top,
an old bottle-green velvet armchair, a grey fabric sofa against the east wall, a low walnut coffee table,
a large monstera plant by the window, unhung picture frames leaning against the wall, a white panel radiator under each window
```
| Kod | Prompt |
|-----|--------|
| T-GÜN | `flat overcast daylight through sheer curtains, dust in the air, muted greens and greys` |
| T-AKŞAM | `single warm floor lamp in the corner, rest of the room in soft shadow, windows deep blue` |
| T-GECE | `lights off, cold white street light filtering through the sheer curtains casting pale window-frame patterns across the ceiling and floor, deep blue darkness` |

### L05 — MUTFAK
**Mimari:** 3.6×2.4 m. Güneyde avluya bakan pencere. Eski beyaz laminat dolaplar, yeni gri tezgâh, beyaz metro fayans. Buzdolabı doğu duvarında. Küçük iki kişilik masa pencere önünde.
**Önemli eşya:** Ayla'nın kupası (krem rengi, ağzında ince lacivert çizgi, kulpu çatlak). Buzdolabındaki yoğurt kâsesi.
**Işık:** Tezgâh altı LED (soğuk), tavan floresan. Gece buzdolabının iç ışığı.
**Ses:** Buzdolabı motoru, damlayan musluk, avludan gelen komşu sesleri.
```
LOCATION L05: a small narrow Istanbul kitchen 3.6 x 2.4 m, old white laminate cabinets with brushed metal handles, new grey stone-look countertop,
white subway tile backsplash, a south-facing window above a small square table with two wooden chairs looking onto a grey inner courtyard,
an older white refrigerator on the east wall, a cream ceramic mug with a thin navy rim and a cracked handle on the counter
```
| Kod | Prompt |
|-----|--------|
| T-GÜN | `pale overcast light from the courtyard window, quiet` |
| T-GECE | `dark kitchen lit only by the cold white light from the slightly open refrigerator door, long shadows` |

### L06 — YATAK ODASI
**Mimari:** 4.4×4.9 m. Kuzeyde sokağa bakan pencere (P3), kalın koyu mavi perde. Kapı odanın güney duvarının batı ucunda, koridora açılıyor. **Nurten bu odada öldü.**
**Mobilya:** Çift kişilik yatak, başı doğu duvarında, gri keten nevresim. İki komodin. Batı duvarında beyaz gardırop. Pencere altında petek.
**Işık:** Komodin lambaları. Gece perde aralığından ince bir şerit sokak ışığı. Telefon ekranı ışığı.
**Ses:** Petek çıtırtısı, iki kişinin nefesi, tavan arasından gelen belli belirsiz ses.
```
LOCATION L06: an old Istanbul bedroom 4.4 x 4.9 m, high ceiling, one tall north window with heavy dark blue curtains slightly parted,
a double bed with its headboard against the east wall, rumpled grey linen bedding, two small nightstands with simple lamps,
a white wardrobe on the west wall, a white radiator under the window, oak parquet floor, the bedroom door in the south wall near the west corner opening to the corridor
```
| Kod | Prompt |
|-----|--------|
| T-GECE | `darkness, a single thin vertical strip of cold street light through the curtain gap falling across the bed, a phone screen glowing blue on the nightstand` |
| T-SABAH | `grey dawn light seeping around the curtains, cold and colorless` |

### L07 — BANYO
**Mimari:** 2.4×2.4 m, alçak tavan (2.10 m, üstü asma tavan depo). Pencere yok, tavanda havalandırma ızgarası. Beyaz fayans, gri derz, küvetli duş, beyaz lavabo, üstünde aynalı dolap.
**Önemli eşya:** Lavabonun sol köşesinde şeffaf cam diş fırçası bardağı (B2-B'de 3 fırça).
**Işık:** Aynanın üstünde soğuk beyaz aplik.
**Ses:** Havalandırma fanının uğultusu (asma tavanla bağlantılı), damlayan su.
```
LOCATION L07: a small windowless bathroom 2.4 x 2.4 m with a LOW ceiling at 2.10 m and a square metal ventilation grille in the ceiling,
white square tiles with grey grout, a white bathtub with a shower curtain, a white pedestal sink with a mirrored cabinet above,
a clear glass toothbrush cup on the left corner of the sink, a single cold white light above the mirror
```
| Kod | Prompt |
|-----|--------|
| T-SABAH-BUĞU | `cold white light, the mirror edges fogged with condensation as if someone just showered, a damp towel hanging crooked` |

### L08 — ÇALIŞMA ODASI (Ayla) *(yardımcı mekân)*
```
LOCATION L08: a small 3 x 3.6 m study room with a south window onto the grey courtyard, a large wooden drawing desk with a desk lamp,
scattered sketches of the apartment's rooms pinned to the wall in a grid, pencils, an open black sketchbook, a tablet stand
```

### L09 — ASMA TAVAN DEPO *(en kritik gizli mekân)*
**Mimari:** x=0–3.4, y=0–3.6 (12 m²), **iç yükseklik yalnızca 1.0 m** (insan ancak emekleyerek ya da çömelerek hareket eder). Taban kontrplak, üstüne serilmiş eski halılar. Tavanı binanın betonu. Ahşap kirişler. Kapak koridora açılıyor (x=1.9–2.5). **Batı duvarında 70×70 cm sökülebilir kontrplak panel → çatı arası (L10).**
**İçerik (sabit yerleşim):**
- **Kuzey yarısı, "Nurten'in köşesi":** Katlanmış krem hırka, F-1, F-2 ve F-4 fotoğrafları çerçeveli, bir sıra halinde. Boş morfin kutuları düzenli bir piramit halinde. Yarım kalmış örgü sepeti. Küçük bir pilli lamba.
- **Orta:** İnce bir sünger yatak, gri battaniye, termos, katlanmış bir hastane taburcu çantası, bir defter.
- **Güney yarısı:** Kombinin **baca borusu** (gri alüminyum, 10 cm çaplı) güneye doğru dış duvara uzanır. **Ortasındaki eklem gevşetilmiş, etrafı eski bir bezle ve gümüş bantla sarılı.** Etrafında hafif kurum lekesi.
- **Batı duvarının dibi:** Kilitli, ezik, yeşil boyalı **metal kutu** (40×25×20 cm), üstünde "SARI ANAHTAR" çıkartması.
- **B2-A dalında:** Kayıp Wi-Fi kamera yatağın üstünde.
**Işık:** Doğal ışık yok. Pilli lamba (soluk sarı), ya da girenlerin telefon feneri (sert beyaz koni).
**Ses:** Kombinin borudan yükselen uğultusu, boru eklemindeki hafif ıslık, toz, ahşap çıtırtısı.
```
LOCATION L09: a cramped hidden storage loft inside an apartment, only 1 meter high, 3.4 x 3.6 m, plywood floor covered with old worn kilim rugs,
raw concrete ceiling with wooden joists, dust in the air, a 60x60 cm open hatch in the floor letting up a pale rectangle of light from the corridor below,
on one side an arranged shrine-like corner: a folded cream cardigan, three framed faded photographs of a smiling woman in a neat row, a neat pyramid of empty medicine boxes, a basket of unfinished knitting, a small battery lamp,
in the middle a thin foam mattress with a grey blanket, a steel thermos, a worn notebook,
along the other side a grey 10 cm aluminum boiler flue pipe running to the outer wall with its middle joint loosened and wrapped in an old rag and silver duct tape, faint black soot stains around it,
against the far wall a dented green metal box with a small faded "SARI ANAHTAR" sticker, and a removable 70x70 cm plywood panel leading into darkness
```
| Kod | Prompt |
|-----|--------|
| T-FENER | `lit only by a harsh white phone flashlight cone, everything outside the cone pitch black, floating dust in the beam` |
| T-LAMBA | `faint dim yellow glow of a small battery lamp, intimate, sad, warm only in a tiny circle` |

### L10 — ÇATI ARASI
**Mimari:** Binanın tüm çatısı boyunca uzanan, kırma çatının altındaki boşluk. En yüksek noktası 2 m. Ahşap çatı makasları, kiremitlerin altı, aralardan sızan ince ışık çizgileri. Zemin cüruf ve toz. Büyük, eski bir **galvaniz su deposu** (Kenan'ın saklandığı yer). Bir köşede metal çatı kapısı (L02'ye açılır), diğer tarafta deponun panel açıklığı.
**Ses:** Rüzgâr, kiremit tıkırtısı, güvercin kanadı, uzak şehir uğultusu.
```
LOCATION L10: a dusty dark attic under a pitched tiled roof of an old apartment building, timber roof trusses, thin lines of light leaking between roof tiles,
floor of loose cinders and dust, a large old galvanized metal water tank casting a deep shadow, cobwebs, a small grey metal door in one corner,
a low square opening in a side wall leading into a hidden loft
```
| Kod | Prompt |
|-----|--------|
| T-GECE | `almost total darkness, only faint cold moonlight lines between the tiles, a flashlight beam searching` |

### L11 — BODRUM / KÖMÜRLÜK 7
**Mimari:** Alçak (2.2 m) beton koridor. İki yanda ahşap çıtalı ve tel örgülü, numaralı kapılı depo bölmeleri (1–8). Çıplak ampuller, boru ve sayaç sırası. Nem lekeleri.
**Kömürlük 7'nin içi:** "NURTEN" yazılı koliler, sökülmüş eski anahtar kopyalama makinesi, sırtüstü yatırılmış "SARI ANAHTAR" tabelası (sarı zemin, siyah harf, paslı), dosya kutusu (taburcu kâğıdı, ölüm belgesi), kapıya bantlanmış Hikmet'in notu.
**Kilit:** Eski pirinç asma kilit. **SARI ANAHTAR damgalı pirinç anahtar bunu açar.**
**Ses:** Su borusu tıkırtısı, sayaç tıkırtısı, ampulün vızıltısı, yukarıdan boğuk ayak sesleri.
```
LOCATION L11: a low damp basement corridor of an old Istanbul apartment, raw concrete walls with water stains,
storage cells on both sides made of wooden slats and chicken wire with painted numbers 1 to 8, exposed pipes and a row of utility meters,
bare hanging bulbs, storage cell number 7 open: cardboard boxes labeled "NURTEN" in marker, a dismantled old key-cutting machine,
a rusty yellow shop sign with black letters "SARI ANAHTAR" lying on its back, a file box with papers, an old brass padlock hanging open
```
| Kod | Prompt |
|-----|--------|
| T-AMPUL | `one bare yellow bulb swinging slightly, harsh moving shadows, the rest in darkness` |

### L12 — DAİRE 8, SAADET'İN OTURMA ODASI
**Mimari:** Daire 7'nin ayna simetrisi (bkz. not), ama 40 yıllık eşyalarla dolu. Kahverengi oymalı büfe, dantel örtüler, el yapımı yastıklar. Köşede eski bir dikiş makinesi ve terzi mankeni. Duvarda **F-1 fotoğrafı** ve eski aile fotoğrafları. Sehpa üstünde ince belli çay bardakları. Mutfağa açılan kapıdan görünen tezgâhta **beyaz işlemeli bir bezle örtülü tabak.**
**Işık:** Sarı tonlu avize, dantel abajur. Her zaman biraz loş.
**Ses:** Duvar saati, radyo (alçak sesle eski Türk sanat müziği), çay kaşığı tıngırtısı, dikiş makinesinin sessizliği.
```
LOCATION L12: an elderly Turkish woman's living room in an old Istanbul apartment, crowded with 40 years of belongings,
a dark carved wooden sideboard with lace doilies, crocheted cushions on a brown velvet sofa, an old black sewing machine and a dressmaker's mannequin in the corner,
many old framed family photographs on the wall including one of a smiling couple sitting in a green velvet armchair,
thin tulip-shaped Turkish tea glasses on a small table, through the kitchen doorway a plate covered with a white embroidered cloth on the counter,
warm yellow chandelier light with lace lampshades, slightly dim, nostalgic and heavy
```

> **Not:** Daire 8, Daire 7'nin batıya doğru ayna simetrisidir. Kapısı sahanlığın batı tarafında, Daire 7'nin kapısıyla yüz yüze. Yalnızca oturma odası ve mutfak girişi gösterilir.

### L13 — ARABA İÇİ (B6-GİT)
**Araç:** Mert'in 2014 model, gri, kompakt bir hatchback'i. Marka ve logo gösterilmez. Sokakta binanın tam karşısına park edilmiş.
**Kadraj:** Ön camdan, 3. kattaki Daire 7 pencerelerine (sokaktan bakınca en üst katın SOL yarısı: önce iki oturma odası penceresi, sonra yatak odası penceresi) yukarı doğru açı.
**Ses:** Kapalı araç sessizliği, buğulanan cam, motor kapalı, telefon titreşimi, dışarıda rüzgâr.
```
LOCATION L13: the interior of a small grey 2014 compact hatchback car with no visible brand logos, parked on a dark narrow cobblestone street at night,
fogged windshield edges, the dashboard dark, two front seats reclined slightly, a phone screen glowing,
through the windshield the cream facade of an old four-storey apartment building, the top floor windows on the left half visible above,
cold white LED street light reflecting on the glass
```

### L14 — YARDIMCI MEKÂNLAR (sonsöz / finaller)
| Kod | Mekân | Prompt |
|-----|-------|--------|
| L14-A | Hastane koridoru (F3) | `a quiet hospital corridor at night, pale green walls, linoleum floor reflecting cold fluorescent light, an empty plastic chair` |
| L14-B | Hastane odası (F2, F3, F4 sonsöz) | `a simple hospital room, a single bed by a window with winter light, a grey wool scarf with a dark red stripe folded on the blanket` |
| L14-C | Ayla'nın yeni evinin kapısı (sonsöz) | `a clean modern apartment hallway, a plain white door with a new silver lock, soft winter morning light, a hand holding a single new key` |
| L14-D | Ambulans ve itfaiye ışıkları, sokak (finaller) | `L01 at night lit by pulsing red and blue emergency lights reflecting on wet cobblestones, a fire truck and an ambulance blocking the narrow street` |

---

## 4. MEKÂN RENK PALETİ (bütün dizi)

| Ortam | Ana renkler | HEX |
|-------|-------------|-----|
| Gece genel | Mavi-siyah, çelik mavi, soğuk gri | `#0E1420` `#2B3A4A` `#5C6773` |
| Termostat / ekran ışığı | Soğuk mavi-beyaz | `#CFE3F2` |
| Sokak LED ışığı | Soğuk beyaz | `#E6ECEF` |
| Gündüz iç mekân | Kırık beyaz, gri meşe, soluk yeşil | `#E8E4DC` `#8A7A66` `#7C8C7A` |
| Saadet'in evi | Bal sarısı, koyu kahve, eski dantel | `#C9A45C` `#4A3426` `#EDE3CF` |
| Bodrum | Kirli sarı ampul, nem yeşili | `#B59A4E` `#3E4A3C` |
| **TEHLİKE (yalnızca kombi alevi)** | Doygun turuncu | `#FF7A1A` |
| Acil ışıklar (finaller) | Kırmızı / mavi | `#D9262C` `#2756D9` |

---

## 5. ORTAM SESİ KÜTÜPHANESİ (mekân başına sabit "oda tonu")

| Mekân | Oda tonu (sürekli) | Belirgin sesler |
|-------|---------------------|-----------------|
| L01 Sokak | Uzak şehir uğultusu | Martı, köpek, rüzgâr, araba geçişi |
| L02 Merdiven | Yankılı sessizlik | Otomatik ışık rölesi, ayak sesi, çatı kapısının metal tıkırtısı |
| L03 Koridor | Çok alçak buzdolabı uğultusu | **Termostat tık'ı**, **kombi ateşlemesi (fuşş + uğultu)**, parke gıcırtısı, tavandan tıkırtı |
| L04 Oturma odası | Sokak uğultusu (camdan boğuk) | Duvar saati, petek çıtırtısı |
| L05 Mutfak | Buzdolabı motoru | Damlayan musluk |
| L06 Yatak odası | Derin sessizlik | Nefes, petek, telefon titreşimi |
| L07 Banyo | Havalandırma fanı | Damla, ayna buğusu (ses yok) |
| L09 Depo | Borudan gelen boğuk kombi uğultusu | Eklemden ince ıslık, kumaş hışırtısı |
| L10 Çatı arası | Rüzgâr | Kiremit, güvercin |
| L11 Bodrum | Ampul vızıltısı | Boru tıkırtısı, sayaç |
| L12 Saadet | Duvar saati | Alçak sesli radyo, çay kaşığı |
| L13 Araba | Kapalı kabin sessizliği | Telefon titreşimi, nefes |

> **Sessizlik kuralı:** Termostat tık'ı ve kombi ateşlemesi dizinin "imza sesleri". Bu sesler hiçbir zaman müzikle örtülmez. Her duyulduklarında müzik keser.
