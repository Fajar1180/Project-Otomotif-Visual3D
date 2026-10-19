# Dokumen Kebutuhan Proyek (PRD)
## Platform Otomotif AI (Project Pak Yogi)

### 1. Ikhtisar Proyek
**Nama Proyek:** Platform Otomotif AI (Project Pak Yogi)
**Versi:** 1.0
**Status:** Fase Inisiasi
**Disusun Oleh:** fajar1180 (Project Manager, System Analyst, Backend, Frontend, QaTesting)

### 2. Konteks Bisnis
- **Tren Pasar:** Pertumbuhan tinggi dalam budaya modifikasi motor di Indonesia (misal: Thailook, Bratstyle, Cafe Racer)
- **Peluang:** Monetisasi melalui pemasaran afiliasi via Program Affiliate Shopee
- **Tujuan:** Membangun platform Web-First yang menggabungkan Computer Vision (rekonstruksi 3D) dan Conversational AI untuk diagnosis komponen kendaraan dan panduan perbaikan DIY

### 3. Ruang Lingkup Pekerjaan
#### 3.1 Fitur Inti

**Fitur 1: AI 3D Modification Configurator & Shopee Recommender**
- Visualisasi 3D interaktif modifikasi kendaraan menggunakan pendekatan 3D hybrid (Sparse-View Image-to-3D + Template-Mesh Swapping)
- Penukaran komponen real-time dengan link affiliate Shopee
- Integrasi dengan Maps API untuk rekomendasi bengkel terdekat

**Fitur 2: AI Storytelling Diagnosis & Smart Workshop Finder**
- Natural Language Processing (RAG) untuk menginterpretasi keluhan kendaraan pengguna (teks/audio)
- Diagnosis otomatis kerusakan mekanis dengan klasifikasi tingkat keparahan (DIY_EASY, DIY_HARD, WORKSHOP_REQUIRED)
- Instruksi perbaikan langkah-demi-langkah dan rekomendasi suku cadang
- Integrasi dengan Shopee Affiliate untuk link suku cadang

#### 3.2 Kebutuhan Teknis

**Frontend (Next.js + React)**
- App Router dengan halaman SEO-friendly
- React Three Fiber (R3F) untuk rendering 3D
- Tailwind CSS untuk styling
- Zustand untuk state management

**Backend (FastAPI + Python)**
- Pemrosesan async untuk beban kerja AI berat (Celery + Redis)
- PostgreSQL dengan ekstensi pgvector untuk vector embeddings
- Integrasi OpenAI/Claude LLM untuk RAG pipeline

**Skema Database**
- `vehicles` - Data master kendaraan
- `symptoms` - Deskripsi gejala dengan vector embeddings
- `diagnoses` - Hasil diagnosis terstruktur
- `spare_parts` - Inventaris komponen dengan link Shopee
- `workshops` - Lokasi bengkel dengan rating
- `mappings` - Mapping gejala-ke-diagnosis

**Endpoint API**
- `POST /api/v1/diagnosis/analyze` - Kirim cerita user → analisis RAG → respons JSON dengan diagnosis, tingkat keparahan, langkah perbaikan, suku cadang
- `POST /api/v1/3d/generate` - Upload 4 foto kendaraan → generate 3D mesh → tampilkan interaktif
- `GET /api/v1/workshops` - Daftar bengkel terdekat
- `GET /api/v1/vehicles` - Ambil katalog kendaraan

### 4. Kebutuhan Non-Fungsional
- **Performa:** Latensi rendah (<200ms) untuk respons diagnosis
- **Skalabilitas:** Mendukung pengguna concurrent via pemrosesan async
- **Keamanan:** Sanitisasi input, autentikasi (JWT), rate limiting
- **Maintainability:** Arsitektur modular, pengembangan TDD-first

### 5. Milestone

| Milestone | Deskripsi | Target |
|-----------|-------------|---------|
| M0 | Project Kickoff & Finalisasi Arsitektur | Minggu 1 |
| M1 | Implementasi Skema Database & Unit Tests | Minggu 2 |
| M2 | Backend API (Diagnosis & 3D) + Frontend Skeleton | Minggu 3 |
| M3 | Modul RAG Diagnostik + Integrasi Shopee | Minggu 4 |
| M4 | Integrasi Fitur Penuh & QA | Minggu 5 |
| M5 | Rilis Production Ready | Minggu 6 |

### 6. Penugasan

| Peran | Pemilik | Tanggung Jawab |
|-------|---------|------------------|
| Project Manager | fajar1180 | Timeline, koordinasi stakeholder, manajemen risiko |
| System Analyst | ilhamalmunawar05-cpu | Pengumpulan kebutuhan, desain database, spec API |
| Backend Developer | ilhamalmunawar05-cpu | Layanan FastAPI, integrasi pgvector, worker Celery |
| Frontend Developer | ilhamalmunawar05-cpu | Aplikasi Next.js, komponen 3D R3F, UI/UX |
| QA Engineer | ilhamalmunawar05-cpu | Test-driven development, regression testing, bug triage |

### 7. Risiko & Mitigasi

| Risiko | Dampak | Mitigasi |
|--------|--------|------------|
| Halusinasi AI dalam diagnosis | Tinggi | RAG dengan grounding, human-in-loop review, fallback ke expert |
| Performa rendering 3D di mobile | Sedang | Optimasi kompleksitas mesh, gunakan akselerasi WebGL |
| Batas rate limit Shopee API | Sedang | Caching, retry logic, fallback ke daftar suku cadang statis |
| Skalabilitas database dengan vector search | Tinggi | Gunakan pgvector dengan indexing proper, pertimbangkan Elasticsearch untuk skala besar |

### 8. Kriteria Keberhasilan
- Akurasi diagnosis > 85% pada test case
- 3D configurator load < 3 detik di mobile
- Rata-rata response time API < 200ms
- Semua fitur inti fungsional dan teruji

---
*Versi Dokumen 1.0 | Dibuat: 19 Oktober 2026*
