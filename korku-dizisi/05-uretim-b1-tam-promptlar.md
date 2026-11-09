# B1 — "SANTİMETRELER" · TAM GÖRSEL VE ANİMASYON PROMPTLARI

> Bu dosya `uretim/prompt_olustur.py` tarafından otomatik üretilir. **Elle düzenlemeyin.** Değişiklik için `uretim/sahneler/b1.json` ya da master `03*` dosyaları düzenlenip betik yeniden çalıştırılır.

**Plan sayısı:** 28 · **Görsel planların toplam süresi:** 132 sn (hedef 132 sn) · **Biçim:** 9:16, 1080×1920 (üretimde 2160×3840 önerilir)

---

## B1-S01  ·  S1  ·  0:00–0:04  ·  4 sn

Mekân `L06` · `T-GECE` · Karakter `AYLA` (A-GECE), `MERT` (M-GECE)

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L06: an old Istanbul bedroom 4.4 x 4.9 m, high ceiling, one tall north window with heavy dark blue curtains slightly parted, a double bed with its headboard against the east wall, rumpled grey linen bedding, two small nightstands with simple lamps, a white wardrobe on the west wall, a white radiator under the window, oak parquet floor, the bedroom door in the south wall near the west corner opening to the corridor, darkness, a single thin vertical strip of cold street light through the curtain gap falling across the bed, a phone screen glowing blue on the nightstand, AYLA DEMIR, a 30-year-old Turkish woman, 166 cm tall, slim average build, slightly tense posture with shoulders turned inward, oval face with a gently pointed chin and defined cheekbones, hazel-brown eyes, natural thick eyebrows, small mole under her LEFT eye, light warm olive skin, faint under-eye shadows, dark chestnut-brown shoulder-length wavy hair tied in a loose low messy bun with a graphite pencil stuck through it, two loose strands falling at the front of her face, thin silver ring on right index finger, thin gold wedding band on left ring finger, faint grey ink smudges on the fingertips of her right hand, observant cautious expression, wearing faded light-grey long-sleeve cotton pajama top and matching loose pajama trousers, the ochre-mustard knit cardigan thrown over her shoulders, barefoot or grey wool socks, MERT DEMIR, a 33-year-old Turkish man, 181 cm tall, broad shoulders, athletic build gone slightly soft, square jaw, strong straight nose, thick dark eyebrows with a thin old scar cutting vertically through the middle of his RIGHT eyebrow leaving a small gap, dark brown eyes, medium warm olive skin, short 4-day black stubble, black hair short on the sides and 4-5 cm on top, pushed back by hand, slightly messy, steel-bracelet wristwatch on left wrist, gold wedding band on left ring finger, restless guarded expression, wearing plain dark grey t-shirt, heather-grey sweatpants, barefoot, the navy hoodie unzipped over it on cold nights, SHOT: extreme close-up of a smartphone lying face-up on a wooden nightstand, the phone in the upper-middle of the vertical frame, a sleeping couple in the bed behind it completely out of focus as soft dark shapes. the phone screen has just lit up and casts cold blue-white light on the nightstand surface and on a glass of water, the screen content itself is a plain glowing rectangle (UI will be added in post), the couple breathes peacefully under grey linen bedding, everything else in blue-black darkness
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, extreme close-up of a smartphone lying face-up on a wooden nightstand, the phone in the upper-middle of the vertical frame, a sleeping couple in the bed behind it completely out of focus as soft dark shapes, the phone screen has just lit up and casts cold blue-white light on the nightstand surface and on a glass of water, the screen content itself is a plain glowing rectangle (UI will be added in post), the couple breathes peacefully under grey linen bedding, everything else in blue-black darkness, location L06 T-GECE (location reference L06-MASTER), characters: AYLA (character reference AYLA-REF-01, outfit A-GECE); MERT (character reference MERT-REF-01, outfit M-GECE)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes, readable text on phone screen, visible logos
```
**ANİMASYON PROMPTU (image-to-video)**
```text
the phone screen lights up from black to cold blue-white over 0.3 seconds; very subtle breathing motion of the blurred sleepers in the background; light from the screen gently spills on the nightstand; no other movement. Duration 4 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: static, then 2% push-in over 4s
```
- **Kamera:** Sabit. Ekran yanınca %2 ileri kayma (dolly-in), 4 sn boyunca. · static, then 2% push-in over 4s
- **Teknik:** Görsel + After Effects: ekran ışığı ayrı katman (opacity animasyonu), arka plan nefes için hafif ölçek (101%) döngüsü. UI grafiği montajda.
- **Montaj grafiği:** Bildirim kartı: Termostat · 03:10 · Manuel ayar · 22°C → 23°C

---

## B1-S02  ·  S2  ·  0:04–0:09  ·  5 sn

Mekân `L03` · `T-GECE-0310` · Eşya/ref `P-03`

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L03: a narrow 7 m long, 1.2 m wide entrance corridor in an old Istanbul apartment, freshly painted off-white walls, worn oak herringbone parquet floor, dark walnut front door at the west end with two locks, the first 3.4 m of the corridor has a LOWERED CEILING at 2.10 m (a built-in loft above), then the ceiling rises to 3.10 m with a visible beam line, in the lowered ceiling a nearly invisible 60x60 cm square hatch painted the same white as the ceiling with a faint grey soot shadow along its edges, directly below the hatch against the LEFT (north) wall a light oak shoe cabinet 90 cm tall with a small ceramic key bowl on top, a small square white digital wall thermostat on the left wall at 1.5 m height, on the RIGHT (south) wall near the entrance a built-in white louvered closet door hiding a combi boiler, next to it a white bathroom door with frosted glass, on the left wall a double glazed door to the living room, at the far east end a closed white door, 3:10 AM, all lights off, the ONLY light is the cold blue-white glow of the thermostat display on the wall and faint cold street light leaking from the living room, the hatch above is a dark square edge barely visible, deep blue-black shadows, square white digital wall thermostat with a blue-white backlit display showing "23°C", SHOT: wide shot at eye level from the far east end of the corridor looking west toward the front door, the thermostat on the LEFT wall in the left-middle of the frame. the thermostat display glowing blue-white is the main light source, the light oak shoe cabinet stands against the left wall in the middle of the corridor directly under the lowered ceiling, the hatch edge in the lowered ceiling is barely perceptible and must not draw attention, the louvered boiler closet and bathroom door on the right wall in deep shadow, faint cold street light leaking through the frosted glass of the living room door on the left
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, wide shot at eye level from the far east end of the corridor looking west toward the front door, the thermostat on the LEFT wall in the left-middle of the frame, the thermostat display glowing blue-white is the main light source, the light oak shoe cabinet stands against the left wall in the middle of the corridor directly under the lowered ceiling, the hatch edge in the lowered ceiling is barely perceptible and must not draw attention, the louvered boiler closet and bathroom door on the right wall in deep shadow, faint cold street light leaking through the frosted glass of the living room door on the left, location L03 T-GECE-0310 (location reference L03-MASTER)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes, people, figures, silhouettes, open hatch
```
**ANİMASYON PROMPTU (image-to-video)**
```text
almost no motion; the thermostat display glow pulses imperceptibly; faint dust particles drift in the thermostat light; the whole image slowly pushes toward the thermostat. Duration 5 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: very slow dolly-in toward the thermostat, 6% over 5s
```
- **Kamera:** Termostata doğru çok yavaş ileri kayma, 5 sn'de %6. · very slow dolly-in toward the thermostat, 6% over 5s
- **Teknik:** Görsel + 2.5D parallax (ön plan duvarlar / orta plan ayakkabılık / arka plan kapı ayrı katmanlar). Toz partikülü AE'de.
- **Montaj grafiği:** Son 1,5 sn sonrası: beyaza kesme, başlık kartı YEDEK ANAHTAR (ayrı grafik, bkz. B1-S02-T)

---

## B1-S02-T  ·  S2  ·  0:08,5–0:09  ·  1.5 sn

**GRAFİK (görsel üretimi yok):** Beyaz zemin (#E8E4DC), ortada ince, aralıklı (tracking +200) gri (#5C6773) büyük harfler: YEDEK ANAHTAR. Animasyon yok, sert giriş ve sert çıkış.

---

## B1-S03  ·  S3  ·  0:09–0:17  ·  8 sn

Mekân `L01` · `T-GÜN` · Karakter `AYLA` (A-DIŞ), `MERT` (M-EV)

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L01: a narrow Istanbul back street with worn cobblestones, 5 meters wide, cars parked on both sides, a 1978 four-storey concrete apartment building with dirty cream plaster facade, four windows per floor, small mosaic sign "IHLAMUR APT. 1978" above a heavy dark wooden entrance door with frosted glass, terracotta tiled pitched roof with a small dormer, old black electrical cables crossing the street, across the street similar aging buildings and a closed corner shop with its metal shutter down and a faded ghost outline of an old sign, cold white LED street lamp on a wall bracket, overcast grey November daylight, flat soft light, wet cobblestones, muted colors, AYLA DEMIR, a 30-year-old Turkish woman, 166 cm tall, slim average build, slightly tense posture with shoulders turned inward, oval face with a gently pointed chin and defined cheekbones, hazel-brown eyes, natural thick eyebrows, small mole under her LEFT eye, light warm olive skin, faint under-eye shadows, dark chestnut-brown shoulder-length wavy hair tied in a loose low messy bun with a graphite pencil stuck through it, two loose strands falling at the front of her face, thin silver ring on right index finger, thin gold wedding band on left ring finger, faint grey ink smudges on the fingertips of her right hand, observant cautious expression, wearing long dark olive-green hooded parka with fur-free hood, the ochre-mustard cardigan visible underneath at the collar, dark charcoal trousers, worn black leather ankle boots, black canvas tote bag, MERT DEMIR, a 33-year-old Turkish man, 181 cm tall, broad shoulders, athletic build gone slightly soft, square jaw, strong straight nose, thick dark eyebrows with a thin old scar cutting vertically through the middle of his RIGHT eyebrow leaving a small gap, dark brown eyes, medium warm olive skin, short 4-day black stubble, black hair short on the sides and 4-5 cm on top, pushed back by hand, slightly messy, steel-bracelet wristwatch on left wrist, gold wedding band on left ring finger, restless guarded expression, wearing dark navy hoodie (#1F2A44) with no print, heather-grey sweatpants, black house slippers, SHOT: tall vertical wide shot from across the street, slight low angle, the two characters small in the lower third of the frame, the full four-storey building facade above them reaching to the top of the frame. moving day: MERT, also wearing his dark navy wool overcoat over the hoodie, carries a large cardboard moving box toward the entrance door, AYLA stands holding a potted plant and looks up at the top floor, a few cardboard boxes on the wet cobblestones, the top floor windows on the LEFT half of the facade are dark and curtainless, the corner shop across with its shutter down
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, tall vertical wide shot from across the street, slight low angle, the two characters small in the lower third of the frame, the full four-storey building facade above them reaching to the top of the frame, moving day: MERT, also wearing his dark navy wool overcoat over the hoodie, carries a large cardboard moving box toward the entrance door, AYLA stands holding a potted plant and looks up at the top floor, a few cardboard boxes on the wet cobblestones, the top floor windows on the LEFT half of the facade are dark and curtainless, the corner shop across with its shutter down, location L01 T-GÜN (location reference L01-MASTER), characters: AYLA (character reference AYLA-REF-01, outfit A-DIŞ); MERT (character reference MERT-REF-01, outfit M-EV)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes, moving truck logo, readable shop sign, crowds
```
**ANİMASYON PROMPTU (image-to-video)**
```text
Mert walks two steps toward the door carrying the box; Ayla slowly raises her head to look up at the top floor; a gull crosses the sky; light drizzle. Duration 8 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: slow tilt up from characters to top-floor left windows over 8s
```
- **Kamera:** Yavaş yukarı tilt: alt üçte birdeki karakterlerden en üst kattaki sol pencerelere, 8 sn. · slow tilt up from characters to top-floor left windows over 8s
- **Teknik:** Uzun dikey görsel (1080×3200 eşdeğeri) üretip AE'de yukarı kaydırma (tilt simülasyonu). Karakterler ayrı katmanda, sınırlı animasyon (yürüyüş 2 poz döngüsü, baş kaldırma 3 ara kare).
- **Montaj grafiği:** Sol üst, küçük: 5 gün önce

---

## B1-S04a  ·  S4  ·  0:17–0:21  ·  4 sn

Mekân `L02` · `T-IŞIK-AÇIK` · Karakter `AYLA` (A-DIŞ) · Eşya/ref `P-01`

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L02: narrow apartment stairwell of an old 1970s Istanbul building, terrazzo mosaic stairs 1.1 m wide, black wrought-iron railing with a worn wooden handrail, walls painted dark green oil paint up to waist height and dirty cream above, third-floor landing 2.2 x 2 m with two facing dark walnut apartment doors, door "8" on the west side and door "7" on the east side, brass door numbers, a doormat in front of each, a small timer light switch glowing red, eight more steps rising to a narrow upper platform with a small grey metal attic door 0.8 x 1.2 m with rusty hinges, bare yellowish-white bulb on the ceiling, harsh top light, deep shadows under the stairs, AYLA DEMIR, a 30-year-old Turkish woman, 166 cm tall, slim average build, slightly tense posture with shoulders turned inward, oval face with a gently pointed chin and defined cheekbones, hazel-brown eyes, natural thick eyebrows, small mole under her LEFT eye, light warm olive skin, faint under-eye shadows, dark chestnut-brown shoulder-length wavy hair tied in a loose low messy bun with a graphite pencil stuck through it, two loose strands falling at the front of her face, thin silver ring on right index finger, thin gold wedding band on left ring finger, faint grey ink smudges on the fingertips of her right hand, observant cautious expression, wearing long dark olive-green hooded parka with fur-free hood, the ochre-mustard cardigan visible underneath at the collar, dark charcoal trousers, worn black leather ankle boots, black canvas tote bag, a simple steel key ring with three keys: a long silver building door key, a modern silver cylinder apartment key, and an old worn brass key stamped with tiny letters "SARI ANAHTAR", SHOT: insert close-up from above of AYLA's open right palm (silver ring on index finger, ink smudges on fingertips) receiving a key ring from an older man's hand entering from the top of the frame (only HIKMET's hand and beige trench coat cuff visible, gold signet ring on his LEFT little finger). the three keys rest in her palm, the old worn brass key on top, the tiny stamped letters on it catch the light but are not emphasized, background is the blurred terrazzo landing
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, insert close-up from above of AYLA's open right palm (silver ring on index finger, ink smudges on fingertips) receiving a key ring from an older man's hand entering from the top of the frame (only HIKMET's hand and beige trench coat cuff visible, gold signet ring on his LEFT little finger), the three keys rest in her palm, the old worn brass key on top, the tiny stamped letters on it catch the light but are not emphasized, background is the blurred terrazzo landing, location L02 T-IŞIK-AÇIK (location reference L02-MASTER), characters: AYLA (character reference AYLA-REF-01, outfit A-DIŞ)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes, extra fingers, wrong hand, readable large text
```
**ANİMASYON PROMPTU (image-to-video)**
```text
the man's hand releases the keys which settle into her palm with a small bounce; her thumb slowly turns the brass key once; his hand withdraws upward. Duration 4 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: static
```
- **Kamera:** Sabit. · static
- **Teknik:** El animasyonu elle ara kare (6–8 kare). Kenan dışı karakter elleri yine de 03c el kuralıyla kontrol edilecek.

---

## B1-S04b  ·  S4  ·  0:21–0:26  ·  5 sn

Mekân `L02` · `T-IŞIK-AÇIK` · Karakter `HİKMET` (H-ANA)

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L02: narrow apartment stairwell of an old 1970s Istanbul building, terrazzo mosaic stairs 1.1 m wide, black wrought-iron railing with a worn wooden handrail, walls painted dark green oil paint up to waist height and dirty cream above, third-floor landing 2.2 x 2 m with two facing dark walnut apartment doors, door "8" on the west side and door "7" on the east side, brass door numbers, a doormat in front of each, a small timer light switch glowing red, eight more steps rising to a narrow upper platform with a small grey metal attic door 0.8 x 1.2 m with rusty hinges, bare yellowish-white bulb on the ceiling, harsh top light, deep shadows under the stairs, HIKMET AKSOY, a 61-year-old Turkish man, 172 cm tall, stocky heavy build with a round belly and thick neck, round face with heavy jowls and full cheeks, small narrow dark brown eyes, thick well-groomed grey moustache, balding on top with grey side hair neatly combed over, ruddy pinkish complexion especially on the nose and cheeks, a string of dark matte amber prayer beads (tespih) always held in his right hand, a gold signet ring on his left little finger, polite closed-lip smile that does not reach his eyes, avoiding eye contact, wearing beige knee-length trench coat (#BFAE8E) belted loosely, brown wool V-neck sweater over a white collared shirt, grey pressed trousers, polished black leather shoes, folded reading glasses in the breast pocket, SHOT: medium close-up of HIKMET framed on the right side of the vertical frame, his eyes NOT looking at the camera or at Ayla but at the door frame of apartment 7 beside him. his polite closed-lip smile, prayer beads in his RIGHT hand at chest height, harsh bare bulb top light leaving his eye sockets in shadow, dark green lower wall behind him
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, medium close-up of HIKMET framed on the right side of the vertical frame, his eyes NOT looking at the camera or at Ayla but at the door frame of apartment 7 beside him, his polite closed-lip smile, prayer beads in his RIGHT hand at chest height, harsh bare bulb top light leaving his eye sockets in shadow, dark green lower wall behind him, location L02 T-IŞIK-AÇIK (location reference L02-MASTER), characters: HİKMET (character reference HIKMET-REF-01, outfit H-ANA)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes, looking at camera, warm friendly expression
```
**ANİMASYON PROMPTU (image-to-video)**
```text
his lips move for a short line (4 words); the prayer beads click forward one by one in his right hand; his eyes shift once toward the door frame; very slight handheld drift. Duration 5 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: very slight handheld drift
```
- **Kamera:** Çok hafif el kamerası titreşimi (±0,5%). · very slight handheld drift
- **Teknik:** Dudak senkronu: 'Alttakini boş verin. Eski.' (2 sn). Tespih: 4 kare döngü.

---

## B1-S05a  ·  S5  ·  0:26–0:30  ·  4 sn

Mekân `L02` · `T-IŞIK-AÇIK` · Karakter `AYLA` (A-DIŞ)

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L02: narrow apartment stairwell of an old 1970s Istanbul building, terrazzo mosaic stairs 1.1 m wide, black wrought-iron railing with a worn wooden handrail, walls painted dark green oil paint up to waist height and dirty cream above, third-floor landing 2.2 x 2 m with two facing dark walnut apartment doors, door "8" on the west side and door "7" on the east side, brass door numbers, a doormat in front of each, a small timer light switch glowing red, eight more steps rising to a narrow upper platform with a small grey metal attic door 0.8 x 1.2 m with rusty hinges, bare yellowish-white bulb on the ceiling, harsh top light, deep shadows under the stairs, AYLA DEMIR, a 30-year-old Turkish woman, 166 cm tall, slim average build, slightly tense posture with shoulders turned inward, oval face with a gently pointed chin and defined cheekbones, hazel-brown eyes, natural thick eyebrows, small mole under her LEFT eye, light warm olive skin, faint under-eye shadows, dark chestnut-brown shoulder-length wavy hair tied in a loose low messy bun with a graphite pencil stuck through it, two loose strands falling at the front of her face, thin silver ring on right index finger, thin gold wedding band on left ring finger, faint grey ink smudges on the fingertips of her right hand, observant cautious expression, wearing long dark olive-green hooded parka with fur-free hood, the ochre-mustard cardigan visible underneath at the collar, dark charcoal trousers, worn black leather ankle boots, black canvas tote bag, SHOT: over-the-shoulder shot from behind AYLA (back of her head and parka hood in the left foreground, out of focus) toward the door of apartment 8 across the landing. the dark walnut door marked 8 is open only a few centimeters, held by a brass door chain, through the narrow gap warm honey-yellow light from inside spills onto the cold landing
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, over-the-shoulder shot from behind AYLA (back of her head and parka hood in the left foreground, out of focus) toward the door of apartment 8 across the landing, the dark walnut door marked 8 is open only a few centimeters, held by a brass door chain, through the narrow gap warm honey-yellow light from inside spills onto the cold landing, location L02 T-IŞIK-AÇIK (location reference L02-MASTER), characters: AYLA (character reference AYLA-REF-01, outfit A-DIŞ)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes, door wide open
```
**ANİMASYON PROMPTU (image-to-video)**
```text
Ayla turns her head slightly toward the door; the warm light in the gap flickers subtly. Duration 4 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: slow push-in toward the door gap
```
- **Kamera:** Kapı aralığına doğru çok yavaş ileri kayma, %4. · slow push-in toward the door gap
- **Teknik:** 2.5D: Ayla ön plan katmanı, kapı arka plan.

---

## B1-S05b  ·  S5  ·  0:30–0:35  ·  5 sn

Mekân `L02` · `T-IŞIK-AÇIK` · Karakter `SAADET` (S-EV)

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L02: narrow apartment stairwell of an old 1970s Istanbul building, terrazzo mosaic stairs 1.1 m wide, black wrought-iron railing with a worn wooden handrail, walls painted dark green oil paint up to waist height and dirty cream above, third-floor landing 2.2 x 2 m with two facing dark walnut apartment doors, door "8" on the west side and door "7" on the east side, brass door numbers, a doormat in front of each, a small timer light switch glowing red, eight more steps rising to a narrow upper platform with a small grey metal attic door 0.8 x 1.2 m with rusty hinges, bare yellowish-white bulb on the ceiling, harsh top light, deep shadows under the stairs, SAADET UNAL, a 73-year-old Turkish woman, 155 cm tall, short round plump build, slightly hunched but holding herself upright, round deeply wrinkled face with downturned lines at the corners of her mouth, stern but soft expression, light brown eyes magnified behind thick-lensed brown tortoiseshell glasses hanging on a beaded chain, white-grey hair pulled tightly into a low bun at the nape held with black hairpins, fair skin with age spots on her hands and forehead, a yellow tailor's measuring tape draped around her neck, one thin gold bangle on her right wrist, watchful silent expression, wearing dark bottle-green hand-knitted wool vest (#2F4A3A) buttoned over a cream long-sleeve blouse with a small round collar, long dark grey A-line wool skirt below the knee, thick brown opaque stockings, worn brown felt house slippers, SHOT: close-up through the chained door gap: only a vertical strip of SAADET's face is visible — one eye magnified behind a thick glasses lens, part of her wrinkled cheek, the yellow measuring tape at her neck, the brass chain crossing the frame. she does not smile, her gaze is steady and heavy, warm yellow light behind her, the cold landing light on the door edge
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, close-up through the chained door gap: only a vertical strip of SAADET's face is visible — one eye magnified behind a thick glasses lens, part of her wrinkled cheek, the yellow measuring tape at her neck, the brass chain crossing the frame, she does not smile, her gaze is steady and heavy, warm yellow light behind her, the cold landing light on the door edge, location L02 T-IŞIK-AÇIK (location reference L02-MASTER), characters: SAADET (character reference SAADET-REF-01, outfit S-EV)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes, smiling, full face visible
```
**ANİMASYON PROMPTU (image-to-video)**
```text
her lips move for one short sentence (7 words); after the line the door slowly closes and the strip of face disappears into the dark wood. Duration 5 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: static
```
- **Kamera:** Sabit. · static
- **Teknik:** Dudak senkronu: 'Kaloriferi kısma kızım. Bu ev soğuğu sevmez.' (3 sn). Kapı kapanışı: kapı katmanının 1,5 sn yatay kayması.

---

## B1-S06a  ·  S6  ·  0:35–0:39  ·  4 sn

Mekân `L04` · `T-GÜN` · Karakter `AYLA` (A-EV)

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L04: a spacious old Istanbul living room 5.6 x 4.9 m with 3.10 m high ceilings and simple plaster crown molding, two tall windows on the north wall facing the street with white sheer curtains and heavy dark grey drapes, worn oak herringbone parquet with FOUR FAINT DARK DENTED MARKS in front of the bookshelf where an old armchair stood for years, a tall white bookshelf along the west wall half filled with books and half with unopened moving boxes, a wall clock on top, an old bottle-green velvet armchair, a grey fabric sofa against the east wall, a low walnut coffee table, a large monstera plant by the window, unhung picture frames leaning against the wall, a white panel radiator under each window, flat overcast daylight through sheer curtains, dust in the air, muted greens and greys, AYLA DEMIR, a 30-year-old Turkish woman, 166 cm tall, slim average build, slightly tense posture with shoulders turned inward, oval face with a gently pointed chin and defined cheekbones, hazel-brown eyes, natural thick eyebrows, small mole under her LEFT eye, light warm olive skin, faint under-eye shadows, dark chestnut-brown shoulder-length wavy hair tied in a loose low messy bun with a graphite pencil stuck through it, two loose strands falling at the front of her face, thin silver ring on right index finger, thin gold wedding band on left ring finger, faint grey ink smudges on the fingertips of her right hand, observant cautious expression, wearing oversized muted ochre-mustard chunky knit cardigan (#B8913A) with large wooden buttons, plain off-white cotton t-shirt, loose dark charcoal-grey wide-leg trousers, thick grey wool socks, no shoes, SHOT: wide shot of the living room from the corridor doorway, the north windows at the back of the frame. moving boxes everywhere, AYLA pushes the bottle-green velvet armchair into place IN FRONT OF THE WINDOW, the four faded dark dents in the parquet in front of the bookshelf on the west wall are visible at the bottom edge of the frame but NOT emphasized
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, wide shot of the living room from the corridor doorway, the north windows at the back of the frame, moving boxes everywhere, AYLA pushes the bottle-green velvet armchair into place IN FRONT OF THE WINDOW, the four faded dark dents in the parquet in front of the bookshelf on the west wall are visible at the bottom edge of the frame but NOT emphasized, location L04 T-GÜN (location reference L04-MASTER), characters: AYLA (character reference AYLA-REF-01, outfit A-EV)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes, armchair in front of the bookshelf
```
**ANİMASYON PROMPTU (image-to-video)**
```text
Ayla gives the armchair a final push and steps back to look at it; dust in the window light. Duration 4 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: static
```
- **Kamera:** Sabit. · static
- **Teknik:** Sınırlı animasyon: itme 4 poz.

---

## B1-S06b  ·  S6  ·  0:39–0:42  ·  3 sn

Mekân `L04` · `T-GÜN` · Karakter `MERT` (M-EV)

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L04: a spacious old Istanbul living room 5.6 x 4.9 m with 3.10 m high ceilings and simple plaster crown molding, two tall windows on the north wall facing the street with white sheer curtains and heavy dark grey drapes, worn oak herringbone parquet with FOUR FAINT DARK DENTED MARKS in front of the bookshelf where an old armchair stood for years, a tall white bookshelf along the west wall half filled with books and half with unopened moving boxes, a wall clock on top, an old bottle-green velvet armchair, a grey fabric sofa against the east wall, a low walnut coffee table, a large monstera plant by the window, unhung picture frames leaning against the wall, a white panel radiator under each window, flat overcast daylight through sheer curtains, dust in the air, muted greens and greys, MERT DEMIR, a 33-year-old Turkish man, 181 cm tall, broad shoulders, athletic build gone slightly soft, square jaw, strong straight nose, thick dark eyebrows with a thin old scar cutting vertically through the middle of his RIGHT eyebrow leaving a small gap, dark brown eyes, medium warm olive skin, short 4-day black stubble, black hair short on the sides and 4-5 cm on top, pushed back by hand, slightly messy, steel-bracelet wristwatch on left wrist, gold wedding band on left ring finger, restless guarded expression, wearing dark navy hoodie (#1F2A44) with no print, heather-grey sweatpants, black house slippers, SHOT: medium shot of MERT kneeling by the bookshelf with a cordless drill, profile view. he concentrates on fixing a shelf bracket, screws between his lips, boxes around him
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, medium shot of MERT kneeling by the bookshelf with a cordless drill, profile view, he concentrates on fixing a shelf bracket, screws between his lips, boxes around him, location L04 T-GÜN (location reference L04-MASTER), characters: MERT (character reference MERT-REF-01, outfit M-EV)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes
```
**ANİMASYON PROMPTU (image-to-video)**
```text
the drill spins briefly; Mert adjusts the bracket. Duration 3 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: static
```
- **Kamera:** Sabit. · static
- **Teknik:** Sınırlı animasyon.

---

## B1-S06c  ·  S6  ·  0:42–0:45  ·  3 sn

Mekân `L05` · `T-GÜN` · Karakter `AYLA` (A-EV), `MERT` (M-İŞ)

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L05: a small narrow Istanbul kitchen 3.6 x 2.4 m, old white laminate cabinets with brushed metal handles, new grey stone-look countertop, white subway tile backsplash, a south-facing window above a small square table with two wooden chairs looking onto a grey inner courtyard, an older white refrigerator on the east wall, a cream ceramic mug with a thin navy rim and a cracked handle on the counter, pale overcast light from the courtyard window, quiet, AYLA DEMIR, a 30-year-old Turkish woman, 166 cm tall, slim average build, slightly tense posture with shoulders turned inward, oval face with a gently pointed chin and defined cheekbones, hazel-brown eyes, natural thick eyebrows, small mole under her LEFT eye, light warm olive skin, faint under-eye shadows, dark chestnut-brown shoulder-length wavy hair tied in a loose low messy bun with a graphite pencil stuck through it, two loose strands falling at the front of her face, thin silver ring on right index finger, thin gold wedding band on left ring finger, faint grey ink smudges on the fingertips of her right hand, observant cautious expression, wearing oversized muted ochre-mustard chunky knit cardigan (#B8913A) with large wooden buttons, plain off-white cotton t-shirt, loose dark charcoal-grey wide-leg trousers, thick grey wool socks, no shoes, MERT DEMIR, a 33-year-old Turkish man, 181 cm tall, broad shoulders, athletic build gone slightly soft, square jaw, strong straight nose, thick dark eyebrows with a thin old scar cutting vertically through the middle of his RIGHT eyebrow leaving a small gap, dark brown eyes, medium warm olive skin, short 4-day black stubble, black hair short on the sides and 4-5 cm on top, pushed back by hand, slightly messy, steel-bracelet wristwatch on left wrist, gold wedding band on left ring finger, restless guarded expression, wearing dark navy wool overcoat (#1F2A44) knee length, light grey button-up shirt with no tie, dark charcoal chinos, brown leather derby shoes, black laptop backpack, SHOT: medium close-up two-shot in the kitchen in the early morning, both standing at the counter. AYLA presses two fingers against her temple with her eyes squinting, MERT dressed for 'work' drinks a glass of water and rubs his forehead, both look tired, cold grey morning light from the courtyard window
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, medium close-up two-shot in the kitchen in the early morning, both standing at the counter, AYLA presses two fingers against her temple with her eyes squinting, MERT dressed for 'work' drinks a glass of water and rubs his forehead, both look tired, cold grey morning light from the courtyard window, location L05 T-GÜN (location reference L05-MASTER), characters: AYLA (character reference AYLA-REF-01, outfit A-EV); MERT (character reference MERT-REF-01, outfit M-İŞ)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes, smiling, energetic
```
**ANİMASYON PROMPTU (image-to-video)**
```text
Ayla rubs her temple in a slow circle; Mert lowers the glass and speaks two words. Duration 3 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: static
```
- **Kamera:** Sabit. · static
- **Teknik:** Dudak senkronu (Mert): 'Boya kokusu.' (1 sn).

---

## B1-S07a  ·  S7  ·  0:45–0:49  ·  4 sn

Mekân `L05` · `T-GÜN` · Eşya/ref `P-02`

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L05: a small narrow Istanbul kitchen 3.6 x 2.4 m, old white laminate cabinets with brushed metal handles, new grey stone-look countertop, white subway tile backsplash, a south-facing window above a small square table with two wooden chairs looking onto a grey inner courtyard, an older white refrigerator on the east wall, a cream ceramic mug with a thin navy rim and a cracked handle on the counter, pale overcast light from the courtyard window, quiet, cream ceramic mug with a thin navy blue rim and a hairline crack on the handle, SHOT: insert shot of the mug on the grey countertop, centered, at counter height. the cream mug with the thin navy rim has its cracked handle pointing to the LEFT, pale overcast morning light from the window, white subway tiles out of focus behind
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, insert shot of the mug on the grey countertop, centered, at counter height, the cream mug with the thin navy rim has its cracked handle pointing to the LEFT, pale overcast morning light from the window, white subway tiles out of focus behind, location L05 T-GÜN (location reference L05-MASTER)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes, handle pointing right, hands
```
**ANİMASYON PROMPTU (image-to-video)**
```text
completely still; only the faint drifting light of passing clouds. Duration 4 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: static
```
- **Kamera:** Sabit. · static
- **Teknik:** Tek görsel, hafif ışık animasyonu.

---

## B1-S07b  ·  S7  ·  0:49–0:52  ·  3 sn

Eşya/ref `P-04`

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, black A5 hardcover sketchbook with an elastic band, pages of precise pencil drawings of an apartment interior, SHOT: full-frame insert of an open sketchbook page, top-down. a precise pencil drawing of the same kitchen counter from yesterday, the same mug drawn with its handle pointing to the RIGHT, small handwritten date in the corner (illegible), clean graphite linework on off-white paper
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, full-frame insert of an open sketchbook page, top-down, a precise pencil drawing of the same kitchen counter from yesterday, the same mug drawn with its handle pointing to the RIGHT, small handwritten date in the corner (illegible), clean graphite linework on off-white paper
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes, handle pointing left, colored drawing, readable text
```
**ANİMASYON PROMPTU (image-to-video)**
```text
still; a tiny flutter of the page edge. Duration 3 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: static
```
- **Kamera:** Sabit. · static
- **Teknik:** Çizim bölümü gerçek kurşun kalem dokusunda (Ayla'nın çizim stili: temiz, mimari). Tarih grafiği montajda.

---

## B1-S07c  ·  S7  ·  0:52–0:55  ·  3 sn

Mekân `L05` · `T-GÜN` · Karakter `AYLA` (A-EV) · Eşya/ref `P-02`

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L05: a small narrow Istanbul kitchen 3.6 x 2.4 m, old white laminate cabinets with brushed metal handles, new grey stone-look countertop, white subway tile backsplash, a south-facing window above a small square table with two wooden chairs looking onto a grey inner courtyard, an older white refrigerator on the east wall, a cream ceramic mug with a thin navy rim and a cracked handle on the counter, pale overcast light from the courtyard window, quiet, AYLA DEMIR, a 30-year-old Turkish woman, 166 cm tall, slim average build, slightly tense posture with shoulders turned inward, oval face with a gently pointed chin and defined cheekbones, hazel-brown eyes, natural thick eyebrows, small mole under her LEFT eye, light warm olive skin, faint under-eye shadows, dark chestnut-brown shoulder-length wavy hair tied in a loose low messy bun with a graphite pencil stuck through it, two loose strands falling at the front of her face, thin silver ring on right index finger, thin gold wedding band on left ring finger, faint grey ink smudges on the fingertips of her right hand, observant cautious expression, wearing oversized muted ochre-mustard chunky knit cardigan (#B8913A) with large wooden buttons, plain off-white cotton t-shirt, loose dark charcoal-grey wide-leg trousers, thick grey wool socks, no shoes, cream ceramic mug with a thin navy blue rim and a hairline crack on the handle, SHOT: close-up of AYLA's right hand (silver ring, ink smudges) turning the mug handle back to the right. only the hand, the cardigan sleeve cuff and the mug in frame, the hand stops and rests on the mug for a moment
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, close-up of AYLA's right hand (silver ring, ink smudges) turning the mug handle back to the right, only the hand, the cardigan sleeve cuff and the mug in frame, the hand stops and rests on the mug for a moment, location L05 T-GÜN (location reference L05-MASTER), characters: AYLA (character reference AYLA-REF-01, outfit A-EV)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes, extra fingers
```
**ANİMASYON PROMPTU (image-to-video)**
```text
the hand rotates the mug 180 degrees smoothly, then rests still for one second. Duration 3 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: slight follow pan
```
- **Kamera:** Elin hareketini izleyen hafif yatay kayma. · slight follow pan
- **Teknik:** Elle ara kare (8 kare).

---

## B1-S08a  ·  S8  ·  0:55–1:00  ·  5 sn

Mekân `L03` · `T-GÜN` · Karakter `AYLA` (A-EV), `MERT` (M-İŞ)

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L03: a narrow 7 m long, 1.2 m wide entrance corridor in an old Istanbul apartment, freshly painted off-white walls, worn oak herringbone parquet floor, dark walnut front door at the west end with two locks, the first 3.4 m of the corridor has a LOWERED CEILING at 2.10 m (a built-in loft above), then the ceiling rises to 3.10 m with a visible beam line, in the lowered ceiling a nearly invisible 60x60 cm square hatch painted the same white as the ceiling with a faint grey soot shadow along its edges, directly below the hatch against the LEFT (north) wall a light oak shoe cabinet 90 cm tall with a small ceramic key bowl on top, a small square white digital wall thermostat on the left wall at 1.5 m height, on the RIGHT (south) wall near the entrance a built-in white louvered closet door hiding a combi boiler, next to it a white bathroom door with frosted glass, on the left wall a double glazed door to the living room, at the far east end a closed white door, soft grey daylight spilling from the open living room door, ceiling light off, calm, AYLA DEMIR, a 30-year-old Turkish woman, 166 cm tall, slim average build, slightly tense posture with shoulders turned inward, oval face with a gently pointed chin and defined cheekbones, hazel-brown eyes, natural thick eyebrows, small mole under her LEFT eye, light warm olive skin, faint under-eye shadows, dark chestnut-brown shoulder-length wavy hair tied in a loose low messy bun with a graphite pencil stuck through it, two loose strands falling at the front of her face, thin silver ring on right index finger, thin gold wedding band on left ring finger, faint grey ink smudges on the fingertips of her right hand, observant cautious expression, wearing oversized muted ochre-mustard chunky knit cardigan (#B8913A) with large wooden buttons, plain off-white cotton t-shirt, loose dark charcoal-grey wide-leg trousers, thick grey wool socks, no shoes, MERT DEMIR, a 33-year-old Turkish man, 181 cm tall, broad shoulders, athletic build gone slightly soft, square jaw, strong straight nose, thick dark eyebrows with a thin old scar cutting vertically through the middle of his RIGHT eyebrow leaving a small gap, dark brown eyes, medium warm olive skin, short 4-day black stubble, black hair short on the sides and 4-5 cm on top, pushed back by hand, slightly messy, steel-bracelet wristwatch on left wrist, gold wedding band on left ring finger, restless guarded expression, wearing dark navy wool overcoat (#1F2A44) knee length, light grey button-up shirt with no tie, dark charcoal chinos, brown leather derby shoes, black laptop backpack, SHOT: wide shot from the front door looking east down the corridor. the light oak shoe cabinet has been dragged from beside the door to the middle of the corridor against the LEFT (north) wall, exactly under the lowered ceiling, AYLA stands next to it with one hand on its top, MERT in his navy overcoat and backpack walks past her toward the camera and the front door without looking at her, the thermostat on the left wall further back
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, wide shot from the front door looking east down the corridor, the light oak shoe cabinet has been dragged from beside the door to the middle of the corridor against the LEFT (north) wall, exactly under the lowered ceiling, AYLA stands next to it with one hand on its top, MERT in his navy overcoat and backpack walks past her toward the camera and the front door without looking at her, the thermostat on the left wall further back, location L03 T-GÜN (location reference L03-MASTER), characters: AYLA (character reference AYLA-REF-01, outfit A-EV); MERT (character reference MERT-REF-01, outfit M-İŞ)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes, visible hatch, open hatch
```
**ANİMASYON PROMPTU (image-to-video)**
```text
Mert walks toward camera and exits frame left at the door; Ayla stays still touching the cabinet; Mert's lips move for two words as he passes. Duration 5 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: static
```
- **Kamera:** Sabit. · static
- **Teknik:** Mert yürüyüşü 6 poz, dudak senkronu: 'Sen çekmişsindir.' (1 sn).

---

## B1-S08b  ·  S8  ·  1:00–1:03  ·  3 sn

Mekân `L03` · `T-GÜN`

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L03: a narrow 7 m long, 1.2 m wide entrance corridor in an old Istanbul apartment, freshly painted off-white walls, worn oak herringbone parquet floor, dark walnut front door at the west end with two locks, the first 3.4 m of the corridor has a LOWERED CEILING at 2.10 m (a built-in loft above), then the ceiling rises to 3.10 m with a visible beam line, in the lowered ceiling a nearly invisible 60x60 cm square hatch painted the same white as the ceiling with a faint grey soot shadow along its edges, directly below the hatch against the LEFT (north) wall a light oak shoe cabinet 90 cm tall with a small ceramic key bowl on top, a small square white digital wall thermostat on the left wall at 1.5 m height, on the RIGHT (south) wall near the entrance a built-in white louvered closet door hiding a combi boiler, next to it a white bathroom door with frosted glass, on the left wall a double glazed door to the living room, at the far east end a closed white door, soft grey daylight spilling from the open living room door, ceiling light off, calm, SHOT: insert of the oak herringbone parquet close to the floor. two fresh pale scrape lines in the parquet varnish lead from the entrance area to the base of the shoe cabinet
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, insert of the oak herringbone parquet close to the floor, two fresh pale scrape lines in the parquet varnish lead from the entrance area to the base of the shoe cabinet, location L03 T-GÜN (location reference L03-MASTER)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes, people, feet
```
**ANİMASYON PROMPTU (image-to-video)**
```text
still; dust settles in a thin light beam. Duration 3 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: static
```
- **Kamera:** Sabit. · static
- **Teknik:** Tek görsel.

---

## B1-S08c  ·  S8  ·  1:03–1:06  ·  3 sn

Mekân `L03` · `T-GÜN`

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L03: a narrow 7 m long, 1.2 m wide entrance corridor in an old Istanbul apartment, freshly painted off-white walls, worn oak herringbone parquet floor, dark walnut front door at the west end with two locks, the first 3.4 m of the corridor has a LOWERED CEILING at 2.10 m (a built-in loft above), then the ceiling rises to 3.10 m with a visible beam line, in the lowered ceiling a nearly invisible 60x60 cm square hatch painted the same white as the ceiling with a faint grey soot shadow along its edges, directly below the hatch against the LEFT (north) wall a light oak shoe cabinet 90 cm tall with a small ceramic key bowl on top, a small square white digital wall thermostat on the left wall at 1.5 m height, on the RIGHT (south) wall near the entrance a built-in white louvered closet door hiding a combi boiler, next to it a white bathroom door with frosted glass, on the left wall a double glazed door to the living room, at the far east end a closed white door, soft grey daylight spilling from the open living room door, ceiling light off, calm, SHOT: POV looking straight up at the low white corridor ceiling at 2.10 m. a plain white painted ceiling surface with a very faint, almost invisible square seam and the softest grey shadow along it, the beam line where the ceiling rises to 3.10 m at the top edge of frame
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, POV looking straight up at the low white corridor ceiling at 2.10 m, a plain white painted ceiling surface with a very faint, almost invisible square seam and the softest grey shadow along it, the beam line where the ceiling rises to 3.10 m at the top edge of frame, location L03 T-GÜN (location reference L03-MASTER)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes, obvious hatch, handle, dark square
```
**ANİMASYON PROMPTU (image-to-video)**
```text
the image tilts upward slowly from the wall to the ceiling and holds one beat too long on the ceiling. Duration 3 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: slow tilt up, hold on ceiling 1.5s
```
- **Kamera:** Yavaş yukarı tilt, tavanda 1,5 sn fazla kalma. · slow tilt up, hold on ceiling 1.5s
- **Teknik:** Duvar+tavan tek uzun görsel, AE'de dikey kaydırma.

---

## B1-S09a  ·  S9  ·  1:06–1:12  ·  6 sn

Mekân `L08` · Karakter `AYLA` (A-EV) · Eşya/ref `P-04`

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L08: a small 3 x 3.6 m study room with a south window onto the grey courtyard, a large wooden drawing desk with a desk lamp, scattered sketches of the apartment's rooms pinned to the wall in a grid, pencils, an open black sketchbook, a tablet stand, AYLA DEMIR, a 30-year-old Turkish woman, 166 cm tall, slim average build, slightly tense posture with shoulders turned inward, oval face with a gently pointed chin and defined cheekbones, hazel-brown eyes, natural thick eyebrows, small mole under her LEFT eye, light warm olive skin, faint under-eye shadows, dark chestnut-brown shoulder-length wavy hair tied in a loose low messy bun with a graphite pencil stuck through it, two loose strands falling at the front of her face, thin silver ring on right index finger, thin gold wedding band on left ring finger, faint grey ink smudges on the fingertips of her right hand, observant cautious expression, wearing oversized muted ochre-mustard chunky knit cardigan (#B8913A) with large wooden buttons, plain off-white cotton t-shirt, loose dark charcoal-grey wide-leg trousers, thick grey wool socks, no shoes, black A5 hardcover sketchbook with an elastic band, pages of precise pencil drawings of an apartment interior, SHOT: wide shot of the study wall covered with a grid of twelve pinned pencil sketches (four days × three rooms), AYLA at the right edge of the frame half turned away, wearing her round reading glasses. warm desk lamp light mixed with cold daylight from the south window, the sketches show the corridor, the kitchen and the living room from the same angles day after day
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, wide shot of the study wall covered with a grid of twelve pinned pencil sketches (four days × three rooms), AYLA at the right edge of the frame half turned away, wearing her round reading glasses, warm desk lamp light mixed with cold daylight from the south window, the sketches show the corridor, the kitchen and the living room from the same angles day after day, location L08 (location reference L08-MASTER), characters: AYLA (character reference AYLA-REF-01, outfit A-EV)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes, readable text, colorful drawings
```
**ANİMASYON PROMPTU (image-to-video)**
```text
slow lateral drift along the sketch wall; Ayla draws a red circle on one sketch. Duration 6 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: slow lateral pan across the wall
```
- **Kamera:** Duvar boyunca yavaş yatay kayma, 6 sn. · slow lateral pan across the wall
- **Teknik:** Geniş yatay görsel, AE'de kaydırma.

---

## B1-S09b  ·  S9  ·  1:12–1:17  ·  5 sn

Mekân `L08`

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L08: a small 3 x 3.6 m study room with a south window onto the grey courtyard, a large wooden drawing desk with a desk lamp, scattered sketches of the apartment's rooms pinned to the wall in a grid, pencils, an open black sketchbook, a tablet stand, SHOT: three quick inserts of individual sketches, each filling the frame. (1) the mug sketch with the handle circled in red pencil, (2) a chair pushed in under the table circled in red, (3) the shoe cabinet in the middle of the corridor circled in red
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, three quick inserts of individual sketches, each filling the frame, (1) the mug sketch with the handle circled in red pencil, (2) a chair pushed in under the table circled in red, (3) the shoe cabinet in the middle of the corridor circled in red, location L08 (location reference L08-MASTER)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes, readable text
```
**ANİMASYON PROMPTU (image-to-video)**
```text
each insert holds 1.6 seconds with a micro push-in. Duration 5 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: micro push-ins
```
- **Kamera:** Her insert'te mikro ileri kayma. · micro push-ins
- **Teknik:** 3 ayrı görsel (B1-S09b-1/2/3).

---

## B1-S10  ·  S10  ·  1:17–1:26  ·  9 sn

Mekân `L04` · `T-AKŞAM` · Karakter `AYLA` (A-EV), `MERT` (M-EV)

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L04: a spacious old Istanbul living room 5.6 x 4.9 m with 3.10 m high ceilings and simple plaster crown molding, two tall windows on the north wall facing the street with white sheer curtains and heavy dark grey drapes, worn oak herringbone parquet with FOUR FAINT DARK DENTED MARKS in front of the bookshelf where an old armchair stood for years, a tall white bookshelf along the west wall half filled with books and half with unopened moving boxes, a wall clock on top, an old bottle-green velvet armchair, a grey fabric sofa against the east wall, a low walnut coffee table, a large monstera plant by the window, unhung picture frames leaning against the wall, a white panel radiator under each window, single warm floor lamp in the corner, rest of the room in soft shadow, windows deep blue, AYLA DEMIR, a 30-year-old Turkish woman, 166 cm tall, slim average build, slightly tense posture with shoulders turned inward, oval face with a gently pointed chin and defined cheekbones, hazel-brown eyes, natural thick eyebrows, small mole under her LEFT eye, light warm olive skin, faint under-eye shadows, dark chestnut-brown shoulder-length wavy hair tied in a loose low messy bun with a graphite pencil stuck through it, two loose strands falling at the front of her face, thin silver ring on right index finger, thin gold wedding band on left ring finger, faint grey ink smudges on the fingertips of her right hand, observant cautious expression, wearing oversized muted ochre-mustard chunky knit cardigan (#B8913A) with large wooden buttons, plain off-white cotton t-shirt, loose dark charcoal-grey wide-leg trousers, thick grey wool socks, no shoes, MERT DEMIR, a 33-year-old Turkish man, 181 cm tall, broad shoulders, athletic build gone slightly soft, square jaw, strong straight nose, thick dark eyebrows with a thin old scar cutting vertically through the middle of his RIGHT eyebrow leaving a small gap, dark brown eyes, medium warm olive skin, short 4-day black stubble, black hair short on the sides and 4-5 cm on top, pushed back by hand, slightly messy, steel-bracelet wristwatch on left wrist, gold wedding band on left ring finger, restless guarded expression, wearing dark navy hoodie (#1F2A44) with no print, heather-grey sweatpants, black house slippers, SHOT: low angle close to the floor: AYLA on her knees in the foreground taping strips of painter's tape on the parquet around the legs of the green armchair in front of the window; MERT out of focus in the background on the sofa. Mert's face lit by his phone screen, the phone shows a blurry job listing website layout (unreadable), a single warm floor lamp, the windows deep blue behind
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, low angle close to the floor: AYLA on her knees in the foreground taping strips of painter's tape on the parquet around the legs of the green armchair in front of the window; MERT out of focus in the background on the sofa, Mert's face lit by his phone screen, the phone shows a blurry job listing website layout (unreadable), a single warm floor lamp, the windows deep blue behind, location L04 T-AKŞAM (location reference L04-MASTER), characters: AYLA (character reference AYLA-REF-01, outfit A-EV); MERT (character reference MERT-REF-01, outfit M-EV)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes, readable phone text, logos
```
**ANİMASYON PROMPTU (image-to-video)**
```text
Ayla tears and presses a strip of tape; Mert lifts his head, looks at her for a second as if to say something, then looks back at his phone; Ayla switches off the floor lamp and the room goes dark blue. Duration 9 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: static
```
- **Kamera:** Sabit. · static
- **Teknik:** Lamba kapanışı: iki ışık durumu görseli (AKŞAM → GECE), 2 karede geçiş.

---

## B1-S11  ·  S11  ·  1:26–1:33  ·  7 sn

Mekân `L03` · `T-GECE-0310` · Eşya/ref `P-03`

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L03: a narrow 7 m long, 1.2 m wide entrance corridor in an old Istanbul apartment, freshly painted off-white walls, worn oak herringbone parquet floor, dark walnut front door at the west end with two locks, the first 3.4 m of the corridor has a LOWERED CEILING at 2.10 m (a built-in loft above), then the ceiling rises to 3.10 m with a visible beam line, in the lowered ceiling a nearly invisible 60x60 cm square hatch painted the same white as the ceiling with a faint grey soot shadow along its edges, directly below the hatch against the LEFT (north) wall a light oak shoe cabinet 90 cm tall with a small ceramic key bowl on top, a small square white digital wall thermostat on the left wall at 1.5 m height, on the RIGHT (south) wall near the entrance a built-in white louvered closet door hiding a combi boiler, next to it a white bathroom door with frosted glass, on the left wall a double glazed door to the living room, at the far east end a closed white door, 3:10 AM, all lights off, the ONLY light is the cold blue-white glow of the thermostat display on the wall and faint cold street light leaking from the living room, the hatch above is a dark square edge barely visible, deep blue-black shadows, square white digital wall thermostat with a blue-white backlit display showing "23°C", SHOT: close-up of the thermostat display centered in the frame, everything around it pure black. the backlit display shows the digits, cold blue-white glow on a tiny area of wall
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, close-up of the thermostat display centered in the frame, everything around it pure black, the backlit display shows the digits, cold blue-white glow on a tiny area of wall, location L03 T-GECE-0310 (location reference L03-MASTER)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes, hands, people, other light sources
```
**ANİMASYON PROMPTU (image-to-video)**
```text
the display digits change from 22 to 23 (handled in post); the glow brightens slightly at the moment of change. Duration 7 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: static
```
- **Kamera:** Sabit. · static
- **Teknik:** Rakamlar montajda grafik (görselde boş ekran üret).
- **Montaj grafiği:** Ekran: 22 → 23

---

## B1-S12a  ·  S12  ·  1:33–1:36  ·  3 sn

Mekân `L04` · `T-GÜN` · Karakter `AYLA` (A-GECE)

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L04: a spacious old Istanbul living room 5.6 x 4.9 m with 3.10 m high ceilings and simple plaster crown molding, two tall windows on the north wall facing the street with white sheer curtains and heavy dark grey drapes, worn oak herringbone parquet with FOUR FAINT DARK DENTED MARKS in front of the bookshelf where an old armchair stood for years, a tall white bookshelf along the west wall half filled with books and half with unopened moving boxes, a wall clock on top, an old bottle-green velvet armchair, a grey fabric sofa against the east wall, a low walnut coffee table, a large monstera plant by the window, unhung picture frames leaning against the wall, a white panel radiator under each window, flat overcast daylight through sheer curtains, dust in the air, muted greens and greys, AYLA DEMIR, a 30-year-old Turkish woman, 166 cm tall, slim average build, slightly tense posture with shoulders turned inward, oval face with a gently pointed chin and defined cheekbones, hazel-brown eyes, natural thick eyebrows, small mole under her LEFT eye, light warm olive skin, faint under-eye shadows, dark chestnut-brown shoulder-length wavy hair tied in a loose low messy bun with a graphite pencil stuck through it, two loose strands falling at the front of her face, thin silver ring on right index finger, thin gold wedding band on left ring finger, faint grey ink smudges on the fingertips of her right hand, observant cautious expression, wearing faded light-grey long-sleeve cotton pajama top and matching loose pajama trousers, the ochre-mustard knit cardigan thrown over her shoulders, barefoot or grey wool socks, SHOT: medium shot of AYLA standing in the living room doorway holding a coffee cup, seen from inside the room. she wears pajamas with the ochre cardigan over her shoulders, her face freezes as she looks toward the window
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, medium shot of AYLA standing in the living room doorway holding a coffee cup, seen from inside the room, she wears pajamas with the ochre cardigan over her shoulders, her face freezes as she looks toward the window, location L04 T-GÜN (location reference L04-MASTER), characters: AYLA (character reference AYLA-REF-01, outfit A-GECE)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes
```
**ANİMASYON PROMPTU (image-to-video)**
```text
Ayla stops mid-step; the coffee in the cup trembles slightly. Duration 3 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: static
```
- **Kamera:** Sabit. · static
- **Teknik:** Sınırlı animasyon.

---

## B1-S12b  ·  S12  ·  1:36–1:39  ·  3 sn

Mekân `L04` · `T-GÜN`

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L04: a spacious old Istanbul living room 5.6 x 4.9 m with 3.10 m high ceilings and simple plaster crown molding, two tall windows on the north wall facing the street with white sheer curtains and heavy dark grey drapes, worn oak herringbone parquet with FOUR FAINT DARK DENTED MARKS in front of the bookshelf where an old armchair stood for years, a tall white bookshelf along the west wall half filled with books and half with unopened moving boxes, a wall clock on top, an old bottle-green velvet armchair, a grey fabric sofa against the east wall, a low walnut coffee table, a large monstera plant by the window, unhung picture frames leaning against the wall, a white panel radiator under each window, flat overcast daylight through sheer curtains, dust in the air, muted greens and greys, SHOT: insert of the parquet in front of the window from slightly above. an empty rectangle of painter's tape strips on the floor where the armchair stood, nothing inside it
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, insert of the parquet in front of the window from slightly above, an empty rectangle of painter's tape strips on the floor where the armchair stood, nothing inside it, location L04 T-GÜN (location reference L04-MASTER)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes, armchair, furniture inside the tape
```
**ANİMASYON PROMPTU (image-to-video)**
```text
still; window light slowly shifts. Duration 3 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: static
```
- **Kamera:** Sabit. · static
- **Teknik:** Tek görsel.

---

## B1-S12c  ·  S12  ·  1:39–1:43  ·  4 sn

Mekân `L04` · `T-GÜN`

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L04: a spacious old Istanbul living room 5.6 x 4.9 m with 3.10 m high ceilings and simple plaster crown molding, two tall windows on the north wall facing the street with white sheer curtains and heavy dark grey drapes, worn oak herringbone parquet with FOUR FAINT DARK DENTED MARKS in front of the bookshelf where an old armchair stood for years, a tall white bookshelf along the west wall half filled with books and half with unopened moving boxes, a wall clock on top, an old bottle-green velvet armchair, a grey fabric sofa against the east wall, a low walnut coffee table, a large monstera plant by the window, unhung picture frames leaning against the wall, a white panel radiator under each window, flat overcast daylight through sheer curtains, dust in the air, muted greens and greys, SHOT: very low tracking shot along the parquet surface. four parallel fresh scrape lines run across the herringbone parquet from the window toward the bookshelf on the west wall
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, very low tracking shot along the parquet surface, four parallel fresh scrape lines run across the herringbone parquet from the window toward the bookshelf on the west wall, location L04 T-GÜN (location reference L04-MASTER)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes, people
```
**ANİMASYON PROMPTU (image-to-video)**
```text
the camera glides low along the scrape lines toward the bookshelf. Duration 4 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: low tracking dolly following the marks
```
- **Kamera:** Yerde yavaş takip kayması (dolly), 4 sn. · low tracking dolly following the marks
- **Teknik:** Uzun yatay zemin görseli, AE'de perspektifli kaydırma.

---

## B1-S12d  ·  S12  ·  1:43–1:46  ·  3 sn

Mekân `L04` · `T-GÜN` · Eşya/ref `FOTO:F-1`

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L04: a spacious old Istanbul living room 5.6 x 4.9 m with 3.10 m high ceilings and simple plaster crown molding, two tall windows on the north wall facing the street with white sheer curtains and heavy dark grey drapes, worn oak herringbone parquet with FOUR FAINT DARK DENTED MARKS in front of the bookshelf where an old armchair stood for years, a tall white bookshelf along the west wall half filled with books and half with unopened moving boxes, a wall clock on top, an old bottle-green velvet armchair, a grey fabric sofa against the east wall, a low walnut coffee table, a large monstera plant by the window, unhung picture frames leaning against the wall, a white panel radiator under each window, flat overcast daylight through sheer curtains, dust in the air, muted greens and greys, SHOT: wide shot of the green velvet armchair standing in front of the white bookshelf on the west wall. the armchair sits at exactly the same position and angle as in photograph F-1 (the old couple's photo), slightly angled toward the room, the empty tape rectangle by the window visible in the background
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, wide shot of the green velvet armchair standing in front of the white bookshelf on the west wall, the armchair sits at exactly the same position and angle as in photograph F-1 (the old couple's photo), slightly angled toward the room, the empty tape rectangle by the window visible in the background, location L04 T-GÜN (location reference L04-MASTER)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes, people, armchair by the window
```
**ANİMASYON PROMPTU (image-to-video)**
```text
still; a faint dust swirl in the light. Duration 3 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: static
```
- **Kamera:** Sabit. · static
- **Teknik:** Kompozisyon F-1 fotoğrafıyla eşleşmeli (aynı açı, aynı konum).
- **Referans:** Kompozisyon için F-1 fotoğraf görseli yanına konup karşılaştırılacak.

---

## B1-S12e  ·  S12  ·  1:46–1:50  ·  4 sn

Mekân `L04` · `T-GÜN` · Karakter `AYLA` (A-GECE)

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L04: a spacious old Istanbul living room 5.6 x 4.9 m with 3.10 m high ceilings and simple plaster crown molding, two tall windows on the north wall facing the street with white sheer curtains and heavy dark grey drapes, worn oak herringbone parquet with FOUR FAINT DARK DENTED MARKS in front of the bookshelf where an old armchair stood for years, a tall white bookshelf along the west wall half filled with books and half with unopened moving boxes, a wall clock on top, an old bottle-green velvet armchair, a grey fabric sofa against the east wall, a low walnut coffee table, a large monstera plant by the window, unhung picture frames leaning against the wall, a white panel radiator under each window, flat overcast daylight through sheer curtains, dust in the air, muted greens and greys, AYLA DEMIR, a 30-year-old Turkish woman, 166 cm tall, slim average build, slightly tense posture with shoulders turned inward, oval face with a gently pointed chin and defined cheekbones, hazel-brown eyes, natural thick eyebrows, small mole under her LEFT eye, light warm olive skin, faint under-eye shadows, dark chestnut-brown shoulder-length wavy hair tied in a loose low messy bun with a graphite pencil stuck through it, two loose strands falling at the front of her face, thin silver ring on right index finger, thin gold wedding band on left ring finger, faint grey ink smudges on the fingertips of her right hand, observant cautious expression, wearing faded light-grey long-sleeve cotton pajama top and matching loose pajama trousers, the ochre-mustard knit cardigan thrown over her shoulders, barefoot or grey wool socks, SHOT: extreme close-up at floor level of one armchair leg and AYLA's right hand lifting it. under the lifted leg a faded dark round dent in the parquet; the leg is then lowered and fits perfectly into the dent
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, extreme close-up at floor level of one armchair leg and AYLA's right hand lifting it, under the lifted leg a faded dark round dent in the parquet; the leg is then lowered and fits perfectly into the dent, location L04 T-GÜN (location reference L04-MASTER), characters: AYLA (character reference AYLA-REF-01, outfit A-GECE)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes, extra fingers
```
**ANİMASYON PROMPTU (image-to-video)**
```text
the hand lifts the leg 3 cm, holds, then lowers it so it drops exactly into the dent with a small settle. Duration 4 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: static
```
- **Kamera:** Sabit. · static
- **Teknik:** Elle ara kare, 'tak' sesiyle kare-senkron.

---

## B1-S13  ·  S13  ·  1:50–1:58  ·  8 sn

Mekân `L04` · `T-GÜN` · Karakter `AYLA` (A-GECE)

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L04: a spacious old Istanbul living room 5.6 x 4.9 m with 3.10 m high ceilings and simple plaster crown molding, two tall windows on the north wall facing the street with white sheer curtains and heavy dark grey drapes, worn oak herringbone parquet with FOUR FAINT DARK DENTED MARKS in front of the bookshelf where an old armchair stood for years, a tall white bookshelf along the west wall half filled with books and half with unopened moving boxes, a wall clock on top, an old bottle-green velvet armchair, a grey fabric sofa against the east wall, a low walnut coffee table, a large monstera plant by the window, unhung picture frames leaning against the wall, a white panel radiator under each window, flat overcast daylight through sheer curtains, dust in the air, muted greens and greys, AYLA DEMIR, a 30-year-old Turkish woman, 166 cm tall, slim average build, slightly tense posture with shoulders turned inward, oval face with a gently pointed chin and defined cheekbones, hazel-brown eyes, natural thick eyebrows, small mole under her LEFT eye, light warm olive skin, faint under-eye shadows, dark chestnut-brown shoulder-length wavy hair tied in a loose low messy bun with a graphite pencil stuck through it, two loose strands falling at the front of her face, thin silver ring on right index finger, thin gold wedding band on left ring finger, faint grey ink smudges on the fingertips of her right hand, observant cautious expression, wearing faded light-grey long-sleeve cotton pajama top and matching loose pajama trousers, the ochre-mustard knit cardigan thrown over her shoulders, barefoot or grey wool socks, SHOT: high angle from near the ceiling looking down at AYLA kneeling small by the armchair, the composition continues upward to the open double glass door of the corridor where the low corridor ceiling sits in darkness. grey morning light in the living room gradually gives way to the dark corridor in the upper part of the frame
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, high angle from near the ceiling looking down at AYLA kneeling small by the armchair, the composition continues upward to the open double glass door of the corridor where the low corridor ceiling sits in darkness, grey morning light in the living room gradually gives way to the dark corridor in the upper part of the frame, location L04 T-GÜN (location reference L04-MASTER), characters: AYLA (character reference AYLA-REF-01, outfit A-GECE)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes, figures in the corridor
```
**ANİMASYON PROMPTU (image-to-video)**
```text
the camera rises and slowly rotates toward the corridor doorway, ending with the dark corridor ceiling filling the upper half of the frame and the top of Ayla's head at the bottom edge. Duration 8 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: slow crane up + pan toward corridor door
```
- **Kamera:** Yavaş yükselme ve dönme (crane + pan), 8 sn. · slow crane up + pan toward corridor door
- **Teknik:** Tek uzun dikey görsel + AE kamera; ya da kaba 3D maket üstüne boyama (projection mapping).

---

## B1-S14  ·  S14  ·  1:58–2:12  ·  14 sn

Mekân `L04` · `T-GÜN` · Karakter `AYLA` (A-GECE)

**GÖRSEL PROMPT (pozitif)**
```text
cinematic hand-drawn 2D animation still, adult psychological horror, mature graphic-novel realism, clean confident ink linework with subtle line-weight variation, realistic human anatomy and proportions, painterly cel shading with soft controlled shadows, detailed atmospheric backgrounds with real depth, accurate architectural perspective, cinematic lighting, desaturated muted color palette, cold blue-grey shadows, film grain, shallow depth of field, 35mm film framing, vertical 9:16 composition, quiet unsettling mood, European adult animation feature quality, LOCATION L04: a spacious old Istanbul living room 5.6 x 4.9 m with 3.10 m high ceilings and simple plaster crown molding, two tall windows on the north wall facing the street with white sheer curtains and heavy dark grey drapes, worn oak herringbone parquet with FOUR FAINT DARK DENTED MARKS in front of the bookshelf where an old armchair stood for years, a tall white bookshelf along the west wall half filled with books and half with unopened moving boxes, a wall clock on top, an old bottle-green velvet armchair, a grey fabric sofa against the east wall, a low walnut coffee table, a large monstera plant by the window, unhung picture frames leaning against the wall, a white panel radiator under each window, flat overcast daylight through sheer curtains, dust in the air, muted greens and greys, AYLA DEMIR, a 30-year-old Turkish woman, 166 cm tall, slim average build, slightly tense posture with shoulders turned inward, oval face with a gently pointed chin and defined cheekbones, hazel-brown eyes, natural thick eyebrows, small mole under her LEFT eye, light warm olive skin, faint under-eye shadows, dark chestnut-brown shoulder-length wavy hair tied in a loose low messy bun with a graphite pencil stuck through it, two loose strands falling at the front of her face, thin silver ring on right index finger, thin gold wedding band on left ring finger, faint grey ink smudges on the fingertips of her right hand, observant cautious expression, wearing faded light-grey long-sleeve cotton pajama top and matching loose pajama trousers, the ochre-mustard knit cardigan thrown over her shoulders, barefoot or grey wool socks, SHOT: close-up of AYLA's face, three-quarter front, kneeling on the floor. her expression: frozen fear mixed with realization, lips slightly parted, grey morning light — this frame will be blurred and darkened under the choice card
```
**KISA PROMPT** (token sınırı olan araçlar için; karakter ve mekân referans görselleriyle birlikte kullanılır)
```text
cinematic hand-drawn 2D animation still, adult psychological horror, graphic-novel realism, realistic anatomy, painterly cel shading, muted desaturated palette, cold blue-grey shadows, film grain, vertical 9:16, close-up of AYLA's face, three-quarter front, kneeling on the floor, her expression: frozen fear mixed with realization, lips slightly parted, grey morning light — this frame will be blurred and darkened under the choice card, location L04 T-GÜN (location reference L04-MASTER), characters: AYLA (character reference AYLA-REF-01, outfit A-GECE)
```
**NEGATİF PROMPT**
```text
chibi, cartoon, kawaii, children's animation style, exaggerated anime eyes, manga, 3D render, CGI, plastic skin, doll-like, glossy, oversaturated colors, neon, deformed face, asymmetrical eyes, extra fingers, missing fingers (except where specified), fused fingers, extra limbs, distorted hands, warped anatomy, elongated neck, inconsistent clothing, random text, watermark, logo, signature, blurry face, duplicate characters, cluttered composition, jump-scare gore, blood splatter, supernatural creature, ghost, glowing eyes
```
**ANİMASYON PROMPTU (image-to-video)**
```text
none (static background under the card); a slow 3% blur increase over the duration. Duration 14 seconds. Keep character faces, clothing and proportions identical to the source frame, no morphing, no new objects, hand-drawn 2D animation look, limited animation on twos (12 fps character motion), camera: static
```
- **Kamera:** Sabit. · static
- **Teknik:** Arka plan: görsel %70 karartma + Gauss bulanıklığı 18 px. Üstüne seçim kartı grafiği.
- **Montaj grafiği:** AYLA NE YAPMALI? / A — Mert'e söylemeden gizli bir kamera kur. / B — Mert'e her şeyi anlat, bu gece birlikte uyanık kalın. / Yorumlara A ya da B yaz.
