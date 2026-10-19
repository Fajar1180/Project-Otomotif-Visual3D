# Project Requirements Document (PRD)
## Platform Otomotif AI (Project Pak Yogi)

### 1. Project Overview
**Project Name:** Platform Otomotif AI (Project Pak Yogi)
**Version:** 1.0
**Status:** Initiation Phase
**Prepared By:** fajar1180 (Project Manager, System Analyst, Backend, Frontend, QaTesting)

### 2. Business Context
- **Market Trend:** High growth in motorcycle modification culture in Indonesia (e.g., Thailook, Bratstyle, Cafe Racer)
- **Opportunity:** Monetization through affiliate marketing via Shopee Affiliate Program
- **Goal:** Build a Web-First platform combining Computer Vision (3D reconstruction) and Conversational AI for vehicle component diagnosis and DIY repair guides

### 3. Scope of Work
#### 3.1 Core Features

**Feature 1: AI 3D Modification Configurator & Shopee Recommender**
- Interactive 3D visualization of vehicle modifications using hybrid 3D approach (Sparse-View Image-to-3D + Template-Mesh Swapping)
- Real-time component swapping with Shopee affiliate links
- Integration with Maps API for nearby workshop recommendations

**Feature 2: AI Storytelling Diagnosis & Smart Workshop Finder**
- Natural Language Processing (RAG) to interpret user-reported vehicle issues (text/audio)
- Automated diagnosis of mechanical faults with severity classification (DIY_EASY, DIY_HARD, WORKSHOP_REQUIRED)
- Step-by-step repair instructions and spare part recommendations
- Integration with Shopee Affiliate for parts linking

#### 3.2 Technical Requirements

**Frontend (Next.js + React)**
- App Router with SEO-friendly pages
- React Three Fiber (R3F) for 3D rendering
- Tailwind CSS for styling
- Zustand for state management

**Backend (FastAPI + Python)**
- Async processing for heavy AI workloads (Celery + Redis)
- PostgreSQL with pgvector extension for vector embeddings
- OpenAI/Claude LLM integration for RAG pipeline

**Database Schema**
- `vehicles` - Vehicle master data
- `symptoms` - Issue descriptions with vector embeddings
- `diagnoses` - Structured diagnostic results
- `spare_parts` - Component inventory with Shopee links
- `workshops` - Workshop locations with ratings
- `mappings` - Symptom-to-diagnosis mappings

**API Endpoints**
- `POST /api/v1/diagnosis/analyze` - Submit user story → RAG analysis → JSON response with diagnosis, severity, repair steps, parts
- `POST /api/v1/3d/generate` - Upload 4 vehicle photos → generate 3D mesh → display interactively
- `GET /api/v1/workshops` - List nearby workshops
- `GET /api/v1/vehicles` - Retrieve vehicle catalog

### 4. Non-Functional Requirements
- **Performance:** Low latency (<200ms) for diagnosis responses
- **Scalability:** Support concurrent users via async processing
- **Security:** Input sanitization, authentication (JWT), rate limiting
- **Maintainability:** Modular architecture, TDD-first development

### 5. Milestones

| Milestone | Description | Target |
|-----------|-------------|---------|
| M0 | Project Kickoff & Architecture Finalization | Week 1 |
| M1 | Database Schema Implementation & Unit Tests | Week 2 |
| M2 | Backend API (Diagnosis & 3D) + Frontend Skeleton | Week 3 |
| M3 | RAG Diagnostics Module + Shopee Integration | Week 4 |
| M4 | Full Feature Integration & QA | Week 5 |
| M5 | Production Ready Release | Week 6 |

### 6. Assignment

| Role | Owner | Responsibilities |
|------|-------|------------------|
| Project Manager | fajar1180 | Timeline, stakeholder coordination, risk management |
| System Analyst | ilhamalmunawar05-cpu | Requirements gathering, database design, API spec |
| Backend Developer | ilhamalmunawar05-cpu | FastAPI services, pgvector integration, Celery workers |
| Frontend Developer | ilhamalmunawar05-cpu | Next.js app, R3F 3D components, UI/UX |
| QA Engineer | ilhamalmunawar05-cpu | Test-driven development, regression testing, bug triage |

### 7. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| AI hallucination in diagnosis | High | RAG with grounding, human-in-loop review, fallback to expert |
| 3D rendering performance on mobile | Medium | Optimize mesh complexity, use WebGL acceleration |
| Shopee API rate limits | Medium | Caching, retry logic, fallback to static parts list |
| Database scaling with vector search | High | Use pgvector with proper indexing, consider Elasticsearch for large scale |

### 8. Success Criteria
- Diagnostic accuracy > 85% on test cases
- 3D configurator loads in <3 seconds on mobile
- Average API response time < 200ms
- All core features functional and tested

---
*Document Version 1.0 | Created: 2026-10-19*
