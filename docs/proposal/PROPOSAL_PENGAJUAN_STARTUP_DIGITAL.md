# PROPOSAL PENGAJUAN STARTUP DIGITAL

**Judul:** Otomotif Visual 3D — Platform Otomotif AI (Project Pak Yogi)
**Penyusun:** fajar1180 & ilhamalmunawar05-cpu
**Versi:** 2.0
**Tanggal:** 10 November 2026
**Program:** UTS Startup Digital UKRI
**Dosen Pengampu:** Yogi Saputra, S.T., M.Kom.

---

## 1. Ringkasan Eksekutif

**Otomotif Visual 3D** bergerak pada kategori industri platform teknologi otomotif (**Autotech**), melayani segmen:
- Penggemar modifikasi motor
- Pemilik kendaraan mencari solusi perbaikan mandiri (**DIY**)
- Mekanik dan bengkel lokal

Dengan model bisnis berbasis **afiliasi e-commerce (Shopee Affiliate)** dan **layanan diagnostik AI**.

Tahap pengembangan saat ini: **Prototipe (MVP diagnosis AI + 3D configurator)**.

Platform ini menggabungkan **Computer Vision (rekonstruksi 3D kendaraan)** dan **Conversational AI (RAG)** untuk diagnosis komponen kendaraan serta panduan perbaikan DIY. Target pengguna: pemilik bengkel, pemilik kendaraan (mobil & motor), mekanik, dan penggemar DIY di Indonesia.

**Masalah inti:** Pemilik kendaraan kesulitan mendiagnosa kerusakan sendiri, sehingga harus datang langsung ke bengkel tanpa estimasi biaya — membuang waktu dan biaya transportasi.

**Solusi:**
1. **AI Storytelling Diagnosis** — NLP/RAG menginterpretasi keluhan kendaraan (teks/audio), klasifikasi tingkat keparahan (DIY_EASY, DIY_HARD, WORKSHOP_REQUIRED), instruksi perbaikan langkah-demi-langkah, rekomendasi suku cadang dengan link Shopee Affiliate, riwayat diagnosis.
2. **AI 3D Modification Configurator & Shopee Recommender** — Visualisasi 3D modifikasi kendaraan (Sparse-View Image-to-3D + Template-Mesh Swapping), penukaran komponen real-time, link afiliasi Shopee, rekomendasi bengkel terdekat via Maps API (data bengkel Bandung: 50 lokasi terverifikasi dengan koordinat, jam buka, kategori).

**Sumber pendapatan:** Komisi afiliasi Shopee dari penjualan suku cadang dan komponen modifikasi (CPS 1–5%, rata-rata 3%).

---

## 2. Identitas Startup

| Item | Isi |
|------|-----|
| Nama | Otomotif Visual 3D |
| Bentuk | Startup Digital (Web-First, Next.js + FastAPI) |
| Status | Fase Inisiasi (PRD v1.0, SRS v1.0, ERD v1.0, API Spec v1.0 — 19 Oktober 2026) |
| Target Pelanggan | Pemilik bengkel, pemilik kendaraan (mobil & motor), mekanik, penggemar DIY |
| Lokasi | Indonesia (pilot: Bandung/Jabodetabek) |
| Tim | **fajar1180** — Project Manager, System Analyst, Backend, Frontend, QA Testing<br>**ilhamalmunawar05-cpu** — System Analyst, Backend Developer, Frontend Developer, QA Engineer<br>**Dosen Pengampu:** Yogi Saputra, S.T., M.Kom. |

---

## 3. Masalah dan Solusi Utama

### 3.1 Masalah
Pemilik motor di Indonesia menghadapi:
1. Kesulitan mendiagnosa kerusakan mandiri
2. Ketergantungan pada bengkel yang mahal dan tidak transparan
3. Minimnya panduan visualisasi modifikasi komponen
4. Tidak tahu estimasi biaya sebelum datang ke bengkel
5. Membuang waktu dan biaya transportasi untuk kunjungan tidak perlu

### 3.2 Solusi
**Otomotif Visual 3D** menyediakan:
- **Diagnosis berbasis AI (RAG + LLM)** yang menginterpretasi keluhan bahasa alami
- **Klasifikasi tingkat keparahan:** DIY_EASY, DIY_HARD, WORKSHOP_REQUIRED
- **Instruksi perbaikan terstruktur:** Kesimpulan diagnosis → Tingkat keparahan → Langkah perbaikan terstruktur → Rekomendasi suku cadang dengan link Shopee Affiliate → Riwayat diagnosis
- **Visualisasi 3D Hybrid:** Sparse-View Image-to-3D + Template-Mesh Swapping (ringan di browser)
- **Ekosistem terintegrasi:** Diagnosis → Suku cadang (Shopee Affiliate) → Bengkel terdekat (Maps API)

---

## 4. Keunggulan Kompetitif

Keunggulan bersifat **[Hipotesis]** karena belum tervalidasi pengguna nyata:

| No | Keunggulan | Target / Keterangan |
|----|------------|---------------------|
| 1 | Diagnosis AI Bahasa Indonesia akurat | **> 85%** [Target] |
| 2 | Referensi diagnosis cepat mengurangi waktu troubleshooting | **50%** [Target] |
| 3 | Integrasi Shopee Affiliate untuk monetisasi | CPS model, komisi 1–5% (rata-rata 3%) |
| 4 | Visualisasi 3D hybrid ringan di browser | Sparse-View Image-to-3D + Template-Mesh Swapping |
| 5 | Ekosistem terintegrasi diagnosis → suku cadang → bengkel | Maps API dengan data 50 bengkel Bandung terverifikasi |

---

## 5. Rencana Finansial Singkat

**Kebutuhan dana awal (CapEx + OpEx 6 bulan): Rp 151.100.000**  
*(Detail perhitungan: `research/finansial_sumber/README.md`, sumber utama: 7 file riset dengan harga pasar Oktober 2024)*

### 5.1 Capital Expenditure (CapEx) — One-time Setup
| Item | Estimasi (Rp) | Sumber |
|------|---------------|--------|
| Laptop GPU RTX 4070 class (development + lokal inference) | 30.000.000 | `01_harga_laptop_gpu.md` |
| Pendirian PT + Notaris + AHU + NPWP + NIB | 7.500.000 | `07_biaya_legal_perusahaan.md` (Opsi B Standard) |
| Merek 3 Kelas (9, 35, 42) via Konsultan | 7.500.000 | `07_biaya_legal_perusahaan.md` |
| Domicile Bandung 1 Tahun | 1.200.000 | `07_biaya_legal_perusahaan.md` |
| Domain .com + .id + SSL DV 1 Tahun | 560.000 | `07_biaya_legal_perusahaan.md` |
| Google Play + Apple Developer 1 Tahun | 1.934.400 | `07_biaya_legal_perusahaan.md` |
| **Total CapEx** | **48.694.400** | ≈ **Rp 48,7 Juta** |

*Asumsi pengakuan aset: laptop dikapitalisasi, depresiasi 3 tahun garis lurus. Cloud & lisensi berkala dicatat dalam OpEx.*

### 5.2 Operational Expenditure (OpEx) — Bulanan (6 Bulan)
| Item | Estimasi/Bulan (Rp) | 6 Bulan (Rp) | Sumber |
|------|---------------------|--------------|--------|
| Cloud GPU AWS g5.xlarge (A10G, Jakarta 24/7) | 13.100.000 | 78.600.000 | `02_harga_cloud_gpu.md` |
| PostgreSQL Supabase Pro (8 GB RAM, 100 GB) | 390.000 | 2.340.000 | `04_harga_database_redis.md` |
| Redis DigitalOcean 4 GB HA | 936.000 | 5.616.000 | `04_harga_database_redis.md` |
| LLM API (GPT-4o-mini + Haiku fallback, buffer 2x) | 100.000 | 600.000 | `03_harga_llm_api.md` |
| Google Maps API (net after $200 free tier) | 2.270.000 | 13.620.000 | `05_harga_google_maps.md` |
| Domicile Bandung (prorated) | 100.000 | 600.000 | `07_biaya_legal_perusahaan.md` |
| Domain/SSL (prorated) | 47.000 | 282.000 | `07_biaya_legal_perusahaan.md` |
| Apple Developer (prorated) | 128.700 | 772.200 | `07_biaya_legal_perusahaan.md` |
| **Total OpEx/Bulan** | **17.071.700** | **102.430.200** | ≈ **Rp 102,4 Juta** |

*Kurs: USD 1 = Rp 15.600 (BI Oktober 2024 rata-rata). Kontribusi tenaga sukarela (anggota) tidak dihitung sebagai biaya kas.*

### 5.3 Sumber Pendanaan
- Dana sendiri (bootstrap): Rp 50.000.000
- Hibah kampus (UKRI): Rp 50.000.000
- Pendanaan pra-seed (angel/VC): Rp 51.100.000

---

---

## 6. Business Model Canvas (BMC v1.0)

| Blok | Isi |
|------|-----|
| **Customer Segments** | Pemilik bengkel, pemilik kendaraan (mobil & motor), mekanik, penggemar DIY, komunitas modifikasi motor (Thailook, Bratstyle, Cafe Racer) |
| **Value Propositions** | Diagnosis AI Bahasa Indonesia akurat >85%; Visualisasi 3D interaktif untuk perbaikan real-time; Rekomendasi suku cadang terintegrasi afiliasi Shopee; Akses bengkel terpercaya dengan rating, review, jam buka, lokasi (50 bengkel Bandung terverifikasi) |
| **Channels** | Platform web (Next.js + R3F), link afiliasi Shopee, Maps API, komunitas motor (WhatsApp, Instagram, event offline) |
| **Customer Relationships** | Self-service diagnosis AI, dukungan mekanik via platform, chat AI avatar, Wizard of Oz MVP (manual review tim) |
| **Revenue Streams** | 1. **Komisi Shopee Affiliate (CPS)** — 1–5% × harga jual (rata-rata 3%); Asumsi: transaksi Rp200k–500k, konversi diagnosis→klik 10%, klik→beli 3%; **Estimasi realistis: Rp 131.250/bln** (15 transaksi × Rp 8.750 komisi) — sumber: `06_shopee_affiliate_cps.md`<br>2. **Langganan Premium** — Bengkel: Rp 150.000–300.000/bln; User: Rp 25.000–50.000/bln; Prasyarat: fitur premium terdefinisi (detail teknis lanjutan, prioritas antrian, API access)<br>3. **Fee Listing Bengkel Premium** — Bengkel partner: Rp 50.000–100.000/bln; Prasyarat: basis pengguna >10.000 MAU, lead terverifikasi |
| **Key Activities** | Pengembangan model AI/RAG (diagnosis), rendering 3D (configurator), pemeliharaan API & DB, validasi data bengkel, rekrutmen early adopter, komunitas building |
| **Key Resources** | Tim 2 orang (PM + Fullstack), PostgreSQL + pgvector, LLM OpenAI/Claude, Celery + Redis, Object Storage, Data bengkel Bandung (50 lokasi, koordinat, jam buka, kategori), Shopee Affiliate API, Maps API |
| **Key Partnerships** | Shopee Affiliate Program, Maps API Provider (Google/OSM), Penyedia LLM (OpenAI/Anthropic), Komunitas motor Bandung/Jabodetabek (20–30 early adopter), 5–10 bengkel partner pilot |
| **Cost Structure** | **CapEx:** Laptop GPU (Rp 30.000.000), Pendirian PT + Legal (Rp 16.200.000), Domain/SSL/Platform fees (Rp 2.494.400) — **Total CapEx: Rp 48.694.400** — sumber: `research/finansial_sumber/README.md`<br>**OpEx/Bulan:** Cloud GPU AWS g5.xlarge (Rp 13.100.000), Supabase Pro (Rp 390.000), Redis DO 4GB HA (Rp 936.000), LLM API (Rp 100.000), Google Maps API (Rp 2.270.000), Legal/Admin prorated (Rp 275.700) — **Total OpEx: Rp 17.071.700/bln** — sumber: `research/finansial_sumber/README.md`<br>*Kontribusi tenaga sukarela (anggota) tidak dihitung sebagai biaya kas.* |

**Status semua blok:** Belum diuji (belum ada eksperimen atau wawancara calon pengguna). Blok sementara berdasarkan PRD & SRS.

---

## 7. Key Activities & Arsitektur Teknis

### 7.1 Arsitektur Sistem
```
Frontend:     Next.js + React + R3F (React Three Fiber) + Tailwind CSS
Backend:      FastAPI + Python
Service Layer: Diagnosis Service, 3D Service, Workshop Service
Data Layer:   PostgreSQL + pgvector (vector DB untuk RAG), Redis (cache & queue), Object Storage (S3-compatible)
Async Processing: Celery + Redis queue untuk 3D generation & LLM inference berat
```

### 7.2 Service Layer Detail
| Service | Fungsi |
|---------|--------|
| **Diagnosis Service** | RAG pipeline: embedding keluhan → retrieve dokumen teknis → LLM generate diagnosis terstruktur (kesimpulan, keparahan, langkah, suku cadang) |
| **3D Service** | Sparse-View Image-to-3D reconstruction + Template-Mesh Swapping untuk konfigurator modifikasi real-time |
| **Workshop Service** | Pencarian bengkel terdekat (Haversine/PostGIS), filter rating/jam buka/kategori, integrasi Maps API |

---

## 8. Value Propositions (Detail)

1. **Diagnosis AI Bahasa Indonesia akurat > 85%** — RAG grounding pada dokumen teknis resmi & data historis, rule-based fallback untuk hallucination mitigation
2. **Visualisasi 3D interaktif untuk perbaikan real-time** — Hybrid rendering: Sparse-View Image-to-3D (rekonstruksi dari foto) + Template-Mesh Swapping (ganti komponen instan), ringan di browser via R3F/WebGL
3. **Rekomendasi suku cadang terintegrasi afiliasi Shopee** — Link afiliasi otomatis di output diagnosis, tracking konversi, komisi CPS
4. **Akses bengkel terpercaya dengan rating dan review** — Data 50 bengkel Bandung (koordinat, telepon, website, jam buka, kategori: Bengkel Mobil/Bengkel Motor, kecamatan: kopo/astanaanyar/regol/lengkong), filter radius & rating

---

## 9. Cost Structure (Rinci)

### 9.1 Capital Expenditure (CapEx) — One-time Setup
| Item | Estimasi (Rp) | Catatan | Sumber |
|------|---------------|---------|--------|
| Laptop GPU (RTX 4070/4080 class) | 30.000.000 | Development + lokal inference | `01_harga_laptop_gpu.md` |
| Pendirian PT + Notaris + AHU + NPWP + NIB | 7.500.000 | Via jasa notaris online (Opsi B Standard) | `07_biaya_legal_perusahaan.md` |
| Merek 3 Kelas (9, 35, 42) via Konsultan | 7.500.000 | Perlindungan brand di kelas Software, Advertising, SaaS | `07_biaya_legal_perusahaan.md` |
| Domicile virtual Bandung 1 tahun | 1.200.000 | Alamat legal untuk pendirian PT | `07_biaya_legal_perusahaan.md` |
| Domain .com + .id + SSL DV 1 tahun | 560.000 | IDwebhost/Niagahoster | `07_biaya_legal_perusahaan.md` |
| Google Play Console ($25) + Apple Developer ($99) | 1.934.400 | Fee publish aplikasi mobile | `07_biaya_legal_perusahaan.md` |
| **Total CapEx** | **48.694.400** | ≈ **Rp 48,7 Juta** | `research/finansial_sumber/README.md` |

*Asumsi pengakuan aset: laptop dikapitalisasi, depresiasi 3 tahun garis lurus. Cloud & lisensi berkala dicatat dalam OpEx.*

### 9.2 Operational Expenditure (OpEx) — Bulanan
| Item | Estimasi/Bulan (Rp) | 6 Bulan (Rp) | Asumsi | Sumber |
|------|---------------------|--------------|--------|--------|
| Cloud GPU Instance AWS g5.xlarge (A10G, Jakarta 24/7) | 13.100.000 | 78.600.000 | Inference LLM 7B-13B, on-demand, region Jakarta | `02_harga_cloud_gpu.md` |
| PostgreSQL + pgvector (Supabase Pro) | 390.000 | 2.340.000 | 8 GB RAM, 100 GB SSD, 2 vCPU, PITR 7 hari | `04_harga_database_redis.md` |
| Redis (DigitalOcean 4 GB HA) | 936.000 | 5.616.000 | Cache + session + Celery queue, standby node | `04_harga_database_redis.md` |
| API LLM (GPT-4o-mini + Haiku fallback) | 100.000 | 600.000 | Buffer 2x dari estimasi realistic 5k diagnosis/bln | `03_harga_llm_api.md` |
| Google Maps API (net after $200 free tier) | 2.270.000 | 13.620.000 | Places Nearby + Details + Directions + Geocoding | `05_harga_google_maps.md` |
| Domicile Bandung (prorated) | 100.000 | 600.000 | 1.200.000 / 12 bulan | `07_biaya_legal_perusahaan.md` |
| Domain + SSL (prorated) | 47.000 | 282.000 | 560.000 / 12 bulan | `07_biaya_legal_perusahaan.md` |
| Apple Developer (prorated) | 128.700 | 772.200 | 1.544.400 / 12 bulan | `07_biaya_legal_perusahaan.md` |
| **Total OpEx/Bulan** | **17.071.700** | **102.430.200** | ≈ **Rp 102,4 Juta / 6 bln** | `research/finansial_sumber/README.md` |

*Kurs: USD 1 = Rp 15.600 (BI Oktober 2024 rata-rata). Kontribusi tenaga sukarela (anggota) tidak dihitung sebagai biaya kas. Object Storage (S3-compatible) diestimasi < Rp 50.000/bln — termasuk di buffer Cloud GPU.*

---

## 10. Revenue Streams (Detail)

### 10.1 Mekanisme Utama: Shopee Affiliate (Cost Per Sale)
- **Pembayar:** Shopee (merchant), bukan pengguna akhir
- **Komisi:** 1–5% × harga jual suku cadang (rata-rata 3%) — sumber: `06_shopee_affiliate_cps.md`
- **Asumsi konversi (Target):**
  - Rata-rata transaksi (AOV): **Rp 350.000** (data industri e-commerce otomotif Indonesia 2023-2024)
  - Diagnosis → Klik afiliasi: **10%** [Target]
  - Klik → Beli (Conversion): **3%** [Target]
  - Komisi rata-rata: **3%**
  - **Komisi per transaksi: Rp 8.750** (350.000 × 2.5% blended rate)

### 10.2 Estimasi Revenue CPS (Realistis)
| Parameter | Conservative | **Realistic** | Optimistic |
|-----------|--------------|---------------|------------|
| Bengkel Aktif | 20 | **25** | 30 |
| Diagnosis/Bengkel/Bulan | 100 | **200** | 300 |
| Total Diagnosis/Bulan | 2.000 | **5.000** | 9.000 |
| Transaksi/Bulan (0.3% overall) | 6 | **15** | 63 |
| **Revenue CPS/Bulan** | Rp 52.500 | **Rp 131.250** | Rp 551.250 |

*Sumber perhitungan lengkap: `06_shopee_affiliate_cps.md` (termasuk proyeksi 12 bulan: Rp 18.506.250 kumulatif)*

### 10.3 Biaya Variabel per Transaksi
- Fee transaksi payment gateway (dipotong Shopee sebelum komisi)
- Biaya infra per request API LLM: ~$0.0006/request (GPT-4o-mini) → **Rp 9/request** — sumber: `03_harga_llm_api.md`

### 10.4 Stream Tambahan (Opsional, Pasca-PMF)
| Stream | Target Bayar | Harga | Prasyarat |
|--------|--------------|-------|-----------|
| **Langganan Premium** | Bengkel | Rp 150.000–300.000/bln | Fitur premium: detail teknis lanjutan, prioritas antrian, API access, analytics dashboard |
| **Langganan Premium** | User (pemilik kendaraan) | Rp 25.000–50.000/bln | Diagnosis unlimited, history export, prioritas bengkel partner |
| **Fee Listing Bengkel Premium** | Bengkel partner | Rp 50.000–100.000/bln | Basis pengguna >10.000 MAU, lead terverifikasi, featured placement |

*Stream 2 & 3 merupakan revenue utama jangka menengah (target >80% total revenue). CPS hanya pelengkap (Stream 1).*

---

## 11. Strategi Pemasaran

**Anggaran Pemasaran Bulanan: Rp 500.000** (termasuk di OpEx buffer, sumber: asumsi bootstrap minimal)

| Pilar | Aktivitas | Target | KPI | Estimasi Biaya/Bulan |
|-------|-----------|--------|-----|----------------------|
| **1. Komunitas & Early Adopter** | Rekrut 20–30 early adopter dari komunitas motor Bandung/Jabodetabek (WhatsApp, Instagram, event offline); insentif voucher Shopee Rp50k/user | 20–30 user Minggu 4–5 | Jumlah early adopter, retention rate, diagnosis/week | Rp 1.500.000 (one-time voucher 30×Rp50k) |
| **2. Digital / SEO / Sosmed** | Konten edukasi: IG Reels, TikTok, YouTube Shorts (diagnosis tips, modifikasi showcase, DIY guide); 3 konten/minggu | 10k followers 6 bln | Follower growth, engagement rate, CTR ke platform | Rp 200.000 (tools editing, boost minor) |
| **3. Partnering Komunitas** | MoU dengan 5–10 komunitas motor (Thailook, Bratstyle, Cafe Racer, dll); cross-promotion event | 5–10 komunitas | Jumlah komunitas, referral user, co-branded event | Rp 100.000 (merchandise, transport) |
| **4. Pemasaran Referral Bengkel** | Program insentif bengkel rujuk pengguna ke platform; fee listing gratis 3 bln pertama | 10 bengkel pilot | Bengkel aktif, lead terverifikasi, conversion rate | Rp 100.000 (admin, koordinasi) |

**Total Marketing 6 Bulan: Rp 3.000.000** (termasuk voucher early adopter one-time)

**CAC Target:** < Rp 50.000/user (organic community-driven)
**Kanal Prioritas:** Komunitas motor (WhatsApp/Instagram) → Organic Sosmed → Referral Bengkel

---

## 12. Produk (MVP)

### 12.1 Konsep Minimum Viable Product
- **Bentuk MVP:** Satu fitur inti — **AI Storytelling Diagnosis (Fitur 2)**
- **Asumsi paling berisiko:** *"Pengguna percaya diagnosis AI dan bertindak mengikuti rekomendasi (beli suku cadang / ke bengkel)."*
- **Tujuan MVP:** Memvalidasi akurasi diagnosis **> 85%** [Target], serta konversi diagnosis → klik link afiliasi **> 10%** [Target].
- **Pengguna uji:** 20–30 early adopter dari komunitas motor Bandung/Jabodetabek (rekrut via komunitas, insentif voucher Shopee Rp50k).
- **Metode:** **Wizard of Oz** — Frontend diagnosis fungsional, backend RAG dijalankan manual/semi-otomatis oleh tim untuk mengamati kualitas output sebelum otomatisasi penuh.
  - **Batas proses manual:** Pemilihan dokumen grounding, verifikasi output LLM sebelum dikirim ke user.

### 12.2 Endpoint MVP
- `POST /api/v1/diagnosis/analyze` (FastAPI)
- RAG pipeline dengan OpenAI/Claude
- Input: cerita keluhan (teks) + konteks kendaraan (merk, tipe, tahun, kategori kerusakan)
- Output: diagnosis terstruktur (kesimpulan, tingkat keparahan, langkah perbaikan, rekomendasi suku cadang + link Shopee, riwayat)

### 12.3 Fitur Ditunda (Post-MVP)
- 3D Configurator (Sparse-View + Template-Mesh)
- Shopee Affiliate integration otomatis (tracking, deep link)
- Pencari bengkel via Maps API (data 50 bengkel Bandung sudah siap)
- Riwayat diagnosis user
- Autentikasi & user profile
- Workshop Service (booking, review bengkel)

---

## 13. Analisis Pasar

- **Tren tinggi** budaya modifikasi motor di Indonesia (Thailook, Bratstyle, Cafe Racer) → basis pengguna penggemar DIY.
- **Peluang monetisasi** via Program Affiliate Shopee (ekosistem e-commerce terbesar SEA).
- **Segmen:** Pemilik bengkel, pemilik kendaraan (mobil & motor), mekanik, penggemar DIY.
- **Data bengkel Bandung:** 50 lokasi terverifikasi Nominatim (OpenStreetMap) — kategori Bengkel Mobil (38) & Bengkel Motor (12), tersebar di 4 kecamatan: Astanaanyar (17), Regol (19), Lengkong (13), Kopo (1). Dilengkapi koordinat, jam buka, kategori, place_id OSM.

---

## 14. Struktur Organisasi Tim

| Peran | fajar1180 | ilhamalmunawar05-cpu |
|-------|-----------|----------------------|
| Project Manager | ✅ | |
| System Analyst | ✅ | ✅ |
| Backend Developer | ✅ | ✅ |
| Frontend Developer | ✅ | ✅ |
| QA Testing / Engineer | ✅ | ✅ |

**Dosen Pengampu:** Yogi Saputra, S.T., M.Kom. (Supervisi akademik & validasi teknis)

*Peran ganda berdasarkan PRD §6.*

---

## 15. Roadmap Pengembangan (6 Minggu / M0–M5)

Sesuai PRD §5 Milestone. Semua jadwal merupakan rencana hingga ada bukti realisasi.

| Milestone | Deskripsi | Target |
|-----------|-----------|--------|
| **M0** | Project Kickoff & Finalisasi Arsitektur | Minggu 1 |
| **M1** | Implementasi Skema Database & Unit Tests | Minggu 2 |
| **M2** | Backend API (Diagnosis & 3D) + Frontend Skeleton | Minggu 3 |
| **M3** | Modul RAG Diagnostik + Integrasi Shopee Affiliate | Minggu 4 |
| **M4** | Integrasi Fitur Penuh (Diagnosis + 3D + Workshop Finder) & QA | Minggu 5 |
| **M5** | Rilis Production Ready + Uji Pengguna (Early Adopter) | Minggu 6 |

**Catatan:** Data bengkel Bandung (50 lokasi, JSON/CSV) siap di-ingest ke Workshop Service pada M3–M4.

---

## 16. Biaya Awal dan Capital Expenditure (CapEx) — Detail

Rincian pembelian aset dan biaya pendirian (sumber: `research/finansial_sumber/`):

| No | Item | Qty | Harga Satuan (Rp) | Total (Rp) | Sumber File |
|----|------|-----|-------------------|------------|-------------|
| 1 | Laptop GPU RTX 4070 class (ASUS ROG / MSI Katana / Lenovo Legion) | 1 | 30.000.000 | 30.000.000 | `01_harga_laptop_gpu.md` |
| 2 | Pendirian PT + Notaris + AHU + NPWP + NIB (paket lengkap) | 1 | 7.500.000 | 7.500.000 | `07_biaya_legal_perusahaan.md` |
| 3 | Pendaftaran Merek 3 Kelas (9, 35, 42) via Konsultan | 1 | 7.500.000 | 7.500.000 | `07_biaya_legal_perusahaan.md` |
| 4 | Domicile Virtual Office Bandung (1 tahun) | 1 | 1.200.000 | 1.200.000 | `07_biaya_legal_perusahaan.md` |
| 5 | Domain .com + .id + SSL DV (1 tahun) | 1 | 560.000 | 560.000 | `07_biaya_legal_perusahaan.md` |
| 6 | Google Play Console ($25) + Apple Developer ($99/tahun) | 1 | 1.934.400 | 1.934.400 | `07_biaya_legal_perusahaan.md` |
| **Total CapEx** | | | | **48.694.400** | `research/finansial_sumber/README.md` |

**Asumsi Akuntansi:**
- Laptop dikapitalisasi sebagai aset tetap, depresiasi garis lurus 3 tahun = **Rp 10.000.000/tahun** (Rp 833.333/bulan) — **bukan pengeluaran kas** setelah pembelian awal.
- Biaya legal, merek, domain, platform fee: dibebankan saat terjadi (expense) atau dikapitalisasi sebagai intangible asset tergantung kebijakan akuntansi.
- Server fisik: **tidak dibeli** — menggunakan cloud GPU (AWS g5.xlarge) yang dicatat di OpEx.

---

---

## 17. Biaya Operasional (OpEx) — Detail

Asumsi harga pasar Oktober 2024 (sumber: `research/finansial_sumber/`):

| No | Item | Provider & Spec | Harga/Bulan (Rp) | 6 Bulan (Rp) | Sumber File |
|----|------|-----------------|------------------|--------------|-------------|
| 1 | Cloud GPU Instance | AWS g5.xlarge (1× A10G 24GB, 4 vCPU, 16 GB RAM, Jakarta, 24/7) | 13.100.000 | 78.600.000 | `02_harga_cloud_gpu.md` |
| 2 | PostgreSQL + pgvector | Supabase Pro (8 GB RAM, 100 GB SSD, 2 vCPU, PITR 7 hari) | 390.000 | 2.340.000 | `04_harga_database_redis.md` |
| 3 | Redis (Cache & Queue) | DigitalOcean Managed Redis 4 GB HA (standby node, SGP1) | 936.000 | 5.616.000 | `04_harga_database_redis.md` |
| 4 | API LLM | GPT-4o-mini (primary) + Claude 3.5 Haiku (fallback), buffer 2x | 100.000 | 600.000 | `03_harga_llm_api.md` |
| 5 | Google Maps API | Places Nearby + Details (Advanced) + Directions + Geocoding (net after $200 free) | 2.270.000 | 13.620.000 | `05_harga_google_maps.md` |
| 6 | Object Storage | S3-compatible (Supabase/DO Spaces) — estimasi < 50 GB | 50.000 | 300.000 | Asumsi internal |
| 7 | Domain + SSL (prorated) | .com + .id + DV SSL | 47.000 | 282.000 | `07_biaya_legal_perusahaan.md` |
| 8 | Apple Developer (prorated) | $99/tahun | 128.700 | 772.200 | `07_biaya_legal_perusahaan.md` |
| 9 | Domicile Bandung (prorated) | Virtual office | 100.000 | 600.000 | `07_biaya_legal_perusahaan.md` |
| 10 | Marketing Digital | Komunitas, sosmed, referral bengkel (detail Section 11) | 500.000 | 3.000.000 | Section 11 |
| **Total OpEx/Bulan** | | | **17.621.700** | **105.730.200** | `research/finansial_sumber/README.md` |

**Catatan Harga Pasar (Oktober 2024):**
- **Cloud GPU:** AWS g5.xlarge Jakarta on-demand $1.15/jam (vs US-East $1.006) × 730 jam = $839.5/bln × Rp 15.600 = **Rp 13.1M**. Reserved 1-yr: ~Rp 7.5M/bln (-43%).
- **API LLM:** GPT-4o-mini $0.15/1M input + $0.60/1M output. Estimasi 5k diagnosis/bln × 3k token in + 800 token out = 19M token in + 4M token out/bln = $2.85 + $2.40 = $5.25/bln → **Rp 82k/bln**. Buffer 2x = **Rp 100k/bln**.
- **Google Maps:** $200 free tier/bln. Estimasi 31k calls/bln (MVP) = $345 gross → $145 net × Rp 15.600 = **Rp 2.27M/bln**. Skala naik proporsional.
- **Kurs:** USD 1 = Rp 15.600 (Bank Indonesia rata-rata Oktober 2024).
- **Kontribusi tenaga sukarela (anggota):** Tidak dihitung sebagai biaya kas.

**Optimasi Biaya (Post-MVP):**
| Opsi | Hemat/Bulan | Trade-off |
|------|-------------|-----------|
| AWS g5.xlarge 1-yr Reserved | ~Rp 5.6M | Komitmen 1 tahun upfront |
| Supabase Free Tier (MVP) | Rp 390k | Limit 500 MB DB, 1 GB RAM |
| Self-host LLM (Llama 3.1 8B di laptop RTX 4070) | Rp 13.1M (hapus Cloud GPU) | Butuh DevOps, latency lokal, VRAM 8GB limit |
| OSM + PostGIS (hapus Google Maps) | Rp 2.27M | Butuh maintenance data, routing engine (OSRM) |
| **Total Potensial Hemat** | **~Rp 18.5M/bln** | Butuh resource engineering |

---

---

## 18. Proyeksi Keuangan (12 Bulan)

**Asumsi Dasar (Data-Driven):**
| Parameter | Nilai | Sumber |
|-----------|-------|--------|
| Pelanggan aktif rata-rata (Bengkel berlangganan) | Bulan 1-3: 0, Bln 4-6: 5, Bln 7-9: 15, Bln 10-12: 30 | Rencana akuisisi |
| Harga langganan bengkel/bln | Rp 200.000 (blended) | Section 10.4 |
| Pelanggan aktif rata-rata (User Premium) | Bln 1-3: 0, Bln 4-6: 50, Bln 7-9: 200, Bln 10-12: 500 | Rencana akuisisi |
| Harga langganan user/bln | Rp 35.000 (blended) | Section 10.4 |
| Fee listing bengkel premium/bln | Rp 75.000 (blended) | Section 10.4 |
| Konversi diagnosis→transaksi (CPS) | 0.3% (realistic) | `06_shopee_affiliate_cps.md` |
| Komisi per transaksi CPS | Rp 8.750 | `06_shopee_affiliate_cps.md` |
| Retensi bulanan (churn) | 5% (bengkel), 10% (user) | Asumsi industri SaaS |
| PPh 0.5% (penghasilan bruto) + PPN 11% (jika PKP) | Terhitung di cashflow | UU PPh/PPN |
| Siklus kas Shopee Affiliate | Net 30–60 hari | Kebijakan Shopee |
| Modal kerja (piutang + persediaan) | Minimal (asset-light) | Model bisnis |

**Proyeksi Revenue Bulanan (Rp):**

| Bulan | Subs Bengkel | Subs User | Listing Bengkel | CPS Affiliate | **Total Revenue** |
|-------|-------------|-----------|-----------------|---------------|-------------------|
| 1 | 0 | 0 | 0 | 0 | **0** |
| 2 | 0 | 0 | 0 | 0 | **0** |
| 3 | 0 | 0 | 0 | 52.500 | **52.500** |
| 4 | 1.000.000 (5×200k) | 1.750.000 (50×35k) | 375.000 (5×75k) | 78.750 | **3.203.750** |
| 5 | 1.000.000 | 1.750.000 | 375.000 | 91.875 | **3.216.875** |
| 6 | 1.000.000 | 1.750.000 | 375.000 | 105.000 | **3.230.000** |
| 7 | 3.000.000 (15×200k) | 7.000.000 (200×35k) | 1.125.000 (15×75k) | 118.125 | **11.243.125** |
| 8 | 3.000.000 | 7.000.000 | 1.125.000 | 131.250 | **11.256.250** |
| 9 | 3.000.000 | 7.000.000 | 1.125.000 | 144.375 | **11.269.375** |
| 10 | 6.000.000 (30×200k) | 17.500.000 (500×35k) | 2.250.000 (30×75k) | 157.500 | **25.907.500** |
| 11 | 6.000.000 | 17.500.000 | 2.250.000 | 170.625 | **25.920.625** |
| 12 | 6.000.000 | 17.500.000 | 2.250.000 | 183.750 | **25.933.750** |
| **Total 12 Bln** | **30.000.000** | **78.750.000** | **11.250.000** | **1.233.750** | **121.233.750** |

**Proyeksi Cashflow (Kas Masuk vs Keluar):**

| Bulan | Kas Masuk (Revenue) | Kas Keluar (OpEx) | Net Cashflow | Kumulatif Kas |
|-------|---------------------|-------------------|--------------|---------------|
| 0 (Setup) | 0 | 48.694.400 (CapEx) | -48.694.400 | -48.694.400 |
| 1 | 0 | 17.621.700 | -17.621.700 | -66.316.100 |
| 2 | 0 | 17.621.700 | -17.621.700 | -83.937.800 |
| 3 | 52.500 | 17.621.700 | -17.569.200 | -101.507.000 |
| 4 | 3.203.750 | 17.621.700 | -14.417.950 | -115.924.950 |
| 5 | 3.216.875 | 17.621.700 | -14.404.825 | -130.329.775 |
| 6 | 3.230.000 | 17.621.700 | -14.391.700 | -144.721.475 |
| 7 | 11.243.125 | 17.621.700 | -6.378.575 | -151.100.050 |
| 8 | 11.256.250 | 17.621.700 | -6.365.450 | -157.465.500 |
| 9 | 11.269.375 | 17.621.700 | -6.352.325 | -163.817.825 |
| 10 | 25.907.500 | 17.621.700 | +8.285.800 | -155.532.025 |
| 11 | 25.920.625 | 17.621.700 | +8.298.925 | -147.233.100 |
| 12 | 25.933.750 | 17.621.700 | +8.312.050 | **-138.921.050** |

**Kesimpulan Proyeksi (Baseline Cloud GPU):**
- **Break-even kas: BELUM TERCAPAI dalam 12 bulan** (defisit Rp 139M)
- **Titik terendah kas: Bulan 9 (Rp -163,8M)**
- **Perlu pendanaan: Minimal Rp 165M** untuk runway 12 bulan + buffer 20%

---

---

## 19. Break-Even Point (BEP) & Kebutuhan Pendanaan

### 19.1 BEP Analisis — Skenario Baseline (Full Cloud GPU)

| Parameter | Nilai |
|-----------|-------|
| Total Biaya 12 Bln (CapEx + OpEx×12) | Rp 48.694.400 + (Rp 17.621.700 × 12) = **Rp 260.154.800** |
| Total Revenue 12 Bln (Proyeksi) | **Rp 121.233.750** |
| **Defisit 12 Bln** | **Rp -138.921.050** |
| Revenue Bulanan Target BEP (12 bln) | Rp 260.154.800 / 12 = **Rp 21.679.567/bln** |
| **Gap vs Proyeksi Bln 12 (Rp 25.9M)** | Perlu **1.18x revenue** atau **kurangi OpEx 15%** |

**Kesimpulan Baseline:** BEP 12 bulan **tidak tercapai** dengan cost structure full cloud. Revenue Bln 12 (Rp 25.9M) < Target BEP (Rp 21.7M) — tapi defisit kumulatif karena biaya awal besar dan 3 bulan pertama revenue 0.

---

### 19.2 BEP Analisis — Skenario Optimasi (Post-MVP)

| Opsi Optimasi | OpEx Baru/Bulan | Hemat/Bulan | Trade-off |
|---------------|-----------------|-------------|-----------|
| AWS g5.xlarge 1-yr Reserved | Rp 7.500.000 | Rp 5.600.000 | Komitmen 1 tahun upfront ~Rp 90M |
| Supabase Free Tier (MVP) | Rp 0 | Rp 390.000 | Limit 500 MB DB, 1 GB RAM |
| Self-host LLM (Llama 3.1 8B di RTX 4070) | Rp 0 | Rp 13.100.000 | Butuh DevOps, VRAM 8GB limit |
| OSM + OSRM (hapus Google Maps) | Rp 0 | Rp 2.270.000 | Butuh maintain data, routing engine |
| **Total OpEx Optimized** | **Rp 2.161.700** | **Rp 15.460.000** | Butuh engineering resource |

**Proyeksi BEP Skenario Optimasi:**

| Parameter | Nilai |
|-----------|-------|
| Total Biaya 12 Bln (CapEx + OpEx Opt×12) | Rp 48.694.400 + (Rp 2.161.700 × 12) = **Rp 74.634.800** |
| Total Revenue 12 Bln | **Rp 121.233.750** |
| **Surplus 12 Bln** | **Rp +46.598.950** |
| BEP Bulan ke- | **Bulan 6–7** (pada Bln 6 kumulatif mendekati 0) |

**Kesimpulan Optimasi:** Dengan self-host LLM + OSM + Reserved Instance + Free Tier DB, **BEP tercapai Bulan 6–7**. Ini adalah arsitektur target **Post-MVP (Bulan 4–6)**.

---

### 19.3 Kebutuhan Pendanaan (Funding Ask)

| Skenario | Kebutuhan Dana (Rp) | Catatan |
|----------|---------------------|---------|
| **Baseline (Full Cloud, 12 bln runway + 20% buffer)** | **Rp 165.000.000** | CapEx Rp 48,7M + OpEx 12 bln Rp 211,5M - Revenue Rp 121,2M + buffer |
| **Optimasi (Self-host target Bln 4, 12 bln runway)** | **Rp 85.000.000** | CapEx Rp 48,7M + OpEx Bln 1-3 full cloud + Bln 4-12 optimized |
| **Minimal (Bootstrap + UKRI Hibah saja)** | **Rp 100.000.000** | Dana sendiri Rp 50M + UKRI Rp 50M = Rp 100M. Runway ~6 bulan full cloud. Perlu pivot ke optimasi Bln 3. |

**Struktur Penawaran (Pre-seed):**
- **Target Raise:** Rp 85.000.000 – Rp 165.000.000
- **Equity:** 10–15% (post-money valuation Rp 570M – Rp 1,1M)
- **Use of Funds:**
  - 30% CapEx (Laptop GPU, Legal, Merek)
  - 50% OpEx Bln 1–6 (Cloud GPU, Maps API, Infra)
  - 20% Marketing & Community Building

**Milestone Funding:**
| Tranche | Trigger | Amount |
|---------|---------|--------|
| Tranche 1 (Signing) | Term sheet signed | 40% |
| Tranche 2 (MVP Launch) | App di Play Store/App Store, 5 bengkel pilot aktif | 30% |
| Tranche 3 (Traction) | 100 MAU, 10 bengkel berlangganan, revenue > Rp 5M/bln | 30% |

---

## 20. Data Bengkel Bandung (Siap Integrasi)

**Sumber:** Nominatim (OpenStreetMap) — Scraped 10 November 2026 19:39 WIB

| Metrik | Nilai |
|--------|-------|
| **Total Bengkel** | 50 |
| **Kategori** | Bengkel Mobil: 38, Bengkel Motor: 12 |
| **Kecamatan** | Astanaanyar: 17, Regol: 19, Lengkong: 13, Kopo: 1 |
| **Koordinat** | Lengkap (latitude, longitude) — siap PostGIS/Haversine |
| **Jam Buka** | Tersedia untuk sebagian (contoh: B-Quik Mo-Su 09:00-21:00, Astra Otoservice Mo-Sa 09:00-21:00) |
| **Kontak** | Phone & website mayoritas kosong (karakteristik OSM) |
| **Rating/Review** | 0.0 / 0 (belum ada data review di OSM) |
| **Format File** | `bandung_bengkel_nominatim_20261110_193915.csv` (51 baris incl header) & `.json` (structured dengan metadata) |
| **Lokasi File** | `/home/zey-van-hell/Proyek/gmaps-scraper/` — akan disalin ke `data/` repo saat integrasi |

**Contoh Data (Top 5):**
1. **Sapphire Body & Paint** — Gang Aki Ahman, Ciseureuh, Kopo — Bengkel Mobil — (-6.9535581, 107.611361)
2. **Cihampelas Car Audio** — Jalan Cihampelas, Tamansari, Astanaanyar — Bengkel Mobil — (-6.90284, 107.6044983)
3. **B-Quik** — Jalan Buah Batu, Cijagra, Astanaanyar — Bengkel Mobil — Mo-Su 09:00-21:00 — (-6.9478854, 107.6328236)
4. **Astra Otoservice** — 139 Jalan Buah Batu, Turangga, Astanaanyar — Bengkel Mobil — Mo-Sa 09:00-21:00 — (-6.9371814, 107.6232631)
5. **Riau Variasi** — Jalan L.L. RE. Martadinata, Babakan Ciamis, Astanaanyar — Bengkel Mobil — (-6.9071783, 107.6100163)

**Rencana Integrasi (M3–M4):**
- Ingest CSV/JSON → PostgreSQL + PostGIS
- API `/api/v1/workshops/nearby?lat=&lng=&radius_km=&category=`
- Filter: kategori (Mobil/Motor), jam buka (buka sekarang), radius
- Response: nama, alamat, jarak, jam buka, koordinat, link OSM, kategori

---

## 21. Kesimpulan

**Otomotif Visual 3D** mengusung solusi platform AI untuk mengatasi kesulitan pemilik motor mendiagnosa kerusakan mandiri, ketergantungan pada bengkel non-transparan, dan keterbatasan visualisasi modifikasi.

**Solusi:**
- Diagnosis AI kontekstual (RAG + LLM) dengan klasifikasi tingkat keparahan, instruksi perbaikan terstruktur, dan rekomendasi suku cadang terintegrasi afiliasi Shopee
- Konfigurator 3D hybrid (Sparse-View Image-to-3D + Template-Mesh Swapping) untuk visualisasi modifikasi real-time
- Workshop Finder dengan data 50 bengkel Bandung terverifikasi (koordinat, jam buka, kategori)

**Bukti Validasi Terpenting:** **[Belum diuji]** — MVP diagnosis belum diluncurkan ke pengguna nyata. Validasi internal test case menunjukkan target akurasi > 85% [Target] dan arsitektur teknis (Next.js, FastAPI, pgvector, R3F, Celery) telah difinalisasi di dokumen **PRD, SRS, ERD, API Spec (semua v1.0, 19 Oktober 2026)**.

**Batasan:**
- Ketergantungan API LLM eksternal (OpenAI/Claude)
- Belum adanya data pengguna nyata
- Belum adanya legalitas entitas bisnis (PT/CV)
- Keahlian pemasaran/keuangan belum tersedia di tim

**Kelayakan Awal:**
- **Teknis: Layak** — Stack modern, arsitektur scalable, RAG grounding mengurangi risiko halusinasi
- **Bisnis: Passing grade** jika konversi diagnosis→transaksi > 3% [Target]. Model afiliasi CPS rendah risiko modal.

**Risiko Prioritas & Mitigasi:**
| Risiko | Mitigasi |
|--------|----------|
| (1) Akurasi diagnosis < target | Rule-based fallback, human-in-loop review (Wizard of Oz) |
| (2) Rate limit/perubahan Shopee API | Caching, fallback static catalog |
| (3) Belum tervalidasi product-market fit | Wizard of Oz MVP Minggu 4–5 dengan 20–30 early adopter komunitas motor |

**Rencana Tindak Lanjut:**
1. Luncurkan MVP diagnosis (Minggu 3) & uji pengguna (Minggu 4–5)
2. Rekrut asesor pemasaran & keuangan
3. Proses pendirian CV/PT & compliance UU PDP
4. Finalisasi pitch deck & mengajukan hibah/pendanaan pra-seed
5. Ekspansi fitur 3D & workshop finder pasca-UTS

---

## 22. Referensi Dokumen Pendukung (v1.0, 19 Oktober 2026)

Semua dokumen tersimpan di `docs/`:
- `PRD.md` — Product Requirements Document
- `SRS.md` — Software Requirements Specification
- `ERD.md` — Entity Relationship Diagram
- `API_SPEC.md` — API Specification (OpenAPI 3.0)
- `UI_UX_DESIGN.md` — UI/UX Design Specification
- `DATA_BENGKEL_BANDUNG.md` — Dokumentasi data bengkel (file ini mereferensikan CSV/JSON di `data/`)

---

*Dokumen ini disesuaikan dengan isi PRD, SRS, ERD, API Spec, dan UI/UX Design Specification yang tersimpan di `docs/`. Data bengkel Bandung terverifikasi dari Nominatim (OpenStreetMap) siap integrasi ke Workshop Service.*