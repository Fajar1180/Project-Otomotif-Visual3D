# Diagram Relasi Entitas (ERD)
## Platform Otomotif AI (Project Pak Yogi)

### Ikhtisar
ERD memvisualisasikan skema database untuk platform Otomotif AI, menghubungkan kendaraan, gejala, diagnosis, suku cadang, dan bengkel melalui tabel mapping.

### Diagram (Mermaid)

```mermaid
erDiagram
    VEHICLES ||--|{ SYMPTOM_DIAGNOSIS_MAP : maps
    VEHICLES {
        UUID id PK
        VARCHAR(50) brand
        VARCHAR(100) model
        INT year_start
        INT year_end
        VARCHAR(30) category
    }

    SYMPTOMS ||--|{ SYMPTOM_DIAGNOSIS_MAP : relates_to
    SYMPTOMS {
        UUID id PK
        VARCHAR(20) symptom_code UNIQUE
        TEXT description
        VARCHAR(50) category
        VECTOR(1536) embedding
    }

    DIAGNOSES ||--|{ SYMPTOM_DIAGNOSIS_MAP : diagnosed_from
    DIAGNOSES {
        UUID id PK
        VARCHAR(150) title
        TEXT technical_explanation
        VARCHAR(20) severity_level
        JSONB repair_steps
    }

    SPARE_PARTS ||--|{ DIAGNOSIS_PART_MAP : linked_to
    SPARE_PARTS {
        UUID id PK
        VARCHAR(150) part_name
        VARCHAR(50) part_number
        VARCHAR(50) brand
        NUMERIC(12,2) price_min
        NUMERIC(12,2) price_max
        VARCHAR(50) shopee_item_id
        VARCHAR(50) shopee_shop_id
        TEXT default_shopee_url
    }

    DIAGNOSES ||--|{ DIAGNOSIS_PART_MAP : triggers
    DIAGNOSES {
        UUID id PK
        VARCHAR(150) title
        TEXT technical_explanation
        VARCHAR(20) severity_level
        JSONB repair_steps
    }

    WORKSHOPS {
        UUID id PK
        VARCHAR(100) name
        TEXT address
        DOUBLE PRECISION latitude
        DOUBLE PRECISION longitude
        NUMERIC(2,1) rating
        TEXT[] specialties
    }

    SYMPTOM_DIAGNOSIS_MAP {
        UUID symptom_id PK,FK
        UUID diagnosis_id PK,FK
        FLOAT confidence_weight
    }

    DIAGNOSIS_PART_MAP {
        UUID diagnosis_id PK,FK
        UUID spare_part_id PK,FK
        BOOLEAN is_primary
    }

    VEHICLES }o--o{ WORKSHOPS : served_by (via vehicle category)
```

### Detail Relasi

| Relasi | Deskripsi |
|--------------|-------------|
| **Vehicle → Symptom Diagnosis Map** | Menghubungkan kendaraan ke mapping gejala→diagnosis via filter kategori kendaraan |
| **Symptoms → Symptom Diagnosis Map** | Many-to-many linking kode gejala ke diagnosis dengan bobot kepercayaan |
| **Diagnoses → Symptom Diagnosis Map** | Setiap diagnosis terhubung ke satu atau lebih kode gejala |
| **Diagnoses → Diagnosis Part Map** | Menghubungkan diagnosis ke suku cadang yang direkomendasikan (primary vs secondary) |
| **Spare Parts → Diagnosis Part Map** | Banyak suku cadang dapat dikaitkan dengan banyak diagnosis |
| **Workshops** | Entitas independen menyimpan lokasi bengkel dan spesialisasi |
| **Vehicle ↔ Workshops** | Relasi konseptual: bengkel yang melayani kategori kendaraan tertentu |

### Observasi Kunci
- Skema menggunakan UUID sebagai primary key untuk semua entitas
- Vector embeddings disimpan di `symptoms.embedding` (1536 dimensi) untuk similarity search RAG
- `severity_level` dibatasi ke nilai enum: DIY_EASY, DIY_HARD, WORKSHOP_REQUIRED
- `repair_steps` disimpan sebagai JSONB untuk deskripsi langkah yang fleksibel
- `specialties` di workshops adalah array text PostgreSQL untuk filtering tipe kendaraan
- Semua foreign key meng-enforce referential integrity dengan opsi CASCADE delete (implisit)

---
*Versi Dokumen 1.0 | Dibuat: 19 Oktober 2026*