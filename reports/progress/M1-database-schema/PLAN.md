# M1 Sprint Plan: Database Schema & Infrastructure

**Issue:** #2 — M1-Backend: Implementasi Database Schema PostgreSQL + pgvector  
**Branch:** M1-database-schema  
**Status:** Planning  

## Scope

Establish backend infrastructure and database layer:
- PostgreSQL 14+ with pgvector extension
- SQLAlchemy ORM with Alembic migrations
- Core domain models (User, Vehicle, DiagnosticResult, Recommendation, VectorStore)
- Development setup (requirements.txt, config, docker-compose.yml)
- Seed script for test data

## Deliverables

1. **backend/requirements.txt** — FastAPI, SQLAlchemy, Alembic, psycopg[binary], pgvector, pytest
2. **backend/config.py** — Database URI, environment config
3. **backend/app/models.py** — SQLAlchemy models (6 tables)
4. **backend/app/schemas.py** — Pydantic schemas for API contracts
5. **backend/migrations/** — Alembic migrations (init + create schema)
6. **backend/seed/seed.py** — Test data seeding
7. **docker-compose.yml** — PostgreSQL + pgvector container
8. **backend/app/database.py** — Session factory, connection pool

## Database Schema (from ERD)

| Table | Purpose |
|-------|---------|
| users | Authentication, profiles |
| vehicles | User vehicle inventory |
| diagnostic_results | AI diagnosis history + vector embeddings |
| recommendations | Suku cadang suggestions (Shopee links) |
| workshops | Bengkel directory (Maps integration) |
| vector_store | pgvector embeddings cache |

## Acceptance Criteria

- [ ] PostgreSQL + pgvector running locally (docker-compose)
- [ ] All 6 models defined + validated
- [ ] Initial Alembic migration creates schema
- [ ] Seed script populates 10+ test records per table
- [ ] All tests pass (`pytest backend/tests/`)
- [ ] `.env.example` provided (no secrets committed)

## Timeline

- **Day 1:** requirements.txt, config, models, schemas
- **Day 2:** Alembic setup, migrations, seed script
- **Day 3:** Docker, tests, PR review + merge

## Risks

- pgvector extension install in Docker
- SQLAlchemy async session setup (for FastAPI async routes — deferred to M2)
- Migration versioning strategy

## Notes

- Use TDD where applicable (model validation tests)
- Follow SRS constraints (PostgreSQL 14+, Python 3.8+)
- No API endpoints in M1 (database layer only)
