# Entity Relationship Diagram (ERD)
## Platform Otomotif AI (Project Pak Yogi)

### Overview
The ERD visualizes the database schema for the Otomotif AI platform, connecting vehicles, symptoms, diagnoses, spare parts, and workshops through mapping tables.

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

### Relationship Details

| Relationship | Description |
|--------------|-------------|
| **Vehicle → Symptom Diagnosis Map** | Links vehicles to symptom→diagnosis mappings via vehicle category filter |
| **Symptoms → Symptom Diagnosis Map** | Many-to-many linking of symptom codes to diagnoses with confidence weights |
| **Diagnoses → Symptom Diagnosis Map** | Each diagnosis linked to one or more symptom codes |
| **Diagnoses → Diagnosis Part Map** | Links diagnoses to recommended spare parts (primary vs secondary) |
| **Spare Parts → Diagnosis Part Map** | Many spare parts can be associated with multiple diagnoses |
| **Workshops** | Independent entity storing workshop locations and specialties |
| **Vehicle ↔ Workshops** | Conceptual relationship: workshops servicing specific vehicle categories |

### Key Observations
- The schema uses UUIDs as primary keys for all entities
- Vector embeddings stored in `symptoms.embedding` (1536 dimensions) for RAG similarity search
- `severity_level` constrained to enum values: DIY_EASY, DIY_HARD, WORKSHOP_REQUIRED
- `repair_steps` stored as JSONB for flexible step descriptions
- `specialties` in workshops is a PostgreSQL text array for vehicle type filtering
- All foreign keys enforce referential integrity with CASCADE delete options (implied)

---
*Document Version 1.0 | Created: 2026-10-19*