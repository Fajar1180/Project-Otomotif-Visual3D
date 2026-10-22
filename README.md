# Project Otomotif AI (Project Pak Yogi) - Paket Dokumentasi

## Ikhtisar
Repositori ini berisi semua hasil kerja untuk Project Otomotif AI (Project Pak Yogi), mencakup:
- Dokumen Kebutuhan Proyek (PRD)
- Spesifikasi Kebutuhan Perangkat Lunak (SRS)
- Diagram Relasi Entitas (ERD)
- Spesifikasi API
- Spesifikasi Desain UI/UX
- Instruksi Pembuatan Desain Figma
- Rencana Implementasi
- Analisis Keterampilan
- Laporan Analisis

## Struktur Proyek
```
Project-Otomotif-Visual3D/
├── design/
│   ├── components/               # Komponen reusable (akan diisi)
│   ├── tokens/                   # Design tokens (akan diisi)
│   ├── figma/                    # File desain Figma (akan diisi)
│   ├── mockups/                  # Mockup HTML (dashboard, 3D configurator, AI diagnosis)
│   ├── spec/                     # Spesifikasi desain (akan diisi)
│   ├── theme/                    # Theme CSS (theme-override.css)
│   └── figma-design-specification.json  # Design tokens
├── docs/
│   ├── prd/
│   │   └── PRD_Project_Pak_Yogi.md
│   ├── srs/
│   │   └── SRS_Project_Pak_Yogi.md
│   ├── erd/
│   │   └── ERD_Project_Pak_Yogi.md
│   ├── api/
│   │   └── API_Spec_Project_Pak_Yogi.md
│   ├── ui-ux/
│   │   └── UI_UX_Design_Specification.md
│   └── design/
│       └── DESIGN.md
├── guides/
│   ├── figma/
│   │   └── FIGMA_MANUAL_GUIDE.md
│   │   ├── Figma_Design_Creation_Instructions.md
│   │   └── preview-figma.html
│   └── development/
│       └── (akan diisi)
├── reports/
│   ├── status/
│   │   ├── DESIGN_MOCKUPS_SUMMARY.md
│   │   ├── FINAL_STATUS_REPORT.md
│   │   ├── PROGRES_DESAIN_FIGMA.md
│   │   ├── PROJECT_COMPLETION_FINAL.md
│   │   ├── PROJECT_SUMMARY.md
│   │   └── TASK_COMPLETION_SUMMARY.md
│   ├── progress/
│   │   └── M0-review-dokumentasi/
│   │       └── CHECKLIST.md
│   └── akademik/
│   │   └── LAPORAN_INISIASI_PRODUK_STARTUP.md
├── plan.md                       # Rencana implementasi detail
├── skills.md                     # Analisis keterampuan yang diperlukan
├── report.md                     # Laporan analisis proyek
├── README.md
└── RULES.md
```

## Daftar Dokumen

### 1. [docs/prd/PRD_Project_Pak_Yogi.md](docs/prd/PRD_Project_Pak_Yogi.md)
**Dokumen Kebutuhan Proyek**
- Ikhtisar proyek dan konteks bisnis
- Fitur inti: AI 3D Configurator & Shopee Recommender, AI Storytelling Diagnosis
- Kebutuhan teknis dan arsitektur
- Milestone dan penugasan
- Kriteria keberhasilan dan risiko

### 2. [docs/srs/SRS_Project_Pak_Yogi.md](docs/srs/SRS_Project_Pak_Yogi.md)
**Spesifikasi Kebutuhan Perangkat Lunak**
- Kebutuhan fungsional detail (FR-001 s.d FR-026)
- Kebutuhan non-fungsional (kinerja, keamanan, keamanan, dll)
- Kebutuhan antarmuka eksternal
- Fitur sistem dan user stories
- Glosarium dan model analisis

### 3. [docs/erd/ERD_Project_Pak_Yogi.md](docs/erd/ERD_Project_Pak_Yogi.md)
**Diagram Relasi Entitas**
- Skema database lengkap dengan relasi
- Visualisasi diagram Mermaid
- Definisi entitas dan detail relasi
- Tabel: vehicles, symptoms, diagnoses, spare_parts, workshops, tabel mapping

### 4. [docs/api/API_Spec_Project_Pak_Yogi.md](docs/api/API_Spec_Project_Pak_Yogi.md)
**Spesifikasi API (OpenAPI 3.0)**
- Endpoint autentikasi (/auth/*)
- Endpoint kendaraan (/vehicles/*)
- Endpoint diagnosis (/diagnosis/*)
- Endpoint 3D Configurator (/3d/*)
- Endpoint bengkel (/workshops/*)
- Respons error dan rate limiting

### 5. [docs/ui-ux/UI_UX_Design_Specification.md](docs/ui-ux/UI_UX_Design_Specification.md)
**Spesifikasi Desain UI/UX**
- Sistem desain (palette warna, tipografi, ikonografi)
- Struktur layout (dashboard, 3D configurator, diagnosis, dll)
- Perpustakaan komponen (tombol, kartu, formulir)
- Elemen interaktif (loading states, notifikasi)
- Panduan desain responsif
- Dukungan aksesibilitas dan internasionalisasi

### 6. [guides/figma/Figma_Design_Creation_Instructions.md](guides/figma/Figma_Design_Creation_Instructions.md)
**Instruksi Pembuatan Desain Figma**
- Panduan langkah-demi-langkah pembuatan file desain Figma
- Instruksi setup sistem desain
- Spesifikasi komponen per layar
- Variasi dan state komponen
- Design tokens dan panduan prototyping
- Pendekatan alternatif dan proses handoff

### 7. [plan.md](plan.md)
**Rencana Implementasi Detail**
- Fase 1: Setup dan Foundation (Minggu 1-2)
- Fase 2: Frontend Development (Minggu 3-6)
- Fase 3: Backend Development (Minggu 6-8)
- Fase 4: Testing dan QA (Minggu 8-10)
- Fase 5: Documentation dan Handoff (Minggu 10-11)
- Timeline, risiko, dan mitigasi

### 8. [skills.md](skills.md)
**Analisis Keterampuan**
- Keterampuan pengembangan inti
- Keterampuan desain
- Keterampuan manajemen proyek
- Keterampuan testing
- Keterampuan dokumentasi
- Keterampilan quality assurance

### 9. [report.md](report.md)
**Laporan Analisis Proyek**
- Ikhtisar proyek
- Analisis struktur folder
- Analisis sistem desain
- Ringkasan rencana implementasi
- Penilaian keterampuan
- Langkah selanjutnya

## Langkah Selanjutnya

### Untuk Project Manager (fajar1180):
1. Tinjau semua dokumentasi dengan stakeholder
2. Tugas ke anggota tim berdasarkan spesifikasi
3. Siapkan lingkungan development dan struktur repositori
4. Mulai sprint planning untuk Milestone 1

### Untuk System Analyst (ilhamalmunawar05-cpu):
1. Finalisasi skema database berdasarkan ERD
2. Setup database development dengan sample data
3. Tinjau spesifikasi API untuk implementasi
4. Siapkan dokumen desain teknis

### Untuk Tim Development (ilhamalmunawar05-cpu):
1. **Milestone 1 (Minggu 2):**
   - Setup repositori proyek
   - Implementasi skema database dan models
   - Tulis unit tests (pendekatan TDD)
   - Buat struktur awal aplikasi FastAPI

2. **Milestone 2 (Minggu 3):**
   - Implementasi endpoint API diagnosis
   - Integrasi pgvector untuk fungsionalitas RAG
   - Setup Celery untuk background tasks
   - Buat skeleton frontend awal dengan Next.js

3. **Milestone 3 (Minggu 4):**
   - Implementasi API 3D configurator dan frontend
   - Integrasi Shopee Affiliate API
   - Setup fungsionalitas workshop finder
   - Implementasi autentikasi pengguna

4. **Milestone 4-5 (Minggu 5-6):**
   - Integrasi fitur dan QA
   - Optimasi performa
   - User acceptance testing
   - Persiapan deployment production

## Konfirmasi Technology Stack
- **Frontend:** Next.js (App Router), React Three Fiber, Tailwind CSS, Zustand
- **Backend:** Python FastAPI, Celery + Redis, PostgreSQL + pgvector
- **AI:** OpenAI/Claude LLM untuk RAG pipeline
- **Integrasi:** Shopee Affiliate API, Google Maps API
- **Development:** Metodologi Test-Driven Development (TDD)

## Kriteria Keberhasilan
- Akurasi diagnosis > 85% pada test case
- 3D configurator load < 3 detik di mobile
- Rata-rata response time API < 200ms
- Semua fitur inti fungsional dan teruji
- Target uptime bulanan 99.5%
- Skor SUS > 75 pada user testing

---
*Paket Dokumentasi Dibuat: 19 Oktober 2026*
*Disusun oleh: fajar1180 (Project Manager), ilhamalmunawar05-cpu (System Analyst/Developer)*