# Survei Validasi Produk: Otomotif Visual 3D

Dua versi survei untuk validasi *problem-solution fit*, *willingness to pay*, dan rekrutmen *early adopter MVP*.

## 📁 Struktur

```
survey/
├── google-forms-template.json   # Template untuk import ke Google Forms
├── index.html                   # Custom HTML + GitHub Pages version
├── gas-endpoint.gs              # Google Apps Script endpoint (copy ke Apps Script)
└── README.md                    # File ini
```

## 🚀 Cara Pakai

### Opsi 1: Google Forms (Recommended untuk distribusi massal)

1. Buka [forms.google.com](https://forms.google.com) → **Blank form**
2. Klik **⋮** (kanan atas) → **Import questions** → Pilih `google-forms-template.json`
   - *Atau* buat manual mengikuti struktur di JSON (7 section, 28 pertanyaan)
3. **Settings** → **Responses** → **Collect email addresses** ✓
4. **Settings** → **Presentation** → **Show progress bar** ✓
5. **Responses** → **Link to Sheets** → Buat spreadsheet baru
6. Kirim link ke target:
   - Pemilik bengkel (via komunitas Bengkel Indonesia, grup WhatsApp bengkel Bandung)
   - Pemilik motor (via grup komunitas: Thailook ID, Bratstyle ID, Cafe Racer ID, Vespa Club, dll)

### Opsi 2: Custom HTML + GitHub Pages (Branded, full control)

**Deploy ke GitHub Pages:**

```bash
# Dari root repo
git add survey/
git commit -m "Add survey: Google Forms template + custom HTML GitHub Pages"
git push origin main
```

Lalu aktifkan GitHub Pages:
1. Repo → **Settings** → **Pages**
2. Source: **Deploy from a branch** → `main` / `survey` folder
3. Save → URL: `https://fajar1180.github.io/Project-Otomotif-Visual3D/survey/`

**Konfigurasi endpoint pengiriman data:**

Edit `index.html`, ganti `FORM_ENDPOINT`:

```javascript
const FORM_ENDPOINT = 'https://script.google.com/macros/s/YOUR_DEPLOYMENT_ID/exec';
```

Buat Google Apps Script endpoint:
1. Buka [script.google.com](https://script.google.com) → **New Project**
2. Copy isi `gas-endpoint.gs` ke editor
3. Buat Google Sheet baru → copy **Spreadsheet ID** dari URL
4. Ganti `SPREADSHEET_ID` di script
5. **Deploy** → **New deployment** → **Web app** → Execute as: **Me**, Who has access: **Anyone** → **Deploy**
6. Copy **URL** → paste ke `FORM_ENDPOINT` di `index.html`

## 📋 Isi Survei (7 Section, 28 Pertanyaan)

| Section | Topik | Jumlah | Tujuan |
|---------|-------|--------|--------|
| A | Screening & Demografi | 4 | Segmentasi: bengkel vs user, lokasi, komunitas |
| B | Validasi Masalah | 5 | Skala 1-5: diagnosis, biaya, ketergantungan, visualisasi modif, wasted trip |
| C | Perilaku Saat Ini | 4 | Channel diagnosis, beli suku cadang, minat modif, app existing |
| D | Validasi Fitur | 5 | Skala 1-5: AI diagnosis, 3D config, bengkel finder, Shopee link, history |
| E | Keinginan Bayar | 4 | Pricing tier bengkel & user, fee listing, metode bayar |
| F | Rekrutmen MVP | 4 | Early adopter, WA, email, channel preferensi |
| G | Masukan Bebas | 3 | Feature request, concern, referral bengkel/komunitas |

## 🎯 Target Responden

| Segmen | Target | Channel Distribusi |
|--------|--------|-------------------|
| Pemilik bengkel motor | 50+ | Grup WA Bengkel Bandung, Asosiasi Bengkel Indonesia, LinkedIn |
| Pemilik motor (user) | 200+ | Komunitas: Thailook ID (150k+), Bratstyle ID, Cafe Racer ID, Vespa Club ID, grup motor Bandung |
| Mekanik/teknisi | 30+ | Grup WA mekanik, bengkel partner |

## 📊 Analisis Hasil (Post-Survei)

Export ke Google Sheets → Analisis:

1. **Pain score rata-rata** per section B → validasi *problem-solution fit*
2. **Feature usefulness** (section D) → prioritas development
3. **WTP distribution** (section E) → pricing strategy
4. **Early adopter list** (section F) → email/WA list untuk MVP testing
5. **Cross-tab** role × pain score → segmentasi ICP

## 🔗 Link Terkait

- Proposal: `docs/proposal/PROPOSAL_PENGAJUAN_STARTUP_DIGITAL.md`
- Data bengkel Bandung: `docs/DATA_BENGKEL_BANDUNG.md`
- Repo: `https://github.com/Fajar1180/Project-Otomotif-Visual3D`

---

**Catatan:** Data survei anonim kecuali email/WA untuk early adopter. Tidak ada PII sensitif. GDPR/PDPA compliant.