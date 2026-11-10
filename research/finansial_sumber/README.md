# Research Finansial — Index Sumber Data Terverifikasi

## Struktur Folder
```
research/finansial_sumber/
├── 01_harga_laptop_gpu.md              # Laptop RTX 4070/4080 Indonesia
├── 02_harga_cloud_gpu.md               # Cloud GPU (AWS, GCP, DO, RunPod)
├── 03_harga_llm_api.md                 # OpenAI & Anthropic API pricing
├── 04_harga_database_redis.md          # PostgreSQL & Redis managed
├── 05_harga_google_maps.md             # Google Maps Platform API
├── 06_shopee_affiliate_cps.md          # Shopee Affiliate CPS Indonesia
├── 07_biaya_legal_perusahaan.md        # Pendirian PT, Merek, Domicile, SSL
└── README.md                           # File ini
```

---

## Ringkasan Nilai Kunci untuk Proposal (CapEx + OpEx 6 Bulan)

### CapEx (One-time / Setup)

| Item | Nilai (Rp) | Sumber File | Baris/Section |
|------|------------|-------------|---------------|
| **Laptop Development GPU (RTX 4070 class)** | **30.000.000** | `01_harga_laptop_gpu.md` | Kesimpulan |
| **Pendirian PT + Notaris + AHU + NPWP + NIB** | **7.500.000** | `07_biaya_legal_perusahaan.md` | Opsi B Standard |
| **Merek 3 Kelas (9, 35, 42) via Konsultan** | **7.500.000** | `07_biaya_legal_perusahaan.md` | Opsi B Standard |
| **Domicile Bandung 1 Tahun** | **1.200.000** | `07_biaya_legal_perusahaan.md` | Rekomendasi |
| **Domain .com + .id + SSL DV 1 Tahun** | **560.000** | `07_biaya_legal_perusahaan.md` | Domain + SSL |
| **Google Play + Apple Developer 1 Tahun** | **1.934.400** | `07_biaya_legal_perusahaan.md` | Platform fees |
| **Total CapEx** | **48.694.400** | | **≈ Rp 48,7 Juta** |

---

### OpEx Bulanan (Recurring)

| Item | Nilai/Bulan (Rp) | Sumber File | Catatan |
|------|------------------|-------------|---------|
| **Cloud GPU (AWS g5.xlarge Jakarta 24/7)** | **13.100.000** | `02_harga_cloud_gpu.md` | Production inference LLM 7B-13B |
| **PostgreSQL (Supabase Pro)** | **390.000** | `04_harga_database_redis.md` | 8 GB RAM, 100 GB SSD |
| **Redis (DigitalOcean 4 GB HA)** | **936.000** | `04_harga_database_redis.md` | Cache + session |
| **LLM API (GPT-4o-mini + Haiku fallback)** | **100.000** | `03_harga_llm_api.md` | Buffer 2x realistic |
| **Google Maps API (net after $200 free)** | **2.270.000** | `05_harga_google_maps.md` | Places + Directions + Geocoding |
| **Domicile Bandung (prorated)** | **100.000** | `07_biaya_legal_perusahaan.md` | 1.200.000 / 12 |
| **Domain/SSL (prorated)** | **47.000** | `07_biaya_legal_perusahaan.md` | 560.000 / 12 |
| **Apple Developer (prorated)** | **128.700** | `07_biaya_legal_perusahaan.md` | 1.544.400 / 12 |
| **Total OpEx/Bulan** | **17.071.700** | | **≈ Rp 17,1 Juta/bln** |

---

### OpEx 6 Bulan Total
**Rp 17.071.700 × 6 = Rp 102.430.200** ≈ **Rp 102,4 Juta**

---

### Total CapEx + OpEx 6 Bulan
**Rp 48,7 Juta + Rp 102,4 Juta = Rp 151,1 Juta** ≈ **Rp 151 Juta**

---

### Revenue Streams (Actual Data)

| Stream | Sumber | Estimasi Realistis/Bulan |
|--------|--------|--------------------------|
| **Stream 1: Premium Subscription** | Proposal assumption | Bengkel: Rp 150.000-300.000 × 20 bengkel = **Rp 3-6 Juta** |
| **Stream 2: Listing Fee Bengkel** | Proposal assumption | Rp 50.000-100.000 × 50 bengkel = **Rp 2,5-5 Juta** |
| **Stream 3: CPS Shopee Affiliate** | `06_shopee_affiliate_cps.md` | **Rp 131.250** (15 transaksi × Rp 8.750) |
| **Total Revenue/Bulan (Realistic)** | | **Rp 5,6 - 11,1 Juta** |

---

### Break-Even Analysis (Data-Driven)

| Parameter | Nilai |
|-----------|-------|
| **Total Biaya 12 Bulan (CapEx + OpEx×12)** | Rp 48,7M + (Rp 17,1M × 12) = **Rp 253,9 M** |
| **Revenue Bulanan Target BEP 12 Bln** | Rp 253,9M / 12 = **Rp 21,2 M/bln** |
| **Gap vs Realistic Revenue (Rp 11,1 M)** | Perlu **2x revenue** atau **kurangi OpEx 50%** |
| **Strategi BEP:** | 1. Cloud GPU → Self-host (RTX 4070 laptop) hemat Rp 13,1M/bln<br>2. Maps API → OSM self-host hemat Rp 2,27M/bln<br>3. Supabase Pro → Free tier (MVP) hemat Rp 390k/bln<br>4. **OpEx Optimized = Rp 1,3M/bln** → BEP achievable |

---

## Cara Menggunakan di Proposal

Setiap angka di proposal yang sebelumnya `[DATA DIBUTUHKAN]` sekarang bisa direferensikan ke file sumber:

```markdown
| Laptop GPU RTX 4070 | Rp 30.000.000 | `research/finansial_sumber/01_harga_laptop_gpu.md` |
| Cloud GPU AWS g5.xlarge (6 bln) | Rp 78.600.000 | `research/finansial_sumber/02_harga_cloud_gpu.md` |
| LLM API GPT-4o-mini (6 bln) | Rp 600.000 | `research/finansial_sumber/03_harga_llm_api.md` |
| Supabase Pro (6 bln) | Rp 2.340.000 | `research/finansial_sumber/04_harga_database_redis.md` |
| Redis DO 4GB HA (6 bln) | Rp 5.616.000 | `research/finansial_sumber/04_harga_database_redis.md` |
| Google Maps API (6 bln net) | Rp 13.620.000 | `research/finansial_sumber/05_harga_google_maps.md` |
| Pendirian PT + Legal | Rp 16.200.000 | `research/finansial_sumber/07_biaya_legal_perusahaan.md` |
| CPS Shopee Affiliate Revenue | Rp 131.250/bln | `research/finansial_sumber/06_shopee_affiliate_cps.md` |
```

---

## Tanggal Verifikasi Terakhir
**Oktober 2024** — Semua harga diambil dari official pricing page masing-masing provider, dikonversi ke IDR dengan kurs Bank Indonesia Rp 15.600/USD (rata-rata Oktober 2024).

## Catatan
- Harga cloud & API bisa berubah kapan saja — **lock-in pricing** via reserved instances / committed use discounts bila memungkinkan.
- Harga laptop fluktuatif — beli saat promo (11.11, 12.12, hari belanja nasional).
- Biaya notaris/merek bervariasi per kota — gunakan jasa online untuk transparansi harga.