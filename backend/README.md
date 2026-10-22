# Backend Documentation

## Overview

FastAPI backend for Otomotif AI platform. Provides REST API for vehicle diagnostics, 3D model generation, and recommendation engine.

## Tech Stack

- **Framework:** FastAPI (async/await)
- **ORM:** SQLAlchemy 2.0 with async support (M2+)
- **Database:** PostgreSQL 14+ with pgvector extension
- **Migrations:** Alembic
- **Testing:** pytest + pytest-asyncio
- **Auth:** JWT (M2)

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app factory
│   ├── database.py          # SQLAlchemy session + engine
│   ├── models.py            # ORM models (6 tables)
│   ├── schemas.py           # Pydantic request/response schemas
│   ├── routes/              # API endpoints (M2+)
│   ├── services/            # Business logic (M2+)
│   └── utils/               # Helpers (M2+)
├── migrations/              # Alembic migrations (M1+)
├── seed/
│   └── seed.py              # Test data seeding
├── tests/
│   ├── conftest.py          # Pytest fixtures
│   ├── test_models.py       # Model tests
│   └── test_routes/         # Route tests (M2+)
├── config.py                # Settings (environment-aware)
├── requirements.txt         # Python dependencies
└── pytest.ini               # Pytest config
```

## Setup

### 1. Install Dependencies

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Start PostgreSQL (Docker)

```bash
docker-compose up -d postgres
# Wait for healthcheck to pass
sleep 5
```

### 3. Create `.env` from `.env.example`

```bash
cp .env.example .env
# Edit .env if using custom credentials
```

### 4. Run Migrations & Seed Data

```bash
# (M1 placeholder: manual schema creation via models.py)
python -m seed.seed  # Populate test data
```

### 5. Run Tests

```bash
pytest
```

### 6. Start API Server (M2+)

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Visit `http://localhost:8000/docs` for interactive API docs (Swagger UI).

## Database Models

| Table | Purpose | Relationships |
|-------|---------|---------------|
| **users** | Authentication & profiles | 1→N vehicles, diagnostics |
| **vehicles** | User vehicle inventory | N→1 user, 1→N diagnostics |
| **diagnostic_results** | AI diagnosis history | N→1 user/vehicle, 1→N recommendations, vector embedding |
| **recommendations** | Parts & services | N→1 diagnostic, Shopee links |
| **workshops** | Bengkel directory | Standalone (Google Maps integration) |
| **vector_store** | RAG knowledge base | Vector embeddings for semantic search |

## Development Workflow

### Adding New Endpoints (M2+)

1. Define schema in `app/schemas.py`
2. Create route in `app/routes/<feature>.py`
3. Write tests in `backend/tests/test_routes/`
4. Add business logic in `app/services/`

### Running Specific Tests

```bash
pytest backend/tests/test_models.py::test_create_user -v
```

## Environment Variables

See `.env.example` for full list:
- `DATABASE_URL` — PostgreSQL connection string
- `DEBUG` — Enable debug mode (development only)
- `ENVIRONMENT` — "development", "staging", "production"
- `SECRET_KEY` — JWT signing key (M2+)

## Troubleshooting

### pgvector Extension Not Found

```bash
docker exec otomotif_ai_db psql -U postgres -c "CREATE EXTENSION IF NOT EXISTS vector;"
```

### Database Connection Refused

Ensure PostgreSQL container is running:

```bash
docker ps | grep postgres
docker-compose logs postgres  # Check logs
```

### Tests Fail with Import Errors

Ensure you're in the project root and dependencies are installed:

```bash
python -m pip install -r backend/requirements.txt
```

## Next Steps (M2+)

- [ ] Async SQLAlchemy session setup
- [ ] JWT authentication endpoints
- [ ] Diagnosis endpoint integration
- [ ] Vector embedding integration (RAG)
- [ ] Shopee & Google Maps APIs
- [ ] Production database setup
