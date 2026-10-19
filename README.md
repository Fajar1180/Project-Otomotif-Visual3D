# Project Otomotif AI (Project Pak Yogi) - Documentation Package

## Overview
This repository contains all deliverables for Project Otomotif AI (Project Pak Yogi), including:
- Project Requirements Document (PRD)
- Software Requirements Specification (SRS)
- Entity Relationship Diagram (ERD)
- API Specification
- UI/UX Design Specification
- Figma Design Creation Instructions

## Document List

### 1. [PRD_Project_Pak_Yogi.md](PRD_Project_Pak_Yogi.md)
**Project Requirements Document**
- Project overview and business context
- Core features: AI 3D Configurator & Shopee Recommender, AI Storytelling Diagnosis
- Technical requirements and architecture
- Milestones and assignments
- Success criteria and risks

### 2. [SRS_Project_Pak_Yogi.md](SRS_Project_Pak_Yogi.md)
**Software Requirements Specification**
- Detailed functional requirements (FR-001 to FR-026)
- Non-functional requirements (performance, safety, security, etc.)
- External interface requirements
- System features and user stories
- Glossary and analysis models

### 3. [ERD_Project_Pak_Yogi.md](ERD_Project_Pak_Yogi.md)
**Entity Relationship Diagram**
- Complete database schema with relationships
- Mermaid diagram visualization
- Entity definitions and relationship details
- Tables: vehicles, symptoms, diagnoses, spare_parts, workshops, mapping tables

### 4. [API_Spec_Project_Pak_Yogi.md](API_Spec_Project_Pak_Yogi.md)
**API Specification (OpenAPI 3.0)**
- Authentication endpoints (/auth/*)
- Vehicle endpoints (/vehicles/*)
- Diagnosis endpoints (/diagnosis/*)
- 3D Configurator endpoints (/3d/*)
- Workshop endpoints (/workshops/*)
- Error responses and rate limiting

### 5. [UI_UX_Design_Specification.md](UI_UX_Design_Specification.md)
**UI/UX Design Specification**
- Design system (color palette, typography, iconography)
- Layout structures (dashboard, 3D configurator, diagnosis, etc.)
- Component library (buttons, cards, forms)
- Interactive elements (loading states, notifications)
- Responsive design guidelines
- Accessibility and internationalization support

### 6. [Figma_Design_Creation_Instructions.md](Figma_Design_Creation_Instructions.md)
**Figma Design Creation Instructions**
- Step-by-step guide to creating Figma design file
- Design system setup instructions
- Screen-by-screen component specifications
- Component variants and states
- Design tokens and prototyping guidance
- Alternative approaches and handoff process

## Project Structure
```
Project-Otomotif-Visual3D/
├── PRD_Project_Pak_Yogi.md
├── SRS_Project_Pak_Yogi.md
├── ERD_Project_Pak_Yogi.md
├── API_Spec_Project_Pak_Yogi.md
├── UI_UX_Design_Specification.md
├── Figma_Design_Creation_Instructions.md
└── .git/
```

## Next Steps

### For Project Manager (fajar1180):
1. Review all documentation with stakeholders
2. Assign tasks to team members based on specifications
3. Set up development environment and repository structure
4. Begin sprint planning for Milestone 1

### For System Analyst (ilhamalmunawar05-cpu):
1. Finalize database schema based on ERD
2. Set up development database with sample data
3. Review API specifications for implementation
4. Prepare technical design documents

### For Development Team (ilhamalmunawar05-cpu):
1. **Milestone 1 (Week 2):**
   - Set up project repository
   - Implement database schema and models
   - Write unit tests (TDD approach)
   - Create initial FastAPI application structure

2. **Milestone 2 (Week 3):**
   - Implement diagnosis API endpoint
   - Integrate pgvector for RAG functionality
   - Set up Celery for background tasks
   - Create initial frontend skeleton with Next.js

3. **Milestone 3 (Week 4):**
   - Implement 3D configurator API and frontend
   - Integrate Shopee Affiliate API
   - Set up workshop finder functionality
   - Implement user authentication

4. **Milestone 4-5 (Week 5-6):**
   - Feature integration and QA
   - Performance optimization
   - User acceptance testing
   - Production deployment preparation

## Technology Stack Confirmation
- **Frontend:** Next.js (App Router), React Three Fiber, Tailwind CSS, Zustand
- **Backend:** Python FastAPI, Celery + Redis, PostgreSQL + pgvector
- **AI:** OpenAI/Claude LLM for RAG pipeline
- **Integrations:** Shopee Affiliate API, Google Maps API
- **Development:** Test-Driven Development (TDD) methodology

## Success Criteria
- Diagnostic accuracy > 85% on test cases
- 3D configurator loads in <3 seconds on mobile
- Average API response time < 200ms
- All core features functional and tested
- 99.5% monthly uptime target
- SUS score > 75 in user testing

---
*Documentation Package Created: 2026-10-19*
*Prepared by: fajar1180 (Project Manager), ilhamalmunawar05-cpu (System Analyst/Developer)*