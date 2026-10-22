# M1 Implementation Checklist — Database Schema PostgreSQL + pgvector

## Status: COMPLETE ✅

### Deliverables

| Item | Status | Notes |
|------|--------|-------|
| **Database Models (7 tables)** | ✅ | Vehicle, Symptom, Diagnosis, SparePart, Workshop, SymptomDiagnosisMap, DiagnosisPartMap |
| **Pydantic Schemas** | ✅ | API request/response contracts (deferred to M2 routes) |
| **FastAPI App Factory** | ✅ | `/health` endpoint + startup hooks |
| **Environment Config** | ✅ | `.env.example` + `config.py` settings |
| **Docker PostgreSQL** | ✅ | `docker-compose.yml` with pgvector 16 |
| **Alembic Migrations** | ✅ | `alembic.ini` + `env.py` + `001_initial.py` (7 tables) |
| **Seed Script** | ✅ | `backend/seed/seed.py` with test data |
| **Pytest Fixtures** | ✅ | `conftest.py` + `test_models.py` (in-memory SQLite) |
| **Dependencies** | ✅ | Fixed: psycopg2-binary 2.9.13, alembic 1.20.0 |
| **Backend README** | ✅ | Setup, structure, troubleshooting guide |

### Architecture

```
backend/
├── app/
│   ├── main.py           # FastAPI app + /health
│   ├── database.py       # SQLAlchemy session + engine
│   ├── models.py         # 7 ORM models (ERD-aligned)
│   ├── schemas.py        # Pydantic contracts (for M2)
│   └── __init__.py
├── migrations/
│   ├── env.py            # Alembic environment config
│   ├── versions/
│   │   └── 001_initial.py # Create 7 tables + associations
├── seed/
│   └── seed.py           # Test data population
├── tests/
│   ├── conftest.py       # Pytest session fixtures
│   ├── test_models.py    # Model validation tests
│   └── __init__.py
├── alembic.ini           # Migration config
├── config.py             # Environment settings
├── requirements.txt      # Dependencies
├── pytest.ini            # Test runner config
└── README.md             # Setup guide
```

### Database Schema (7 Tables)

1. **vehicles** — Kendaraan catalog (brand, model, year_start, year_end, category)
2. **symptoms** — Deskripsi gejala (symptom_code UNIQUE, description, embedding 1536-dim)
3. **diagnoses** — Hasil diagnosis (title, technical_explanation, severity_level ENUM, repair_steps JSON)
4. **spare_parts** — Suku cadang (part_name, part_number, brand, price_min/max, Shopee IDs)
5. **workshops** — Bengkel directory (name, address, latitude, longitude, rating, specialties ARRAY)
6. **symptom_diagnosis_map** — M:M linking gejala → diagnosis (confidence_weight)
7. **diagnosis_part_map** — M:M linking diagnosis → spare parts (is_primary flag)
8. **vehicle_symptom** — Association (vehicle_id, symptom_id)
9. **vehicle_workshop** — Association (vehicle_id, workshop_id)

### Key Decisions

- **UUID primary keys** — `sqlalchemy.dialects.postgresql.UUID` + `default=uuid4`
- **pgvector 1536-dim** — Symptom embeddings for RAG similarity search
- **Severity ENUM** — DIY_EASY, DIY_HARD, WORKSHOP_REQUIRED (per ERD)
- **psycopg2-binary** — Fallback from psycopg3 (Windows compatibility)
- **Migration strategy** — Manual `001_initial.py` (Alembic autogenerate issues on Windows)
- **Async deferred to M2** — ORM ready; FastAPI async routes in next milestone

### Testing

```bash
# Run model tests
pytest backend/tests/test_models.py -v

# Seed test data
python backend/seed/seed.py

# Start PostgreSQL
docker-compose up -d postgres
```

### Known Limitations (M2+)

- [ ] Async SQLAlchemy sessions (depends on sqlalchemy.ext.asyncio setup)
- [ ] JWT authentication endpoints
- [ ] Vector embedding integration (OpenAI embeddings model)
- [ ] Shopee API integration (affiliate links, price sync)
- [ ] Google Maps integration (workshop finder)
- [ ] Production database setup + backups

### Next Milestone: M2 (FastAPI Diagnosis Endpoint)

See issue #3 for details:
- `/api/v1/diagnosis/analyze` endpoint
- RAG pipeline (pgvector semantic search)
- LLM integration (OpenAI/Claude)
- Severity classification
- Integration tests

---

**Completed:** 2026-10-22  
**PR:** #17 (merged)  
**Branch:** M1-database-schema (deleted after merge)
