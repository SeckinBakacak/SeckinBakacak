# AŞAMA 3-A — KARAKTERLER VE MASTER CHARACTER PROMPT (Dosya C)

**Dizi:** YEDEK ANAHTAR
**Kullanım kuralı:** Promptlar görsel üretim araçlarında en tutarlı sonucu verdiği için **İngilizce** yazıldı. Açıklamalar Türkçe.

Her görselde promptlar şu sırayla birleştirilir:

```
[GLOBAL STYLE BLOCK] + [CHARACTER BLOCK] + [OUTFIT BLOCK] + [SCENE / ACTION] + [GLOBAL NEGATIVE]
```

**CHARACTER BLOCK ve OUTFIT BLOCK metinleri kelimesi kelimesine kopyalanır, hiçbir zaman değiştirilmez.** Sahneye özel bilgi yalnızca SCENE / ACTION kısmına yazılır.

---

## 0. GLOBAL STYLE BLOCK (her promptun başına)

```
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism,
clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions,
painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth,
accurate architectural perspective, cinematic lighting, desaturated muted color palette,
cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition,
quiet unsettling mood, European adult animation feature quality
```

## 0.1 GLOBAL NEGATIVE (her promptun sonuna)

```
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI,
plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes,
extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands,
warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature,
blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter,
supernatural creature, ghost, glowing eyes
```

> **Kenan'a özel istisna:** Kenan'ın görsellerinde negatif listeden `missing fingers` çıkarılır ve pozitif prompta parmak tanımı eklenir (bkz. Kenan).

---

## 1. RENK KİMLİĞİ (karakter renk kodları)

Her karakterin kıyafetinde bir **imza rengi** var. Karanlık ve uzak planlarda bile izleyici karakteri bu renkten tanır.

| Karakter | İmza rengi | HEX | Kıyafetteki yeri |
|----------|-----------|-----|------------------|
| Ayla | Soluk hardal / okr | `#B8913A` | Örgü hırka |
| Mert | Lacivert | `#1F2A44` | Yün palto / koyu kapüşonlu |
| Kenan | Gri + tek koyu kırmızı şerit | `#6E6E6A` + `#6B1E1E` | Nurten'in ördüğü atkı |
| Saadet | Şişe yeşili | `#2F4A3A` | Örgü yelek |
| Hikmet | Bej + kehribar | `#BFAE8E` + `#C27A1E` | Trençkot + tespih |

> **Sanat yönetimi kuralı:** Doygun turuncu yalnızca **kombi alevi** için kullanılır. Bu renk tehlikenin sembolü. Başka hiçbir nesnede, ışıkta ya da kıyafette doygun turuncu olmaz. (Hikmet'in kehribar tespihi koyu ve mat tutulur.)

---

## 2. AYLA DEMİR — Ana karakter

### Kimlik kartı
| Özellik | Değer |
|---------|-------|
| Yaş | 30 |
| Boy | 1,66 m |
| Vücut yapısı | İnce-orta, dik ama gergin duruş, omuzları hafif içe dönük |
| Yüz şekli | Oval, hafif sivri çene, belirgin elmacık kemikleri |
| Göz rengi | Ela-kahverengi (yeşile çalan açık kahve) |
| Saç | Koyu kestane, omuz boyu, hafif dalgalı. Genellikle gevşek, alçak bir topuz, içine sıkıştırılmış bir kurşun kalem. Önden iki tutam yüzüne düşer. |
| Ten | Açık buğday, sıcak alt ton |
| Ayırt edici özellikler | **Sol gözünün altında küçük bir ben.** Sağ elinin işaret ve orta parmağında silik mürekkep / grafit lekeleri. Hafif göz altı halkaları (bölüm ilerledikçe koyulaşır, bkz. devamlılık). |
| Aksesuarlar | Sağ işaret parmağında ince gümüş yüzük. Sol elde ince altın alyans. Yalnızca çizerken taktığı ince metal çerçeveli yuvarlak gözlük. A5, siyah kapaklı, lastik bantlı eskiz defteri. |
| Konuşma / hareket | Az ve alçak sesle konuşur. Cümlelerini yarım bırakır. Nesnelere dokunarak düşünür (kupanın kulpunu çevirmek gibi). Gerilince alt dudağını ısırır. Hızlı ama dikkatli adımlar. |
| Kişilik | Detaycı, sezgisi güçlü, gözlemci, kendinden şüphe eden, inatçı |
| Geçmiş | Ankara doğumlu. İstanbul'da 6 yıldır serbest illüstratör. Çocukken "hayal gücü fazla" denip ciddiye alınmamış. Mert'le 4 yıllık evli. |
| Motivasyon | Gördüğü şeyin gerçek olduğunu kanıtlamak. Sonra da ondan ne pahasına olursa olsun doğru şeyi yapmak. |
| Korkuları | İnanılmamak. Delirdiğini düşünmek. Yalnız kalmak. |
| İlişkiler | **Mert:** seviyor ama son aylarda arada bir duvar hissediyor. **Saadet:** ilk günden ürkütücü ama çekici buluyor. **Hikmet:** güvenmiyor. **Kenan:** önce tehdit, sonra acıma ve sorumluluk. |

### CHARACTER BLOCK — AYLA
```
AYLA DEMIR, a 30-year-old Turkish woman, 166 cm tall, slim average build, slightly tense posture with shoulders turned inward,
oval face with a gently pointed chin and defined cheekbones, hazel-brown eyes, natural thick eyebrows,
small mole under her LEFT eye, light warm olive skin, faint under-eye shadows,
dark chestnut-brown shoulder-length wavy hair tied in a loose low messy bun with a graphite pencil stuck through it,
two loose strands falling at the front of her face, thin silver ring on right index finger, thin gold wedding band on left ring finger,
faint grey ink smudges on the fingertips of her right hand, observant cautious expression
```

### OUTFIT BLOCK — AYLA
| Kod | Kullanım | Prompt |
|-----|----------|--------|
| **A-EV** | Evde, gündüz ve akşam (ana kıyafet) | `oversized muted ochre-mustard chunky knit cardigan (#B8913A) with large wooden buttons, plain off-white cotton t-shirt, loose dark charcoal-grey wide-leg trousers, thick grey wool socks, no shoes` |
| **A-GECE** | Uyku, gece sahneleri | `faded light-grey long-sleeve cotton pajama top and matching loose pajama trousers, the ochre-mustard knit cardigan thrown over her shoulders, barefoot or grey wool socks` |
| **A-DIŞ** | Dışarı, bodrum, araba | `long dark olive-green hooded parka with fur-free hood, the ochre-mustard cardigan visible underneath at the collar, dark charcoal trousers, worn black leather ankle boots, black canvas tote bag` |
| **A-EPİLOG** | Sonsöz, Ocak 2027 | `long camel wool coat, cream turtleneck sweater, dark trousers, black ankle boots, hair down loose to shoulders for the first time` |

---

## 3. MERT DEMİR — Eş

### Kimlik kartı
| Özellik | Değer |
|---------|-------|
| Yaş | 33 |
| Boy | 1,81 m |
| Vücut yapısı | Geniş omuzlu, atletik ama son aylarda biraz yumuşamış. Ağırlığını tek ayağa veren huzursuz duruş. |
| Yüz şekli | Kare çene, düz ve güçlü burun, kalın kaşlar |
| Göz rengi | Koyu kahverengi |
| Saç | Siyah, yanları kısa, üstü 4–5 cm, geriye doğru elle taranmış (gün ilerledikçe dağılır) |
| Ten | Orta buğday, sıcak alt ton |
| Ayırt edici özellikler | **Sağ kaşının ortasından geçen ince, eski bir yara izi** (kaşta küçük bir boşluk). 3–4 günlük kısa sakal. |
| Aksesuarlar | Sol bilekte çelik kordonlu saat. Sol yüzük parmağında altın alyans. Elinden düşmeyen telefon. |
| Konuşma / hareket | Kısa ve kesin cümleler, savunmaya geçince alaycı. Sürekli telefonuna bakar. Gerilince çenesi kasılır, ensesini ovuşturur. Hızlı ve ağır adımlar. |
| Kişilik | Pragmatik, gururlu, koruyucu, utancını öfkeyle örten |
| Geçmiş | İzmir doğumlu. Bir lojistik firmasında planlama uzmanıydı, iki ay önce toplu işten çıkarmada işini kaybetti. Ayla'ya söylemedi. Ucuz kiralı bu evi bu yüzden ısrarla istedi. |
| Motivasyon | Ayla'yı korumak, ama önce kendi yalanını korumak. |
| Korkuları | Yetersiz görünmek. Ayla'nın gözünde küçülmek. |
| İlişkiler | **Ayla:** seviyor, yalanı aralarında büyüyen bir boşluk. **Hikmet:** ucuz kira yüzünden ona minnettar, bu yüzden itiraz etmiyor. **Kenan:** öfke, sonra korku. |

### CHARACTER BLOCK — MERT
```
MERT DEMIR, a 33-year-old Turkish man, 181 cm tall, broad shoulders, athletic build gone slightly soft,
square jaw, strong straight nose, thick dark eyebrows with a thin old scar cutting vertically through the middle of his RIGHT eyebrow leaving a small gap,
dark brown eyes, medium warm olive skin, short 4-day black stubble,
black hair short on the sides and 4-5 cm on top, pushed back by hand, slightly messy,
steel-bracelet wristwatch on left wrist, gold wedding band on left ring finger, restless guarded expression
```

### OUTFIT BLOCK — MERT
| Kod | Kullanım | Prompt |
|-----|----------|--------|
| **M-İŞ** | "İşe gidiyormuş" gibi yaptığı kıyafet | `dark navy wool overcoat (#1F2A44) knee length, light grey button-up shirt with no tie, dark charcoal chinos, brown leather derby shoes, black laptop backpack` |
| **M-EV** | Evde | `dark navy hoodie (#1F2A44) with no print, heather-grey sweatpants, black house slippers` |
| **M-GECE** | Uyku, gece | `plain dark grey t-shirt, heather-grey sweatpants, barefoot, the navy hoodie unzipped over it on cold nights` |
| **M-EPİLOG** | Sonsöz (`GÜVEN=yüksek` ise) | `dark navy wool overcoat, dark green knit sweater, dark jeans, brown boots` |

---

## 4. KENAN SARI — Evdeki üçüncü kişi

### Kimlik kartı
| Özellik | Değer |
|---------|-------|
| Yaş | 52 (60'ında gösteriyor) |
| Boy | 1,76 m (kamburluk yüzünden 1,70 görünüyor) |
| Vücut yapısı | Çok zayıf, kemikleri belirgin, omuzları düşük ve öne kamburlaşmış. Uzun kollar, iri ve damarlı eller. |
| Yüz şekli | Uzun ve çökük. Elmacık kemikleri çıkık, yanakları içe göçmüş. Derin alın çizgileri. |
| Göz rengi | Gri-yeşil. Gözler derin çukurlarda, kenarları kızarık, bakışı bulanık ve uzak. |
| Saç | Gri-beyaz, seyrekleşmiş, kısa ama dağınık, tepede açılma |
| Sakal | Kır-beyaz, bakımsız, 2–3 cm, düzensiz |
| Ten | Soluk, sarımsı-gri, güneş görmemiş. Dudaklar kuru ve çatlak. |
| Ayırt edici özellikler | **SOL İŞARET PARMAĞININ ÜST BOĞUMU YOK** (parmak ilk eklemden kesik, yuvarlanmış eski yara). Ellerin çizgilerinde silinmemiş eski metal yağı. Kuru, çatlak parmak uçları. |
| Aksesuarlar | **Nurten'in ördüğü gri yün atkı, tek bir koyu kırmızı şeritli** (hiç çıkarmaz). Boynunda kirli bir iple asılı tek bir eski anahtar (çatı arası kapısının anahtarı). |
| Konuşma / hareket | Neredeyse hiç konuşmaz. Konuşunca fısıltıyla, kelimeleri yavaş ve kopuk. **Sessiz, temkinli ve yavaş adımlar.** Hareketin ortasında donar, bir şey dinler gibi. Nesnelere çok özenle dokunur (eşyaları "yerine" koyarken). Ayakkabı giymez, yalnızca yün çorap. |
| Kişilik | Yasın içinde kaybolmuş, sadık, titiz, içe kapanık. Kronik karbonmonoksit zehirlenmesinden zihni bulanık. |
| Geçmiş | 20 yıl mahallenin çilingiri ("SARI ANAHTAR"). Nurten'le 25 yıl evli, çocukları yok. Nurten 14 Ocak 2025'te 03:10'da evde öldü. Yasa dışı tahliyeden sonra asma tavanda yaşıyor. |
| Motivasyon | Nurten'in evini, eşyalarını ve "düzenini" korumak. Onu ısıtmak. |
| Korkuları | Nurten'in eşyalarının atılması. Bir yere kapatılmak. Unutmak. |
| İlişkiler | **Saadet:** tek bağı, ama yüzüne bakamaz. **Hikmet:** onu evinden atan adam. **Ayla ve Mert:** "geçici misafirler", sonra tehdit, sonra… |

### CHARACTER BLOCK — KENAN
```
KENAN SARI, a 52-year-old Turkish man who looks 60, 176 cm tall but stooped and hunched forward, very thin and gaunt with visible collarbones,
long hollow face with sunken cheeks and prominent cheekbones, deep forehead lines,
deep-set grey-green eyes with red-rimmed lids and a distant clouded gaze,
thinning short unkempt grey-white hair, receding on top, uneven untrimmed grey-white beard 2-3 cm long,
pale sallow grey-yellow skin, dry cracked lips,
large veined hands with old black machine grease in the skin creases,
his LEFT INDEX FINGER IS MISSING ITS TOP SEGMENT, cut off at the first knuckle, an old rounded healed stump, all other fingers normal (anatomically exact: left thumb, middle, ring and little fingers are complete, only the index finger is shortened),
always wearing a long hand-knitted grey wool scarf with one single dark red stripe near one end,
an old brass key hanging on a dirty string around his neck, silent careful posture
```
> **Not:** Kenan'ın görsellerinde GLOBAL NEGATIVE'den `missing fingers (except where specified)` ifadesi çıkarılır, yerine `extra fingers on left hand, complete left index finger` eklenir.

### OUTFIT BLOCK — KENAN
| Kod | Kullanım | Prompt |
|-----|----------|--------|
| **K-ANA** | Bütün güncel sahneler (tek kıyafet) | `worn dark brown corduroy jacket with frayed cuffs and elbows, faded blue-black checkered flannel shirt buttoned to the top, baggy grey wool trousers with dust on the knees, thick dark grey wool socks with no shoes, the grey scarf with one dark red stripe wrapped twice around his neck` |
| **K-ESKİ** | Fotoğraflar, 2015 civarı, dükkânda | `KENAN at 42: healthy fuller face, full dark brown beard neatly trimmed, dark brown hair with grey at the temples, warm confident smile, navy work apron with "SARI ANAHTAR" embroidered in small white letters over a light blue shirt, sleeves rolled up, left index finger already missing its top segment` |
| **K-HASTANE** | Final 2–4 sonsözü | `plain pale blue hospital gown, a thin grey hospital blanket over his shoulders, the grey red-striped scarf in his hands` |

---

## 5. SAADET ÜNAL — Karşı komşu

### Kimlik kartı
| Özellik | Değer |
|---------|-------|
| Yaş | 73 |
| Boy | 1,55 m |
| Vücut yapısı | Kısa, yuvarlak, dolgun. Hafif kambur ama dik durmaya çalışan. Yavaş. |
| Yüz şekli | Yuvarlak, derin kırışıklı. Ağzının kenarlarında aşağı inen çizgiler. Sert ama yumuşak. |
| Göz rengi | Açık kahverengi, kalın camlı gözlüğün arkasında büyümüş görünür |
| Saç | Beyaz-gri, ensede sıkı bir topuz, siyah firketelerle tutturulmuş |
| Ten | Açık ten, ellerinde ve alnında yaşlılık lekeleri |
| Ayırt edici özellikler | Boncuklu bir zincirle boynuna asılı **kalın camlı, kahverengi kemik çerçeveli gözlük**. Evde boynunda sarı bir **terzi mezurası**. Sağ orta parmağında eski bir yüksük nasırı. |
| Aksesuarlar | Mezura, gözlük zinciri, ince altın bilezik (tek), kapı aralığından bakarken kapı zincirine dayanan eli |
| Konuşma / hareket | Çok az konuşur, her cümlesi iki anlamlı. Ses tonu düz ve kısık. Kapıyı hiç tam açmaz, zincir takılı aralıktan bakar. Ağır, terlik sürüyen adımlar. |
| Kişilik | Sır tutan, sadık, suçluluk taşıyan, gözlemci, yalnız |
| Geçmiş | 40 yıl terzilik yaptı. Eşi 2008'de öldü, çocukları yurt dışında. Nurten'in 14 yıllık en yakın dostuydu. Nurten'in ona verdiği Daire 7 yedek anahtarını hâlâ saklıyor. |
| Motivasyon | Kenan'ı korumak. Nurten'e verdiği sözü tutmak ("Kenan'a göz kulak ol"). |
| Korkuları | Kenan'ın bir kuruma kapatılması. Suskunluğunun birine zarar vermesi. |
| İlişkiler | **Kenan:** bir oğul gibi, ama yüzleşemediği biri. **Ayla:** ona Nurten'i hatırlatıyor. **Hikmet:** ondan nefret ediyor ama sesini çıkarmıyor. |

### CHARACTER BLOCK — SAADET
```
SAADET UNAL, a 73-year-old Turkish woman, 155 cm tall, short round plump build, slightly hunched but holding herself upright,
round deeply wrinkled face with downturned lines at the corners of her mouth, stern but soft expression,
light brown eyes magnified behind thick-lensed brown tortoiseshell glasses hanging on a beaded chain,
white-grey hair pulled tightly into a low bun at the nape held with black hairpins,
fair skin with age spots on her hands and forehead, a yellow tailor's measuring tape draped around her neck,
one thin gold bangle on her right wrist, watchful silent expression
```

### OUTFIT BLOCK — SAADET
| Kod | Kullanım | Prompt |
|-----|----------|--------|
| **S-EV** | Evde ve kapı aralığında (ana kıyafet) | `dark bottle-green hand-knitted wool vest (#2F4A3A) buttoned over a cream long-sleeve blouse with a small round collar, long dark grey A-line wool skirt below the knee, thick brown opaque stockings, worn brown felt house slippers` |
| **S-GECE** | Gece, çatı kapısına tabak götürürken | `the bottle-green vest over a long faded floral flannel nightgown in muted grey-lilac, a dark grey wool shawl around her shoulders, brown felt slippers, carrying a plate covered with a white embroidered cloth` |
| **S-DIŞ** | Dışarıda, final ve sonsöz | `long black wool coat, thin muted lilac headscarf loosely tied under the chin, black orthopedic shoes, black handbag` |

---

## 6. HİKMET AKSOY — Ev sahibi

### Kimlik kartı
| Özellik | Değer |
|---------|-------|
| Yaş | 61 |
| Boy | 1,72 m |
| Vücut yapısı | Tıknaz, göbekli, kalın boyunlu. Dik ama ağır. |
| Yüz şekli | Yuvarlak, sarkık gıdı ve yanaklar. Küçük, dar gözler. |
| Göz rengi | Koyu kahverengi |
| Saç | Tepesi açık. Yanlardaki gri saçlar özenle yana taranmış. |
| Bıyık | Kalın, bakımlı, gri |
| Ten | Kırmızımsı-pembe, özellikle burun ve yanaklarda |
| Ayırt edici özellikler | **Sağ elinde sürekli çektiği koyu kehribar tespih** (gerildikçe hızlanır). Sol serçe parmağında altın bir mühür yüzük. |
| Aksesuarlar | Tespih, mühür yüzük, göğüs cebinde katlanmış gözlük, araba anahtarı |
| Konuşma / hareket | Kibar, resmî ve "efendim"li. Göz teması kurmaz, konuşurken gözleri duvarlarda ve tavanda dolaşır. Gülümsemesi gözlerine ulaşmaz. Ağır, ölçülü adımlar. |
| Kişilik | Kibar görünümlü, hesapçı, korkak, kendini haklı çıkaran |
| Geçmiş | Emekli tapu memuru. Üç dairesi var. Kira artışı döneminde Kenan'ı yasa dışı yollarla tahliye etti. Önceki kiracı kaçınca kirayı düşürdü. |
| Motivasyon | Yaptığının ortaya çıkmaması. Evin "temiz" görünmesi. |
| Korkuları | Polis, mahkeme, mahalledeki itibarı. |
| İlişkiler | **Kenan:** onu tehdit olarak görüyor, "dengesiz" diyor. **Saadet:** ondan çekiniyor. **Ayla ve Mert:** sessiz kaldıkları sürece "iyi kiracılar". |

### CHARACTER BLOCK — HİKMET
```
HIKMET AKSOY, a 61-year-old Turkish man, 172 cm tall, stocky heavy build with a round belly and thick neck,
round face with heavy jowls and full cheeks, small narrow dark brown eyes,
thick well-groomed grey moustache, balding on top with grey side hair neatly combed over,
ruddy pinkish complexion especially on the nose and cheeks,
a string of dark matte amber prayer beads (tespih) always held in his right hand,
a gold signet ring on his left little finger, polite closed-lip smile that does not reach his eyes, avoiding eye contact
```

### OUTFIT BLOCK — HİKMET
| Kod | Kullanım | Prompt |
|-----|----------|--------|
| **H-ANA** | Bütün sahneler | `beige knee-length trench coat (#BFAE8E) belted loosely, brown wool V-neck sweater over a white collared shirt, grey pressed trousers, polished black leather shoes, folded reading glasses in the breast pocket` |
| **H-DIŞ** | Sokak, arabada gece gözetleme | `H-ANA outfit plus a grey tweed flat cap` |

---

## 7. NURTEN SARI — Yalnızca fotoğraflarda (konuşan karakter değil)

```
NURTEN SARI, a Turkish woman in her mid-to-late 40s, medium height, soft round face with kind laugh lines,
warm dark brown eyes, short chin-length hair dyed auburn-copper, light warm skin, gentle wide smile,
wearing a soft cream cardigan, often holding knitting needles or a cup of tea, photographed in warm faded film colors
```
**Fotoğraf seti (sabit, her sahnede aynı kareler kullanılır):**
| Kod | Fotoğraf | Nerede görünür |
|-----|----------|----------------|
| **F-1** | Nurten ve Kenan (K-ESKİ), Daire 7 oturma odasında koltukta yan yana, 2015. Koltuk parkedeki izlerin üstünde. | Saadet'in duvarı (B3-B), depo (B4-A) |
| **F-2** | Nurten, örgü örerken, mutfak penceresinin önünde. Kucağında yarım kalmış gri atkı, kırmızı şerit. | Depo (B4-A), sonsöz |
| **F-3** | Kenan, SARI ANAHTAR dükkânının önünde. Kesik parmak net görünüyor. | Bodrum (B4-B) |
| **F-4** | Nurten'in hastalık döneminde, yatak odasında, başında yün bere, gülümsüyor. 2024. | Depo (B4-A) |

---

## 8. KARAKTER ETKİLEŞİM HARİTASI

```
                     SAADET (Daire 8)
              besliyor ↗   ↑ sırrı   ↖ ürkütüyor / Nurten'i hatırlatıyor
           KENAN ─────────┼───────────── AYLA
   evinden attı ↑          │               ↕ yalan / güven (GÜVEN bayrağı)
           HİKMET ─────────┴───────────── MERT
             "ucuz kira" minneti / sessizlik
```

---

## 9. BÖLÜMLERE GÖRE KARAKTER DURUMU (görsel devamlılık için ön tablo)

| Bölüm | Ayla | Mert | Kenan | Saadet | Hikmet |
|------|------|------|-------|--------|--------|
| B1 | A-EV / A-DIŞ, dinç, hafif göz altı halkası | M-İŞ / M-EV | Görünmez (yalnızca termostat, eşyalar) | S-EV, kapı aralığı | H-ANA, anahtar teslimi |
| B2 | A-EV / A-GECE, göz altları koyulaşıyor | M-EV / M-GECE | Yalnızca el (B2-A) | — | — |
| B3 | A-EV / A-GECE | M-EV | El (B3-B) | S-EV / S-GECE | H-ANA / H-DIŞ (B3-A) |
| B4 | A-EV / A-DIŞ (bodrum) | M-EV | Görünmez (yalnızca eşyaları) | — | — |
| B5 | A-EV, solgun, belirgin göz altları | M-EV | Görünmez | S-EV (kapı aralığı) | H-ANA (B5-A) |
| B6 | A-GECE (kal) / A-DIŞ (git), çok solgun | M-GECE / M-İŞ paltosu (arabada) | **K-ANA, ilk tam görünüş** | — | — |
| B7 | A-GECE → A-EPİLOG | M-GECE → M-EPİLOG | K-ANA → K-HASTANE (F2–F4) | S-GECE / S-DIŞ | Yalnızca soruşturmada (H-ANA) |

**Fiziksel bozulma çizelgesi (CO etkisi):**
- **Ayla ve Mert:** B1'de normal. B3'te hafif göz altı halkası. B5'te solgun ten, koyu halkalar, kuru dudak. B6'da gri-solgun ten, terli alın.
- **Kenan:** Bütün bölümlerde aynı (zaten ileri derecede). B6'da dudaklarda hafif kirazımsı kızarıklık *(CO'nun klinik işareti, çok ince tutulur)*.
