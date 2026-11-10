# Data Bengkel Bandung — Dokumentasi

## Sumber Data
- **Sumber:** Nominatim (OpenStreetMap)
- **Tanggal Scraping:** 10 November 2026 19:39:15 WIB
- **Tool:** gmaps-scraper (internal)
- **Area Coverage:** 4 kecamatan Kota Bandung

## File
| File | Ukuran | Format | Deskripsi |
|------|--------|--------|-----------|
| `bandung_bengkel_nominatim_20261110_193915.csv` | 13 KB | CSV | Full data dengan header, 51 baris (1 header + 50 data) |
| `bandung_bengkel_nominatim_20261110_193915.json` | 33 KB | JSON | Structured dengan metadata (scraped_at, source, areas, total_count, by_area, places[]) |

## Statistik Ringkas
| Metrik | Nilai |
|--------|-------|
| **Total Bengkel** | 50 |
| **Kategori** | Bengkel Mobil: 38, Bengkel Motor: 12 |
| **Kecamatan** | Astanaanyar: 17, Regol: 19, Lengkong: 13, Kopo: 1 |
| **Koordinat** | 100% lengkap (latitude, longitude) |
| **Jam Buka** | Parsial (beberapa bengkel memiliki `opening_hours.raw`) |
| **Kontak** | Phone & website mayoritas kosong (karakteristik OSM) |
| **Rating/Review** | 0.0 / 0 (belum ada data review di OSM) |

## Skema CSV
```csv
name,address,phone,website,rating,review_count,category,latitude,longitude,place_id,url,opening_hours,photos,price_level,plus_code,description,scraped_at,source,kecamatan
```

## Skema JSON (places[])
```json
{
  "name": "string",
  "address": "string",
  "phone": "string",
  "website": "string",
  "rating": "float",
  "review_count": "int",
  "category": "string",  // "Bengkel Mobil" | "Bengkel Motor"
  "latitude": "float",
  "longitude": "float",
  "place_id": "string",  // "nominatim/{osm_id}"
  "url": "string",       // OSM URL
  "opening_hours": "object",  // {"raw": "Mo-Su 09:00-21:00"} atau {}
  "photos": "array",
  "price_level": "int",
  "plus_code": "string",
  "description": "string",
  "scraped_at": "ISO8601 datetime",
  "source": "nominatim",
  "kecamatan": "string"  // "astanaanyar" | "regol" | "lengkong" | "kopo"
}
```

## Contoh Data (5 Sampel)
| No | Nama | Alamat | Kategori | Koordinat | Jam Buka | Kecamatan |
|----|------|--------|----------|-----------|----------|-----------|
| 1 | Sapphire Body & Paint | Gang Aki Ahman, Ciseureuh | Bengkel Mobil | -6.9535581, 107.611361 | - | kopo |
| 2 | Cihampelas Car Audio | Jalan Cihampelas, Tamansari | Bengkel Mobil | -6.90284, 107.6044983 | - | astanaanyar |
| 3 | B-Quik | Jalan Buah Batu, Cijagra | Bengkel Mobil | -6.9478854, 107.6328236 | Mo-Su 09:00-21:00 | astanaanyar |
| 4 | Astra Otoservice | 139 Jalan Buah Batu, Turangga | Bengkel Mobil | -6.9371814, 107.6232631 | Mo-Sa 09:00-21:00 | astanaanyar |
| 5 | Riau Variasi | Jalan L.L. RE. Martadinata, Babakan Ciamis | Bengkel Mobil | -6.9071783, 107.6100163 | - | astanaanyar |

## Rencana Integrasi ke Workshop Service (M3–M4)

### 1. Ingest ke Database
```sql
-- Tabel target (PostgreSQL + PostGIS)
CREATE TABLE workshops (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    address TEXT,
    phone VARCHAR(50),
    website VARCHAR(255),
    rating DECIMAL(2,1),
    review_count INT,
    category VARCHAR(50),  -- 'Bengkel Mobil' | 'Bengkel Motor'
    location GEOGRAPHY(POINT, 4326),  -- PostGIS
    place_id VARCHAR(100),
    osm_url VARCHAR(255),
    opening_hours JSONB,
    kecamatan VARCHAR(50),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Index spasial
CREATE INDEX idx_workshops_location ON workshops USING GIST (location);
```

### 2. API Endpoint
```
GET /api/v1/workshops/nearby
  ?lat={float}&lng={float}&radius_km={int}&category={Bengkel Mobil|Bengkel Motor}&open_now={true|false}
```

### 3. Query Contoh (PostGIS)
```sql
SELECT name, address, category,
       ST_Distance(location, ST_MakePoint(:lng, :lat)::geography) / 1000 AS distance_km,
       opening_hours
FROM workshops
WHERE ST_DWithin(location, ST_MakePoint(:lng, :lat)::geography, :radius_km * 1000)
  AND (:category IS NULL OR category = :category)
  AND (:open_now = false OR (opening_hours->>'raw') IS NOT NULL)
ORDER BY distance_km
LIMIT 20;
```

### 4. Response Format
```json
{
  "workshops": [
    {
      "name": "B-Quik",
      "address": "Jalan Buah Batu, Cijagra, Kota Bandung, 40266",
      "category": "Bengkel Mobil",
      "distance_km": 1.2,
      "location": {"lat": -6.9478854, "lng": 107.6328236},
      "opening_hours": {"raw": "Mo-Su 09:00-21:00"},
      "osm_url": "https://www.openstreetmap.org/way/1331394928",
      "kecamatan": "astanaanyar"
    }
  ],
  "total": 1,
  "center": {"lat": -6.93, "lng": 107.62},
  "radius_km": 5
}
```

## Catatan & Keterbatasan
1. **Phone/Website kosong** — OSM Nominatim jarang mengandung kontak bisnis. Perlu enrichments dari Google Places API / manual.
2. **Rating 0.0** — OSM tidak menyimpan rating/review. Perlu data eksternal (Google Maps, dll).
3. **Opening hours parsial** — Hanya ~20% bengkel memiliki jam buka. Default: asumsi buka jam kerja normal.
4. **Kategori biner** — Hanya "Bengkel Mobil" & "Bengkel Motor". Perlu refinemen: bengkel resmi, bengkel keliling, spesialis (body repair, engine, dll).
5. **Cakupan geografis** — Hanya 4 kecamatan Bandung. Perlu ekspansi ke kota lain untuk production.

## Next Steps
- [ ] Enrich phone/website via Google Places API (butuh API key & budget)
- [ ] Tambah rating/review dari Google Maps / user-generated
- [ ] Normalisasi kategori (bengkel resmi, independen, spesialis)
- [ ] Ekspansi cakupan: Jabodetabek, Surabaya, Medan, dll
- [ ] Build ingestion script (CSV/JSON → PostgreSQL + PostGIS)
- [ ] Unit test spatial query (Haversine vs PostGIS performance)

---

*File ini mereferensikan data mentah di `data/bandung_bengkel_nominatim_20261110_193915.{csv,json}`. Proposal utama: `docs/proposal/PROPOSAL_PENGAJUAN_STARTUP_DIGITAL.md` Section 20.*