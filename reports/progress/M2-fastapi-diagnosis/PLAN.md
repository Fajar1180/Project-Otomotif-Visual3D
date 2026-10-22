# M2 Implementation Plan — FastAPI Diagnosis Endpoint + RAG

## Overview

Implement POST `/api/v1/diagnosis/analyze` endpoint with:
- Request validation (symptom description + vehicle info)
- RAG pipeline (pgvector semantic search + LLM)
- Severity classification (DIY_EASY / DIY_HARD / WORKSHOP_REQUIRED)
- Recommendation engine (spare parts from Shopee)
- Response in JSON with diagnosis, steps, parts, confidence

## Deliverables

### 1. Async SQLAlchemy Setup
- [ ] `backend/app/database.py` → async engine + AsyncSessionLocal
- [ ] Dependency injection: `get_db()` returns async session
- [ ] Connection pooling for 100+ concurrent requests

### 2. Request/Response Schemas
- [ ] `DiagnosisRequest` (symptom_text, vehicle_id, optional vehicle info)
- [ ] `DiagnosisResponse` (diagnosis, severity, repair_steps, confidence_score, recommendations)
- [ ] `RecommendationResponse` (part_name, estimated_cost, shopee_link, priority)

### 3. RAG Service (`backend/app/services/rag.py`)
- [ ] Vector embedding generation (OpenAI or local model)
- [ ] Similarity search in VectorStore (pgvector)
- [ ] Top-k retrieval (k=5) with confidence filtering
- [ ] Context assembly for LLM prompt

### 4. LLM Integration (`backend/app/services/llm.py`)
- [ ] OpenAI/Claude client initialization
- [ ] Prompt engineering (with RAG context)
- [ ] Structured output parsing (diagnosis + severity + repair_steps JSON)
- [ ] Fallback to zero-shot if RAG retrieval fails

### 5. Diagnosis Service (`backend/app/services/diagnosis.py`)
- [ ] Orchestrate: validate input → search RAG → call LLM → extract recommendations
- [ ] Store result in `diagnostic_results` table
- [ ] Query `spare_parts` + `diagnosis_part_map` for recommendations
- [ ] Build response JSON

### 6. API Endpoint (`backend/app/routes/diagnosis.py`)
- [ ] `POST /api/v1/diagnosis/analyze` 
- [ ] Path `/api/v1`, Request body validation
- [ ] Error handling (422, 500, timeout)
- [ ] Response 200 with diagnosis + recommendations
- [ ] Performance: target <500ms (95%)

### 7. Integration Tests (`backend/tests/test_routes/test_diagnosis.py`)
- [ ] Mock LLM responses (avoid OpenAI cost)
- [ ] Test happy path (valid symptom → valid diagnosis)
- [ ] Test edge cases (empty symptom, unknown vehicle)
- [ ] Test error handling (LLM timeout, DB error)
- [ ] Performance baseline (concurrent requests)

### 8. Documentation
- [ ] API spec (request/response schemas in docstrings)
- [ ] Swagger UI auto-documentation
- [ ] M2 checklist + decisions

## Architecture

```
backend/app/
├── main.py                    # Include diagnosis route
├── routes/
│   └── diagnosis.py           # POST /api/v1/diagnosis/analyze
├── services/
│   ├── rag.py                 # Vector search + retrieval
│   ├── llm.py                 # LLM client + prompting
│   └── diagnosis.py           # Orchestration
└── schemas.py                 # Updated with diagnosis schemas
```

## Dependencies (requirements.txt additions)

```
openai>=1.0.0            # OpenAI API (or anthropic for Claude)
httpx>=0.25.0            # Async HTTP client
tenacity>=8.2.0          # Retry logic for LLM calls
python-dotenv>=1.0.0     # Already installed
```

## API Endpoint Spec

### Request
```json
POST /api/v1/diagnosis/analyze
{
  "symptom_text": "Mesin berbunyi aneh saat RPM tinggi",
  "vehicle_id": "550e8400-e29b-41d4-a716-446655440000",
  "vehicle_make": "Honda",
  "vehicle_model": "Civic",
  "year": 2020
}
```

### Response (200 OK)
```json
{
  "diagnosis_id": "550e8400-e29b-41d4-a716-446655440001",
  "diagnosis": "Kemungkinan carbon buildup di ruang bakar...",
  "severity": "DIY_HARD",
  "confidence_score": 0.87,
  "repair_steps": [
    {"step": 1, "description": "Gunakan fuel octane booster"},
    {"step": 2, "description": "Bawa ke bengkel untuk service"}
  ],
  "recommendations": [
    {
      "part_name": "Fuel System Cleaner",
      "part_category": "Additives",
      "estimated_cost": 75000,
      "priority": 1,
      "urgency": "soon",
      "shopee_link": "https://shopee.co.id/..."
    }
  ]
}
```

## Performance Target
- 95th percentile: <500ms (includes pgvector search + LLM call)
- 100 concurrent requests supported
- Timeout: 30s max (fail gracefully)

## Known Limitations (M3+)
- [ ] No persistent user sessions (JWT deferred to M2.5)
- [ ] LLM responses cached only in DB (Redis for M3)
- [ ] Single LLM provider (switch logic for M3)
- [ ] Shopee affiliate links hardcoded (dynamic fetch in M3)

## Success Criteria
- [ ] All 8 deliverables implemented
- [ ] Integration tests pass (mocked LLM)
- [ ] Swagger docs accessible at `/docs`
- [ ] Response time <500ms (load test 50 concurrent)
- [ ] No hardcoded secrets in code (all in .env)

## Timeline
Target: Complete by EOD 2026-10-23 (48 hours)
- Phase 1 (4h): Schemas + Services architecture
- Phase 2 (8h): RAG + LLM integration  
- Phase 3 (8h): Endpoint + error handling
- Phase 4 (6h): Tests + load testing
- Phase 5 (4h): Documentation + PR review

---
**Start:** 2026-10-22 08:30 UTC+7
**Status:** Planning
**Branch:** M2-fastapi-diagnosis
