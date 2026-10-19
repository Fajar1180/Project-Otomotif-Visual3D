# Software Requirements Specification (SRS)
## Platform Otomotif AI (Project Pak Yogi)

### 1. Introduction
This document specifies the software requirements for the Platform Otomotif AI (Project Pak Yogi), a Web-First application for vehicle diagnosis and modification visualization.

#### 1.1 Purpose
To provide a complete description of the functional and non-functional requirements for the Otomotif AI Platform.

#### 1.2 Scope
The system covers:
- 3D vehicle modification visualization with AI-driven spare part recommendations
- Conversational AI diagnosis of vehicle issues via natural language input
- Integration with Shopee Affiliate for parts purchasing
- Workshop locator integration

#### 1.3 Definitions, Acronyms, and Abbreviations
- **AI:** Artificial Intelligence
- **RAG:** Retrieval-Augmented Generation
- **LLM:** Large Language Model
- **TDD:** Test-Driven Development
- **REST:** Representational State Transfer
- **API:** Application Programming Interface
- **ERD:** Entity Relationship Diagram

#### 1.4 References
1. [PRD_Project_Pak_Yogi.md](PRD_Project_Pak_Yogi.md) - Project Requirements Document
2. Database schema in ide-dasar.txt
3. API specifications in ide-dasar.txt

#### 1.5 Overview
- Section 2: Overall Description
- Section 3: Specific Requirements (Functional & Non-functional)
- Section 4: External Interface Requirements
- Section 5: System Features
- Section 6: Other Non-functional Requirements

### 2. Overall Description
#### 2.1 Product Perspective
A standalone web application with backend API services, PostgreSQL database, and integration with external services (Shopee API, Google Maps API).

#### 2.2 Product Functions
| Function | Description |
|----------|-------------|
| 3D Visualization | Real-time 3D model rendering and modification |
| AI Diagnosis | Natural language processing for issue analysis |
| Part Recommendation | Intelligent spare part suggestions with affiliate links |
| Workshop Finder | Location-based workshop discovery |

#### 2.3 User Classes and Characteristics
| User Type | Description |
|-----------|-------------|
| Vehicle Owner | Seeks diagnosis and repair guidance for their vehicle |
| DIY Enthusiast | Looks for step-by-step repair instructions |
| Mechanic | Uses platform as diagnostic reference tool |
| Workshop Owner | Listed in workshop finder for customer acquisition |

#### 2.4 Operating Environment
- Web browsers: Chrome, Firefox, Safari (latest versions)
- Backend: Linux/Windows server with Python 3.8+
- Database: PostgreSQL 14+ with pgvector extension
- Frontend: Node.js 16+, Next.js 13+

#### 2.5 Design and Implementation Constraints
- Must use Test-Driven Development methodology
- Frontend: Next.js App Router, React Three Fiber
- Backend: FastAPI, Python async
- Database: PostgreSQL + pgvector for vector search
- Budget: Open-source tools + cloud services (Vercel, Render, etc.)

#### 2.6 User Documentation
- Online help system integrated into platform
- API documentation via OpenAPI/Swagger
- Developer documentation in CODEOWNERS and CONTRIBUTING files

### 3. Specific Requirements

#### 3.1 Functional Requirements

##### 3.1.1 User Authentication & Profile
**FR-001:** The system SHALL allow users to create accounts with email/password
**FR-002:** The system SHALL support Google OAuth login alternative
**FR-003:** The system SHALL maintain user session state with JWT tokens
**FR-004:** The system SHALL allow profile updates (name, preferred vehicle, location)

##### 3.1.2 3D Vehicle Configurator
**FR-005:** The system SHALL display an interactive 3D vehicle model in the browser
**FR-006:** The system SHALL allow users to select and swap vehicle components (wheels, exhaust, etc.)
**FR-007:** The system SHALL highlight modified components with visual indicators
**FR-008:** The system SHALL generate a unique modification ID for each configuration
**FR-009:** The system SHALL save user configurations to their profile

##### 3.1.3 AI Diagnosis Engine
**FR-010:** The system SHALL accept natural language input (text or voice) describing vehicle issues
**FR-011:** The system SHALL process input through RAG pipeline with vehicle-specific embeddings
**FR-012:** The system SHALL return diagnosis results with:
  - Diagnosis ID and title
  - Technical explanation
  - Severity level (DIY_EASY, DIY_HARD, WORKSHOP_REQUIRED)
  - Step-by-step repair instructions (JSONB array)
  - Recommended spare parts list
  - Nearby workshop suggestions (if severity = WORKSHOP_REQUIRED)
**FR-013:** The system SHALL cache frequent queries to improve response times
**FR-014:** The system SHALL provide confidence scores for each diagnosis

##### 3.1.4 Shopee Affiliate Integration
**FR-015:** The system SHALL extract keywords from diagnosis to search Shopee catalog
**FR-016:** The system SHALL generate affiliate links for recommended spare parts
**FR-017:** The system SHALL display price estimates and availability from Shopee
**FR-018:** The system SHALL track clicks on affiliate links for analytics

##### 3.1.5 Workshop Finder
**FR-019:** The system SHALL integrate with Google Maps API for location services
**FR-020:** The system SHALL display workshops within 25km radius for WORKSHOP_REQUIRED diagnoses
**FR-021:** The system SHALL show workshop ratings, specialties, and contact information
**FR-022:** The system SHALL provide turn-by-turn navigation to selected workshop

##### 3.1.6 Administrative Functions
**FR-023:** Administrators SHALL manage vehicle makes/models in the database
**FR-024:** Administrators SHALL update symptom-disease mappings
**FR-025:** Administrators SHALL moderate workshop listings
**FR-026:** The system SHALL log all API requests for audit purposes

#### 3.2 Non-Functional Requirements

##### 3.2.1 Performance Requirements
**NFR-001:** Diagnosis API response time SHALL be < 500ms for 95% of requests
**NFR-002:** 3D model loading time SHALL be < 3 seconds on mobile devices
**NFR-003:** System SHALL support 100 concurrent users without degradation
**NFR-004:** Database queries with vector search SHALL complete in < 200ms

##### 3.2.2 Safety Requirements
**NFR-005:** The system SHALL display disclaimers that diagnosis is advisory only
**NFR-006:** Critical safety issues SHALL always recommend professional workshop visit
**NFR-007:** All medical/chemical safety warnings SHALL be included in repair steps

##### 3.2.3 Security Requirements
**NFR-008:** All user inputs SHALL be sanitized to prevent XSS/SQL injection
**NFR-009:** Passwords SHALL be hashed using bcrypt with salt
**NFR-010:** API endpoints SHALL require authentication (except public diagnosis endpoint)
**NFR-011:** Rate limiting SHALL be applied to prevent abuse (100 req/hour/IP)
**NFR-012:** JWT tokens SHALL expire after 24 hours with refresh mechanism

##### 3.2.4 Portability Requirements
**NFR-013:** Frontend SHALL be responsive on mobile (320px width) and desktop (1920px width)
**NFR-014:** Backend SHALL deploy to Docker containers
**NFR-015:** Database migrations SHALL be version-controlled

##### 3.2.5 Maintainability Requirements
**NFR-016:** Code SHALL follow PEP 8 (Python) and ESLint (JavaScript) standards
**NFR-017:** Minimum 80% test coverage required for all new code
**NFR-018:** Documentation SHALL be updated with every feature release
**NFR-019:** Logging SHALL follow structured format (JSON) for ELK stack compatibility

### 4. External Interface Requirements

#### 4.1 User Interfaces
**UI-001:** Frontend SHALL use Tailwind CSS for consistent styling
**UI-002:** 3D canvas SHALL occupy minimum 60vh on diagnosis page
**UI-003:** Color scheme SHALL use automotive-inspired palette (dark blues, metallic grays)
**UI-004:** Typography SHALL prioritize readability (Inter or similar sans-serif)

#### 4.2 Hardware Interfaces
**HI-001:** System SHALL support microphone input for voice diagnosis
**HI-002:** System SHALL support camera input for future computer vision features
**HI-003:** Touch events SHALL be supported for mobile interaction

#### 4.3 Software Interfaces
**SI-001:** Backend SHALL expose RESTful JSON APIs under `/api/v1/`
**SI-002:** Database SHALL use PostgreSQL with pgvector extension
**SI-003:** External APIs:
  - Shopee Affiliate API (for product search and link generation)
  - Google Maps API (for workshop geolocation)
  - OpenAI/Claude API (for LLM in RAG pipeline)
**SI-004:** Authentication SHALL use JWT with refresh tokens

#### 4.4 Communications Interfaces
**CI-001:** System SHALL communicate via HTTPS only
**CI-002:** API requests SHALL use JSON format
**CI-003:** WebSocket connections SHALL be used for real-time 3D updates
**CI-004:** Email notifications SHALL use SMTP for user alerts

### 5. System Features

#### 5.1 Feature: 3D Vehicle Configurator
**Description:** Interactive 3D visualization allowing users to modify vehicle appearance
**Stimulus:** User selects component category (wheels, exhaust, body kit)
**Response:** 
  - Display available options in scrollable panel
  - Preview selected component on 3D model in real-time
  - Confirm selection with "Apply" button
  - Update modification ID and save to user profile

#### 5.2 Feature: AI Diagnosis Engine
**Description:** Conversational AI that interprets vehicle issues and provides solutions
**Stimulus:** User submits natural language description of vehicle problem
**Response:**
  - Process input through RAG pipeline with symptom embeddings
  - Retrieve top-k matching diagnoses with confidence scores
  - Generate detailed explanation using LLM with technical context
  - Classify severity based on repair complexity and safety implications
  - Return structured JSON with diagnosis details, repair steps, parts, workshops

#### 5.3 Feature: Shopee Affiliate Integration
**Description:** Monetization through affiliate links for recommended spare parts
**Stimulus:** Diagnosis returns list of recommended spare parts
**Response:**
  - Extract keywords (part name, vehicle model, brand) from diagnosis
  - Query Shopee Affiliate API for matching products
  - Generate trackable affiliate links with UTM parameters
  - Display price, availability, and seller ratings
  - Log click events for revenue attribution

#### 5.4 Feature: Workshop Finder
**Description:** Locates nearby repair workshops for complex issues
**Stimulus:** Diagnosis severity = WORKSHOP_REQUIRED
**Response:**
  - Get user location (with permission) or use IP-based approximation
  - Query Google Maps Place API for "auto repair" within radius
  - Filter results by vehicle specialization if available in database
  - Display results in list and map view with distance sorting
  - Provide "Navigate" button launching external maps application

### 6. Other Non-functional Requirements

#### 6.1 Reliability
- System SHALL achieve 99.5% monthly uptime
- Database backups SHALL occur daily with point-in-time recovery
- Error rates SHALL be monitored and alerted via SLO/SLI metrics

#### 6.2 Maintainability
- Technical debt SHALL be tracked and addressed in sprint planning
- Code reviews SHALL be mandatory for all production changes
- Dependency updates SHALL be tested in staging before production

#### 6.3 Portability
- Deployment artifacts SHALL be versioned and immutable
- Infrastructure SHALL be defined as code (Terraform/CloudFormation)
- Environment variables SHALL manage configuration differences

#### 6.4 Usability
- Platform SHALL achieve SUS score > 75 in user testing
- Error messages SHALL be user-friendly and actionable
- Help tooltips SHALL be available for complex features
- Loading states SHALL be displayed for all asynchronous operations

### 7. Appendices

#### 7.1 Glossary
- **DIY_EASY:** Repair requiring basic tools (< 1 hour)
- **DIY_HARD:** Repair requiring intermediate skills/tools (1-4 hours)
- **WORKSHOP_REQUIRED:** Repair needing professional equipment/expertise
- **pgvector:** PostgreSQL extension for similarity search of vectors
- **RAG:** Technique combining retrieval with generation for grounded AI
- **TDD:** Development practice writing tests before implementation

#### 7.2 Analysis Models
*Entity definitions from database schema:*
- **vehicles:** id (UUID), brand (string), model (string), year_start/end (int), category (string)
- **symptoms:** id (UUID), symptom_code (string), description (text), category (string), embedding (vector)
- **diagnoses:** id (UUID), title (string), technical_explanation (text), severity_level (enum), repair_steps (JSONB)
- **spare_parts:** id (UUID), part_name (string), part_number (string), brand (string), price_min/max (numeric), shopee_item_id/shop_id (string), default_shopee_url (text)
- **workshops:** id (UUID), name (string), address (text), latitude/longitude (double), rating (numeric), specialties (text array)
- **mappings:** symptom_id/diagnosis_id (UUID foreign keys), confidence_weight (float); diagnosis_id/spare_part_id (UUID foreign keys), is_primary (boolean)

#### 7.3 To Be Determined (TBD)
- Exact Shopee affiliate commission structure to finalize
- Google Maps API usage limits and cost projection
- Final decision on LLM provider (OpenAPI vs Claude vs open-source)
- Mobile app roadmap (Phase 2)

---
*Document Version 1.0 | Created: 2026-10-19*
