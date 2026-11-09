# AŞAMA 5-A — BÖLÜM 1 "SANTİMETRELER" GÖRSEL VE SES ÜRETİM PAKETİ

**Dosyalar G, H, I, J — Bölüm 1**

| Dosya | İçerik | Konum |
|-------|--------|-------|
| **G** | Her planın görsel üretim promptu (tam + kısa + negatif) | `05-uretim-b1-tam-promptlar.md` (otomatik üretilir) |
| **H** | Her planın animasyon ve kamera promptu | Aynı dosya + bu dosyanın 2. bölümü |
| **I** | Anlatıcı ve karakter seslendirme metinleri, altyazı | Bu dosyanın 3. bölümü + `uretim/altyazi/b1.srt` |
| **J** | Ses efektleri ve müzik planı (zaman kodlu) | Bu dosyanın 4. bölümü |
| — | Plan listesi verisi (tek kaynak) | `uretim/sahneler/b1.json` |
| — | Prompt araçları | `uretim/bloklari_cikar.py`, `uretim/prompt_olustur.py` |

---

## 0. ÜRETİM HATTI

### 0.1 Prompt sistemi (devamlılığın teknik güvencesi)

```
03a / 03b / 03c (master .md)
        │  python3 uretim/bloklari_cikar.py
        ▼
uretim/bloklar.json  (84 blok: stil, negatif, 6 karakter, 15 kıyafet, 18 mekân, 22 ışık, 19 eşya)
        │  + uretim/sahneler/b1.json  (28 plan)
        │  python3 uretim/prompt_olustur.py b1
        ▼
05-uretim-b1-tam-promptlar.md  (her plan için tam prompt, kısa prompt, negatif, animasyon promptu)
```

- **Tek doğruluk kaynağı master dosyalar.** Bir karakterin tarifi değişirse yalnızca `03a` düzenlenir, iki komut çalıştırılır ve bütün promptlar güncellenir. Hiçbir prompt elle kopyalanmaz, bu yüzden "Ayla'nın beni bir sahnede sağ gözünün altına kaydı" türünden hatalar sistemsel olarak engelleniyor.
- Betik, eksik bir blok kodu (yanlış kıyafet ya da mekân kodu) görürse durur. Plan sürelerinin toplamı hedef süreyle uyuşmazsa uyarı yazar. **B1: 28 plan, 132 sn, hedefle birebir.**
- **Tam prompt:** Uzun prompt kabul eden araçlar için (stil + mekân + ışık + karakter + kıyafet + eşya + plan tarifi).
- **Kısa prompt:** Token sınırı olan araçlar için. Karakter ve mekân referans görselleri (`AYLA-REF-01`, `L03-MASTER` vb.) ile birlikte kullanılır.

### 0.2 Plan başına iş akışı

1. **Anahtar kare (keyframe):** Tam ya da kısa prompt + karakter referansı + STİL-REF-01 → 4 varyant üret → en iyisini seç.
2. **Kare kalite kontrolü:** Bölüm 5'teki listeyle kontrol et (yüz, eller, kıyafet, mekân konumları). Gerekirse inpainting ile düzelt.
3. **Katmanlara ayırma:** Ön plan, karakter, arka plan (2.5D parallax gerektiren planlar için).
4. **Animasyon:** Plan başına belirtilen tekniğe göre:
   - **AE:** After Effects ya da muadili, katmanlı parallax, ışık ve partikül.
   - **İ2V:** Image-to-video aracı, animasyon promptuyla, en fazla 4–5 sn'lik parçalar.
   - **EL:** Elle ara kare (eller, kritik nesne hareketleri).
5. **Montaj:** Zaman çizelgesine göre kurgu. Grafikler (telefon ekranları, termostat rakamları, başlık, seçim kartı) **montajda eklenir, asla görsel aracına yazdırılmaz.**
6. **Ses:** Seslendirme → ses efektleri → müzik → miks (bölüm 4).
7. **Altyazı:** `b1.srt` montajda gömülür (güvenli alan: ekran yüksekliğinin %62–%72'si).

### 0.3 Çıktı ayarları

| Ayar | Değer |
|------|-------|
| Çözünürlük | 1080×1920 (üretim 2160×3840, çıktıda küçültme) |
| Kare hızı | 24 fps (proje). Karakter animasyonu "ikilerde" (12 fps), kamera ve ışık 24 fps. |
| Codec | H.264 High, 15–20 Mbps, AAC 320 kbps 48 kHz |
| Ses seviyesi | Entegre **-14 LUFS**, gerçek tepe **-1 dBTP** |
| Renk | Rec.709. Gece sahnelerinde siyahlar ezilmez (telefonda görünürlük için siyah seviyesi en az 4–6 IRE). |
| Altyazı | Gömülü (burned-in). Platformun otomatik altyazısına güvenilmez. |

---

## 1. (G) GÖRSEL PLAN LİSTESİ — ÖZET

> Tam promptlar: `05-uretim-b1-tam-promptlar.md`

| Plan | Zaman | Süre | Mekân · Işık | Karakter (kıyafet) | Kadraj | Teknik |
|------|-------|------|---------------|---------------------|--------|--------|
| B1-S01 | 0:00 | 4 | L06 · GECE | Ayla (A-GECE), Mert (M-GECE), odak dışı | ECU telefon | AE |
| B1-S02 | 0:04 | 5 | L03 · GECE-0310 | — | WS koridor, doğudan batıya | AE parallax |
| B1-S02-T | 0:08,5 | 1,5 | — | — | Başlık kartı | Grafik |
| B1-S03 | 0:09 | 8 | L01 · GÜN | Ayla (A-DIŞ), Mert (M-EV + palto) | Uzun dikey WS, tilt | AE + EL |
| B1-S04a | 0:17 | 4 | L02 · IŞIK-AÇIK | Ayla'nın eli, Hikmet'in eli | İNSERT anahtar (P-01) | EL |
| B1-S04b | 0:21 | 5 | L02 · IŞIK-AÇIK | Hikmet (H-ANA) | MCU | EL + dudak |
| B1-S05a | 0:26 | 4 | L02 · IŞIK-AÇIK | Ayla (A-DIŞ), arkadan | OTS → Daire 8 | AE parallax |
| B1-S05b | 0:30 | 5 | L02 · IŞIK-AÇIK | Saadet (S-EV) | CU kapı aralığı | EL + dudak |
| B1-S06a | 0:35 | 4 | L04 · GÜN | Ayla (A-EV) | WS, koltuk pencere önünde | EL |
| B1-S06b | 0:39 | 3 | L04 · GÜN | Mert (M-EV) | MS profil | EL |
| B1-S06c | 0:42 | 3 | L05 · GÜN | Ayla (A-EV), Mert (M-İŞ) | MCU ikili | EL + dudak |
| B1-S07a | 0:45 | 4 | L05 · GÜN | — | İNSERT kupa, kulp SOLDA | AE |
| B1-S07b | 0:49 | 3 | — | — | İNSERT eskiz, kulp SAĞDA | AE |
| B1-S07c | 0:52 | 3 | L05 · GÜN | Ayla'nın eli | CU el kupayı çeviriyor | EL |
| B1-S08a | 0:55 | 5 | L03 · GÜN | Ayla (A-EV), Mert (M-İŞ) | WS girişten doğuya | EL + dudak |
| B1-S08b | 1:00 | 3 | L03 · GÜN | — | İNSERT sürtünme izleri | AE |
| B1-S08c | 1:03 | 3 | L03 · GÜN | — | POV tavan | AE tilt |
| B1-S09a | 1:06 | 6 | L08 | Ayla (A-EV, gözlüklü) | WS eskiz duvarı | AE pan |
| B1-S09b | 1:12 | 5 | L08 | — | 3 İNSERT (kırmızı daireler) | AE |
| B1-S10 | 1:17 | 9 | L04 · AKŞAM→GECE | Ayla (A-EV), Mert (M-EV) | Alçak açı | EL |
| B1-S11 | 1:26 | 7 | L03 · GECE-0310 | — | CU termostat | AE + grafik |
| B1-S12a | 1:33 | 3 | L04 · GÜN | Ayla (A-GECE) | MS kapıda | EL |
| B1-S12b | 1:36 | 3 | L04 · GÜN | — | İNSERT boş bant karesi | AE |
| B1-S12c | 1:39 | 4 | L04 · GÜN | — | Alçak takip, izler | AE dolly |
| B1-S12d | 1:43 | 3 | L04 · GÜN | — | WS koltuk = F-1 kompozisyonu | AE |
| B1-S12e | 1:46 | 4 | L04 · GÜN | Ayla'nın eli | ECU ayak çukura | EL |
| B1-S13 | 1:50 | 8 | L04 · GÜN | Ayla (A-GECE) | Yüksek açı, crane | AE / 3D maket |
| B1-S14 | 1:58 | 14 | L04 · GÜN | Ayla (A-GECE) | CU yüz + seçim kartı | Grafik |

**Üretilecek görsel sayısı:** 30 anahtar kare (S09b'de 3 ayrı insert var, S10'da iki ışık durumu var).
**Önce üretilecek referans görseller (03c):** STİL-REF-01, AYLA-REF-01, MERT-REF-01, SAADET-REF-01, HIKMET-REF-01, L01/L02/L03/L04/L05-MASTER, P-01, P-02, P-03, P-04, F-1.

---

## 2. (H) ANİMASYON VE KAMERA PLANI

### 2.1 Genel animasyon dili
- **Sınırlı animasyon (limited animation):** Karakterler az ama anlamlı hareket ediyor. Her mikro hareket (kupayı çevirmek, baş kaldırmak) bir bilgi taşıyor.
- **Kamera hareketleri yavaş ve sabit hızlı.** Ani zoom yok. Bütün "push-in"ler %2–%6 aralığında.
- **Image-to-video kuralı:** Yüzler, kıyafet ve oranlar kaynak kareyle birebir aynı kalmalı. Biçim değiştirme (morphing) görülen çıktı kullanılmaz. En fazla 4–5 sn'lik parçalar üretilir.
- **Dudak senkronu:** Diyaloglu 5 plan için ses önce kaydedilir, animasyon sese göre yapılır (bkz. 3. bölüm).

### 2.2 Plan bazında hareket tablosu

| Plan | Kamera | Karakter / nesne animasyonu | Kritik zamanlama |
|------|--------|------------------------------|------------------|
| S01 | Sabit → %2 ileri | Ekran 0,3 sn'de yanar. Uyuyanlarda nefes. | Ekran 0:00,5'te yanar. Tık 0:01, fuşş 0:02. |
| S02 | %6 ileri, 5 sn | Toz partikülü | Beyaza kesme 0:08,5 |
| S02-T | — | Sert giriş/çıkış | 0:08,5–0:09 |
| S03 | Tilt yukarı, 8 sn | Mert 2 adım, Ayla başını kaldırır, martı geçer | Tilt anlatıcıyla biter (0:16,8) |
| S04a | Sabit | Anahtarlar avuca düşer, başparmak pirinç anahtarı çevirir | Şıngırtı 0:18 |
| S04b | ±%0,5 el titreşimi | Dudak (2 sn), tespih, göz kayması | Replik 0:22–0:24 |
| S05a | %4 ileri | Ayla başını çevirir | — |
| S05b | Sabit | Dudak (3 sn), sonra kapı 1,5 sn'de kapanır | Replik 0:30,8–0:33,8. Klik 0:34,6 |
| S06a | Sabit | Koltuğa son itiş | — |
| S06b | Sabit | Matkap 1 sn döner | Matkap sesi 0:39,5 |
| S06c | Sabit | Ayla şakağını ovar, Mert su içer, konuşur | Replik 0:43–0:44 |
| S07a | Sabit | Yok (bulut ışığı) | — |
| S07b | Sabit | Sayfa kenarı kıpırdar | — |
| S07c | Elle takip | El kupayı 180° çevirir, 1 sn durur | Seramik sürtünmesi 0:53 |
| S08a | Sabit | Mert kameraya yürür, çıkar. Ayla sabit. | Replik 0:57,5. Kapı 0:59,5 |
| S08b | Sabit | Toz | — |
| S08c | Tilt yukarı, tavanda 1,5 sn bekleme | — | Tilt 1:03–1:04,5, bekleme 1:04,5–1:06 |
| S09a | Yatay pan, 6 sn | Ayla kırmızı daire çizer | Kalem sesi 1:10 |
| S09b | 3× mikro ileri | — | Her insert 1,66 sn |
| S10 | Sabit | Ayla bant yapıştırır. Mert bakar, vazgeçer. Lamba kapanır. | Lamba 1:25 (drone burada kesilir) |
| S11 | Sabit | Rakam 22→23 (grafik) | Tık 1:27, rakam 1:27, fuşş 1:28, sürtünme 1:29,5–1:31 |
| S12a | Sabit | Ayla durur, fincan titrer | — |
| S12b | Sabit | Işık kayar | — |
| S12c | Alçak dolly, 4 sn | — | — |
| S12d | Sabit | Toz | — |
| S12e | Sabit | El ayağı 3 cm kaldırır, bırakır | **"Tak" 1:48,5 (kare senkron)** |
| S13 | Crane + pan, 8 sn | — | Anlatıcı 1:51–1:56,3. Drone kesimi 1:56,3 |
| S14 | Sabit, bulanıklık artışı | Seçim kartı 1:58,5'te belirir | Tık 2:11,5 |

---

## 3. (I) SESLENDİRME METİNLERİ

### 3.1 Ses kimlikleri (bütün dizi için sabit)

| Rol | Ses tarifi | Yaş | Not |
|-----|------------|-----|-----|
| **ANLATICI** | Derin, sıcak, sakin bariton. İstanbul Türkçesi, nötr ve standart aksan. Dramatize etmeyen, "fısıldamayan" ama yakın mikrofon hissi veren bir ses (radyo tiyatrosu değil, belgesel yakınlığı). | 45–60 | **Bütün bölümlerde aynı kişi ve aynı mikrofon zinciri.** İlk kayıt oturumunun ayarları belgelenip sabitlenir. |
| **HİKMET** | Orta tonlu, biraz boğuk, "efendim"li ve resmî. Kibarlığın altında gerginlik. Cümle sonlarını yutar. | 61 | |
| **SAADET** | Kısık, düz, yaşlı ama net. Duygusuz gibi, ama her kelime ağır. | 73 | Fısıltıya yakın ama fısıltı değil. |
| **MERT** | Bariton, kısa ve kesin. Savunmaya geçince hafif alaycı. | 33 | |
| **AYLA** | Alçak, yumuşak, cümlelerini yarım bırakan. | 30 | B1'de repliği yok. |
| **KENAN** | Kuru, kırık, fısıltılı. Uzun aralıklarla konuşur. | 52 | B1'de yok. B6'dan itibaren. |

**Yapay zekâ seslendirmesi kullanılırsa (TTS):** Anlatıcı için tek bir ses profili seçilip **bütün bölümlerde aynı ayarlarla** kullanılır. Öneri: Stabilite yüksek (%65–75), stil abartısı düşük (%10–20), konuşma hızı 0,9×. Her bölümün ilk cümlesi önceki bölümün kaydıyla A/B dinlenerek karşılaştırılır.

### 3.2 Yazım işaretleri
- `/` kısa durak (0,3–0,5 sn) · `//` uzun durak (0,8–1 sn)
- **Kalın** kelime: hafif vurgu (ses yükseltmeden, yalnızca ağırlık)
- `[…]` yönetmen notu

### 3.3 ANLATICI METNİ — B1 (toplam 83 kelime, ~41,5 sn)

| # | Başlangıç | Bitiş | Metin | Yön |
|---|-----------|-------|-------|-----|
| A1 | 0:00,8 | 0:03,3 | O gece evde / **kimse** uyanık değildi. | [Çok sakin. Neredeyse bir sır veriyor. Tık sesinden hemen önce bitmeli değil, tık "uyanık" kelimesinin altına denk gelir.] |
| A2 | 0:05,0 | 0:07,0 | Termostat / yine de **değişti**. | [Düz. "Değişti"de hafif bir düşüş, soru değil, gerçek.] |
| A3 | 0:09,3 | 0:13,3 | Ayla ve Mert, / Ihlamur Apartmanı'na / bir kasım sabahı taşındılar. | [Masal tonu değil, tutanak tonu. Sıradan bir bilgi gibi.] |
| A4 | 0:13,6 | 0:16,8 | Kira, // olması gerekenin / **neredeyse yarısıydı**. | ["Kira"dan sonraki uzun durak bilinçli. Son kelimelerde çok hafif bir ironi.] |
| A5 | 0:36,0 | 0:38,5 | İlk gece / ikisi de deliksiz uyudu. | [Rahat bir tonla.] |
| A6 | 0:39,0 | 0:41,5 | Sabah, / ikisinin de **başı ağrıyordu**. | [Aynı rahat ton, değişmeden. İzleyici bunu önemsiz sanmalı.] |
| A7 | 0:46,0 | 0:48,0 | Ayla / sağ elini kullanırdı. | [Bir karakter bilgisi verir gibi.] |
| A8 | 0:48,3 | 0:50,5 | Kupasının kulpunu / **hep** sağa bırakırdı. | ["Hep" kelimesinde kısa bir ağırlık.] |
| A9 | 1:07,5 | 1:11,0 | Değişiklikler küçüktü. // Bir kupa. / Bir sandalye. / Bir ayakkabılık. | [Liste ritmik, her öğe bir öncekinden biraz daha yavaş.] |
| A10 | 1:11,5 | 1:15,0 | Hiçbiri, / birine anlatılacak kadar / büyük değildi. | [Ayla'nın yalnızlığı. Hafif hüzün.] |
| A11 | 1:40,0 | 1:42,3 | Koltuk / **kırk santim** kaymıştı. | [Somut, ölçülü.] |
| A12 | 1:42,6 | 1:45,5 | Tam / **on dört yıl** boyunca / durduğu yere. | [Bölümün en önemli cümlesi. "On dört yıl" yavaş. Cümle sonunda ses düşmez, askıda kalır.] |
| A13 | 1:51,0 | 1:53,3 | Ev, / eski düzenini hatırlıyordu. | [Sakin, neredeyse şefkatli.] |
| A14 | 1:53,8 | 1:56,3 | Ya da **biri**, // onun yerine hatırlıyordu. | ["Biri"den sonraki uzun durak bölümün korku anı. Son kelime fısıltıya yakın, ama net.] |
| A15 | 1:59,0 | 2:00,5 | Ayla ne yapmalı? | [Doğrudan izleyiciye. Soru tonunu abartmadan.] |

### 3.4 KARAKTER REPLİKLERİ — B1 (15 kelime)

| # | Zaman | Karakter | Replik | Yön | Dudak senkronu planı |
|---|-------|----------|--------|-----|----------------------|
| D1 | 0:22,0–0:24,0 | HİKMET | Alttakini boş verin. / Eski. | [Önemsiz bir şey söyler gibi, ama "eski"yi hızlı geçer, konuyu kapatır.] | B1-S04b |
| D2 | 0:30,8–0:33,8 | SAADET | Kaloriferi kısma kızım. / Bu ev soğuğu sevmez. | [Tavsiye değil, uyarı. Duygu yok. "Sevmez"de ses hafifçe düşer.] | B1-S05b |
| D3 | 0:43,0–0:44,0 | MERT | Boya kokusu. | [Umursamaz, ağzında su varmış gibi.] | B1-S06c |
| D4 | 0:57,5–0:58,5 | MERT | Sen çekmişsindir. | [Dönüp bakmadan, kapıya yürürken. Hafif sabırsızlık.] | B1-S08a |

### 3.5 Kayıt notları
- Diyaloglar **ortam hissiyle** kaydedilir: Hikmet ve Saadet merdiven boşluğunda (miksajda hafif yankı eklenecek, kayıt kuru yapılır). Mert mutfakta ve koridorda.
- Saadet'in repliği **kapı aralığından** konuşuyormuş gibi: mikrofon 40–50 cm, hafif eksen dışı.
- Anlatıcı: kuru, yakın (15–20 cm), pop filtreli, oda yankısı yok.
- Her satır için 3 alternatif okuma alınır. Montajda en az "oynanmış" olan seçilir.

### 3.6 Altyazı
`uretim/altyazi/b1.srt`: 19 altyazı satırı. Anlatıcı satırları düz, karakter replikleri başında uzun tire (—) ile.

---

## 4. (J) SES EFEKTLERİ VE MÜZİK PLANI

### 4.1 İmza sesler (bütün dizi, tek bir ses dosyası olarak sabitlenir)

| Kod | Ses | Tasarım | Kural |
|-----|-----|---------|-------|
| **SIG-TIK** | Termostat rölesi | Kuru, plastik ve metal karışımı tek bir "tık". 2–4 kHz bandında belirgin. Çok kısa yankı (koridor). | **Duyulduğu an müzik keser.** Her bölümde aynı dosya. |
| **SIG-FUSS** | Kombi ateşlemesi | Gaz akışının "fıs"ı + alevin "fuşş"u + ardından alçak gövde uğultusu (60–120 Hz). | Tık'tan 0,8–1 sn sonra gelir. |
| **SIG-HUM** | Kombi çalışma uğultusu | Alçak, sürekli, hafif dalgalı (kalp atışını andıran 0,8 Hz modülasyon, çok ince). | Gece sahnelerinde arka planda. Dizi ilerledikçe seviye yükselir (B1'de -38 dB, B6'da -22 dB). |
| **SIG-GICIRT** | Parke gıcırtısı | Eski meşe parke, tek ve uzun. | Kaynağı hiç gösterilmez. |

### 4.2 Müzik kuralları
- B1'de toplam **müzik süresi yaklaşık 25 sn** (bölümün %19'u). Geri kalanı ortam sesi ve sessizlik.
- Tek enstrüman: **çello drone'u** (sürekli, tek nota, D2 civarı, çok yavaş açılıp kapanan). Melodi yok.
- Müzik hiçbir zaman diyalogun ya da imza seslerin üstüne çıkmaz.

### 4.3 ZAMAN KODLU SES PLANI (cue sheet)

**Katmanlar:** AMB = ortam · SFX = efekt · FOL = foley · MUS = müzik · VO = anlatıcı · DIA = diyalog

| Zaman | Katman | Ses | Seviye | Not |
|-------|--------|-----|--------|-----|
| 0:00,0 | AMB | Yatak odası oda tonu (neredeyse sessiz) | -48 dB | |
| 0:00,5 | SFX | Telefon ekranı yanma (çok hafif elektronik "nefes") | -36 dB | |
| 0:00,8 | VO | A1 | -16 LUFS kısa | |
| 0:01,0 | SFX | **SIG-TIK** (uzak, kapı ardından, filtreli) | -30 dB | Low-pass 6 kHz |
| 0:02,0 | SFX | **SIG-FUSS** (uzak) → SIG-HUM | -32 → -40 dB | |
| 0:04,0 | AMB | Koridor gece tonu + SIG-HUM | -40 dB | |
| 0:05,0 | VO | A2 | | |
| 0:06,5 | FOL | **SIG-GICIRT** (tek, kaynaksız) | -30 dB | |
| 0:08,5 | — | **SERT SESSİZLİK** (beyaz başlık kartı, 0,5 sn tam sessizlik) | -∞ | |
| 0:09,0 | AMB | Sokak gündüz: uzak trafik, ıslak kaldırım | -30 dB | |
| 0:09,5 | SFX | Martı (tek çağrı) | -28 dB | |
| 0:10,0 | FOL | Koli bandı, koli taşıma, ayak sesleri | -26 dB | |
| 0:09,3 | VO | A3–A4 | | |
| 0:17,0 | AMB | Merdiven boşluğu yankılı oda tonu | -40 dB | |
| 0:18,0 | FOL | Anahtar şıngırtısı (P-01, üç anahtar) | -22 dB | Kare senkron |
| 0:21,0 | FOL | Tespih tıkırtısı (döngü, düzenli) | -30 dB | S04b boyunca |
| 0:22,0 | DIA | D1 Hikmet (hafif merdiven yankısı) | | |
| 0:26,0 | FOL | Kapı zincirinin gerilmesi | -28 dB | |
| 0:26,5 | AMB | Daire 8'den sızan radyo (eski Türk sanat müziği, enstrümantal, **telifsiz/özgün**), boğuk | -42 dB | Low-pass 2 kHz |
| 0:30,8 | DIA | D2 Saadet | | |
| 0:33,5 | FOL | Kapının kapanması + kilit kliği | -24 dB | Klik 0:34,6 |
| 0:35,0 | AMB | Oturma odası gündüz, camdan boğuk sokak | -38 dB | |
| 0:35,5 | FOL | Koltuğun parkede itilmesi (kısa) | -28 dB | |
| 0:36,0 | VO | A5–A6 | | |
| 0:39,5 | SFX | Akülü matkap (1 sn) | -30 dB | VO altında, kısık |
| 0:42,0 | AMB | Mutfak: buzdolabı motoru | -40 dB | |
| 0:42,5 | FOL | Musluk, bardak | -32 dB | |
| 0:43,0 | DIA | D3 Mert | | |
| 0:45,0 | AMB | Mutfak tonu sürer, buzdolabı motoru | -40 dB | |
| 0:46,0 | VO | A7–A8 | | |
| 0:53,0 | FOL | Seramiğin tezgâha sürtünmesi | -26 dB | |
| 0:53,5 | — | 2 sn **sessizlik** (yalnızca buzdolabı) | | |
| 0:54,5 | FOL | Koridordan ahşap sürtünmesi (ses köprüsü) | -30 dB | S8'e taşınır |
| 0:55,0 | AMB | Koridor gündüz tonu | -42 dB | |
| 0:56,0 | FOL | Mert'in ayak sesleri, palto hışırtısı | -28 dB | |
| 0:57,5 | DIA | D4 Mert | | |
| 0:59,5 | FOL | Dış kapı açılış/kapanış, kilit dönüşü | -24 dB | |
| 1:00,5 | FOL | Merdivende uzaklaşan ayak sesleri | -34 → -50 dB | |
| 1:02,0 | — | **Sessizlik** (S8c tavan bekleyişi) | -50 dB oda tonu | |
| 1:06,0 | AMB | Çalışma odası, avludan uzak çocuk sesi | -40 dB | |
| 1:06,0 | MUS | **M1 — çello drone** girişi (fade-in 3 sn) | -34 dB | Neredeyse hissedilmez |
| 1:07,5 | VO | A9–A10 | | |
| 1:10,0 | FOL | Kırmızı kalemin kâğıda sürtünmesi | -28 dB | |
| 1:17,0 | AMB | Oturma odası akşam, duvar saati tik-takı | -36 dB | |
| 1:18,0 | FOL | Kâğıt bant kopma ve yapıştırma (×3) | -26 dB | |
| 1:25,0 | FOL | Lamba düğmesi | -24 dB | |
| 1:25,0 | MUS | **M1 keskin kesim** (lamba ile) | → -∞ | |
| 1:26,0 | AMB | Koridor gece, mutlak sessizliğe yakın | -50 dB | |
| 1:27,0 | SFX | **SIG-TIK** (yakın, net) | -20 dB | Bölümün en net tık'ı |
| 1:28,0 | SFX | **SIG-FUSS** → SIG-HUM | -24 → -38 dB | |
| 1:29,5 | FOL | Oturma odası yönünden ağır mobilya sürtünmesi (ahşap/parke, 1,5 sn) | -26 dB | Kaynak görünmez, hafif uzak |
| 1:31,0 | — | **2 sn mutlak sessizlik** (hum bile kısılır) | -∞ | |
| 1:33,0 | AMB | Oturma odası sabah, boğuk sokak | -38 dB | |
| 1:34,0 | FOL | Fincan tabağında hafif titreme | -32 dB | |
| 1:40,0 | VO | A11–A12 | | |
| 1:48,5 | FOL | **"TAK"**: koltuk ayağının çukura oturması (tok, kısa, alçak frekanslı) | -18 dB | **Kare senkron, bölümün en net foley'si** |
| 1:48,6 | — | 1 sn sessizlik | | |
| 1:49,5 | MUS | **M2 — çello drone** (aynı nota, daha yakın), fade-in 1,5 sn | -30 → -24 dB | |
| 1:51,0 | VO | A13–A14 | | |
| 1:54,0 | FOL | Tavandan tek, ince tıkırtı (çok uzak) | -40 dB | Dikkatli izleyici duyar |
| 1:55,0 | SFX | SIG-HUM tek nefes | -40 dB | |
| 1:56,3 | MUS | **M2 keskin kesim** (son kelimeyle) | → -∞ | |
| 1:56,3 | — | **1,7 sn sessizlik** | | |
| 1:58,0 | SFX | SIG-HUM (seçim kartı altında sürekli) | -38 dB | |
| 1:59,0 | VO | A15 | | |
| 2:11,5 | SFX | **SIG-TIK** (son kare) | -24 dB | Bölümü kapatır |
| 2:12,0 | — | Son | | |

### 4.4 Sessizlik anları (bilinçli)

| Zaman | Süre | İşlev |
|-------|------|-------|
| 0:08,5 | 0,5 sn | Başlık kartı darbesi |
| 0:53,5 | 2 sn | Kupa: "bir şey yanlış" duygusu |
| 1:02–1:06 | ~4 sn | Tavanın bekleyişi |
| 1:31 | 2 sn | Mobilya sürtünmesinden sonra |
| 1:48,6 | 1 sn | "Tak"tan sonra |
| 1:56,3 | 1,7 sn | Kapanış cümlesinden sonra |

### 4.5 Miks notları
- **Dinleme ortamı telefon hoparlörü.** Bütün kritik sesler (tık, tak, sürtünme) telefon hoparlöründe de duyulmalı. 150 Hz altındaki bilgi tek başına taşıyıcı olmamalı. SIG-HUM için 200–400 Hz bandında harmonik katman eklenir.
- Kulaklık dinleyicisi için: Tavandan gelen sesler hafif yukarıda ve merkezde. Kapı ardı sesler filtreli ve yanlarda.
- Anlatıcı her zaman en net ses. Altında müzik varsa müzik 6 dB bastırılır (sidechain/ducking).
- Bölüm sonu (seçim kartı): SIG-HUM sürekli ve tekdüze, izleyiciyi yorum yazana kadar huzursuz tutar.

---

## 5. B1 ÜRETİM KALİTE KONTROL LİSTESİ

**Görsel**
- [ ] Ayla'nın beni **sol** gözünün altında (S06c, S12a, S14).
- [ ] Ayla'nın gümüş yüzüğü **sağ işaret** parmağında (S04a, S07c, S12e).
- [ ] Hikmet'in tespihi **sağ** elinde, mühür yüzüğü **sol serçe** parmağında (S04a, S04b).
- [ ] Mert'in **sağ** kaşında yara izi (S06c, S08a).
- [ ] Saadet'in gözlüğü zincirli, mezurası boynunda (S05b).
- [ ] Kupanın kulpu: S07a'da **SOL**, S07b eskizinde **SAĞ**.
- [ ] Koltuk: S06a ve S10'da **pencere önünde**, S12d ve S13'te **kitaplık önünde** (F-1 ile aynı açı).
- [ ] Ayakkabılık: S02 ve S08a'da koridorun ortasında, kuzey duvarında, alçak tavanın altında.
- [ ] Koridorda alçak tavanla yüksek tavan arasındaki kiriş çizgisi görünüyor (S02, S08a, S08c).
- [ ] Kapak hiçbir karede açık ya da belirgin değil.
- [ ] Hiçbir karede okunabilir yapay zekâ metni ya da logo yok.
- [ ] Turuncu yalnızca kombi alevinde kullanılır. **B1'de turuncu hiç yok.**

**Ses**
- [ ] SIG-TIK üç kez duyuluyor (0:01, 1:27, 2:11,5) ve üçü aynı dosya.
- [ ] Müzik toplamı ~25 sn, iki parça (M1, M2), ikisi de keskin kesimle bitiyor.
- [ ] "Tak" sesi koltuk ayağıyla kare senkron.
- [ ] -14 LUFS, -1 dBTP.

**Süre ve metin**
- [ ] Toplam 2:12.
- [ ] Altyazı satırları VO zamanlarıyla uyumlu (`b1.srt`).
- [ ] Seçim kartı en az 12 sn ekranda.

---

*Bölüm 1'in Aşama 5 paketi tamamlandı. Onayınızdan sonra aynı paket B2-A ve B2-B için hazırlanacak. Sistem kurulduğu için sonraki bölümlerde yalnızca `uretim/sahneler/b2a.json` ve `b2b.json` plan dosyaları yazılacak, tam promptlar betikle üretilecek.*
