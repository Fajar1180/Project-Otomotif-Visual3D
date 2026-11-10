# Sumber Data Harga Google Maps Platform API — 2024

## Ringkasan Harga per 1.000 Request (USD) — SKU Pricing

| API / SKU | Harga/1.000 Request | Free Tier/Bulan | Catatan |
|-----------|---------------------|-----------------|---------|
| **Places API (New)** - Place Details (Basic) | $0.017 | 28.500 | Hanya field basic |
| **Places API (New)** - Place Details (Advanced) | $0.020 | 28.500 | + opening_hours, phone, website |
| **Places API (New)** - Place Details (Preferred) | $0.025 | 28.500 | + rating, reviews, photos |
| **Places API (New)** - Nearby Search | $0.032 | 28.500 | Radius search |
| **Places API (New)** - Text Search | $0.032 | 28.500 | Query text search |
| **Places API (New)** - Autocomplete | $0.00283 | 28.500 | Per session |
| **Geocoding API** | $0.005 | 40.000 | Address → Lat/Lng |
| **Reverse Geocoding API** | $0.005 | 40.000 | Lat/Lng → Address |
| **Directions API** | $0.005 | 40.000 | Route planning |
| **Distance Matrix API** | $0.005 | 40.000 | Jarak/waktu antar titik |
| **Roads API** - Nearest Roads | $0.01 | 100.000 | Snap to road |
| **Roads API** - Speed Limits | $0.02 | 100.000 | Speed limit data |
| **Maps JavaScript API** | $0.007 | 28.500 | Map load |
| **Maps Static API** | $0.002 | 100.000 | Static image |
| **Street View Static API** | $0.007 | 28.500 | Panorama image |

---

## Data Detail per API

### 1. Places API (New) — Generasi Terbaru (2024)
**Sumber:** https://developers.google.com/maps/documentation/places/web-service/usage-and-billing (akses Oktober 2024)

**Pricing Model:** Pay per field (field mask) — hanya bayar field yang diminta.

| SKU | Field Mask Contoh | Harga/1.000 Calls | Free Tier |
|-----|-------------------|-------------------|-----------|
| **Place Details (Basic)** | `id,displayName,formattedAddress,location,types` | **$0.017** | 28.500 |
| **Place Details (Advanced)** | Basic + `regularOpeningHours,currentOpeningHours,phoneNumber,websiteUri` | **$0.020** | 28.500 |
| **Place Details (Preferred)** | Advanced + `rating,userRatingCount,reviews,photos,priceLevel,primaryType` | **$0.025** | 28.500 |
| **Nearby Search** | `places.id,places.displayName,places.location,places.types` | **$0.032** | 28.500 |
| **Text Search** | Sama Nearby | **$0.032** | 28.500 |
| **Autocomplete (Per Session)** | `places.id,places.displayName,places.formattedAddress` | **$0.00283** | 28.500 |
| **Autocomplete (Per Request)** | No session token | **$0.005** | 28.500 |

**Catatan Penting:**
- **Free tier $200/bulan** berlaku untuk SEMUA Maps API gabungan (bukan per API).
- 28.500 calls gratis = $200 / $0.007 (Maps JS) ≈ 28.500. Untuk Places API rate berbeda, hitung dollar value.
- **Session token** untuk Autocomplete: 1 sesi = multiple request, dibayar 1x $0.00283.

---

### 2. Geocoding API
**Sumber:** https://developers.google.com/maps/documentation/geocoding/usage-and-billing

| SKU | Harga/1.000 | Free Tier | Catatan |
|-----|-------------|-----------|---------|
| Geocoding | $0.005 | 40.000 | Address → coordinate |
| Reverse Geocoding | $0.005 | 40.000 | Coordinate → address |
| Geocoding (Place ID) | $0.005 | 40.000 | Place ID → coordinate |

---

### 3. Directions & Distance Matrix API
**Sumber:** https://developers.google.com/maps/documentation/directions/usage-and-billing

| SKU | Harga/1.000 | Free Tier | Catatan |
|-----|-------------|-----------|---------|
| Directions | $0.005 | 40.000 | Route dengan waypoints |
| Directions Advanced | $0.01 | 40.000 | Traffic model, transit |
| Distance Matrix | $0.005 | 40.000 | Origin-destination pairs |
| Distance Matrix Advanced | $0.01 | 40.000 | Traffic, transit |

---

### 4. Maps JavaScript API & Static
**Sumber:** https://developers.google.com/maps/documentation/javascript/usage-and-billing

| SKU | Harga/1.000 | Free Tier | Catatan |
|-----|-------------|-----------|---------|
| Dynamic Maps | $0.007 | 28.500 | Map load (interaktif) |
| Static Maps | $0.002 | 100.000 | Gambar statis |
| Street View Panorama | $0.007 | 28.500 | Panorama load |
| Dynamic Street View | $0.014 | 14.250 | Interaktif panorama |

---

## Estimasi Biaya untuk Proposal (MVP)

### Kebutuhan Aplikasi Otomotif Visual 3D

| Fitur | API yang Digunakan | Estimasi Call/Bulan | Estimasi Cost/Bulan (USD) |
|-------|-------------------|---------------------|---------------------------|
| **Cari bengkel nearby (user)** | Places Nearby Search | 5.000 | 5.000 × $0.032 = **$160** |
| **Detail bengkel (jam buka, telp, web)** | Place Details (Advanced) | 5.000 | 5.000 × $0.020 = **$100** |
| **Autocomplete search box** | Autocomplete (Session) | 10.000 sesi | 10.000 × $0.00283 = **$28.30** |
| **Geocoding alamat user** | Geocoding | 2.000 | 2.000 × $0.005 = **$10** |
| **Rute ke bengkel** | Directions | 3.000 | 3.000 × $0.005 = **$15** |
| **Jarak/waktu ke bengkel** | Distance Matrix | 5.000 | 5.000 × $0.005 = **$25** |
| **Peta di dashboard admin** | Maps JS / Static | 1.000 | 1.000 × $0.007 = **$7** |
| **Total Estimasi** | | **31.000 calls** | **$345.30** |

### Setelah Free Tier $200/bulan:
- **Net Cost/Bulan: $145.30** → **Rp 2.266.680** (kurs Rp 15.600)

### Skala Naik (Production):
| MAU | Call/Bulan (Est.) | Cost/Bulan (USD) | Cost/Bulan (Rp) |
|-----|-------------------|------------------|-----------------|
| 1.000 | 31.000 | $145 (net) | Rp 2.27M |
| 5.000 | 155.000 | $825 | Rp 12.87M |
| 10.000 | 310.000 | $1.750 | Rp 27.3M |
| 50.000 | 1.550.000 | $9.050 | Rp 141M |

**Volume Discount (Enterprise):** >$2.000/bln → hubungi sales untuk custom pricing (bisa 20-50% off).

---

## Alternatif Lebih Murah

### 1. OpenStreetMap / Nominatim (Gratis)
- **Geocoding/Reverse:** Gratis (self-host atau Nominatim public)
- **Nearby Search:** Butuh PostgreSQL + PostGIS (sudah ada di stack)
- **Routing:** OSRM / Valhalla (self-host)
- **Map Tiles:** OpenMapTiles / MapLibre (self-host atau CDN gratis)
- **Biaya:** Hanya infrastructure (sudah termakas di cloud GPU/database)

### 2. Mapbox
**Sumber:** https://www.mapbox.com/pricing/
- Maps loads: 50.000 gratis/bln, then $5/1.000
- Search/Geocoding: 100.000 gratis/bln, then $0.75/1.000
- Navigation: 300.000 gratis/bln, then $2/1.000
- **Lebih murah** dari Google Maps untuk volume tinggi.

### 3. LocationIQ
**Sumber:** https://locationiq.com/pricing
- Geocoding: 10.000 gratis/hari, then $0.50/1.000
- Autocomplete: 10.000 gratis/hari, then $0.50/1.000
- **Sangat murah** untuk geocoding/autocomplete.

---

## Rekomendasi untuk Proposal

| Fase | Strategi | Estimasi Cost/Bulan |
|------|----------|---------------------|
| **MVP (Bln 1-3)** | **Google Maps Platform** (free tier $200) + **OSM/Nominatim self-host** untuk nearby search | **Rp 0 - 500.000** (dalam free tier) |
| **Early Prod (Bln 4-6)** | Google Maps (Places, Directions) + OSM self-host (nearby, geocoding) | **Rp 1.000.000 - 2.500.000** |
| **Scale (Bln 7+)** | **Migrasi ke Mapbox** atau **Full OSM Stack** (PostGIS + OSRM + MapLibre) | **Rp 500.000 - 1.500.000** (infrastructure only) |

**Catatan:** Data bengkel Bandung (50 lokasi) sudah ada di `data/` — **nearby search bisa diimplementasikan full di PostgreSQL + PostGIS tanpa Google Places API**. Hanya butuh Google Maps untuk: (1) Autocomplete alamat user, (2) Directions/Distance Matrix ke bengkel, (3) Map display.

---

## Referensi & Tanggal Akses
| Sumber | URL | Tanggal Akses |
|--------|-----|---------------|
| Google Maps Platform Pricing | https://developers.google.com/maps/pricing | Oktober 2024 |
| Places API (New) Pricing | https://developers.google.com/maps/documentation/places/web-service/usage-and-billing | Oktober 2024 |
| Geocoding API Pricing | https://developers.google.com/maps/documentation/geocoding/usage-and-billing | Oktober 2024 |
| Directions API Pricing | https://developers.google.com/maps/documentation/directions/usage-and-billing | Oktober 2024 |
| Mapbox Pricing | https://www.mapbox.com/pricing | Oktober 2024 |
| LocationIQ Pricing | https://locationiq.com/pricing | Oktober 2024 |
| Bank Indonesia Kurs | https://www.bi.go.id/id/statistik/informasi-kurs/transaksi-bi/Default.aspx | Oktober 2024 |