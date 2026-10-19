# Project Otomotif AI (Project Pak Yogi) - Paket Dokumentasi

## Ikhtisar
Repositori ini berisi semua hasil kerja untuk Project Otomotif AI (Project Pak Yogi), mencakup:
- Dokumen Kebutuhan Proyek (PRD)
- Spesifikasi Kebutuhan Perangkat Lunak (SRS)
- Diagram Relasi Entitas (ERD)
- Spesifikasi API
- Spesifikasi Desain UI/UX
- Instruksi Pembuatan Desain Figma

## Daftar Dokumen

### 1. [PRD_Project_Pak_Yogi.md](PRD_Project_Pak_Yogi.md)
**Dokumen Kebutuhan Proyek**
- Ikhtisar proyek dan konteks bisnis
- Fitur inti: AI 3D Configurator & Shopee Recommender, AI Storytelling Diagnosis
- Kebutuhan teknis dan arsitektur
- Milestone dan penugasan
- Kriteria keberhasilan dan risiko

### 2. [SRS_Project_Pak_Yogi.md](SRS_Project_Pak_Yogi.md)
**Spesifikasi Kebutuhan Perangkat Lunak**
- Kebutuhan fungsional detail (FR-001 s.d FR-026)
- Kebutuhan non-fungsional (kinerja, keamanan, keamanan, dll)
- Kebutuhan antarmuka eksternal
- Fitur sistem dan user stories
- Glosarium dan model analisis

### 3. [ERD_Project_Pak_Yogi.md](ERD_Project_Pak_Yogi.md)
**Diagram Relasi Entitas**
- Skema database lengkap dengan relasi
- Visualisasi diagram Mermaid
- Definisi entitas dan detail relasi
- Tabel: vehicles, symptoms, diagnoses, spare_parts, workshops, tabel mapping

### 4. [API_Spec_Project_Pak_Yogi.md](API_Spec_Project_Pak_Yogi.md)
**Spesifikasi API (OpenAPI 3.0)**
- Endpoint autentikasi (/auth/*)
- Endpoint kendaraan (/vehicles/*)
- Endpoint diagnosis (/diagnosis/*)
- Endpoint 3D Configurator (/3d/*)
- Endpoint bengkel (/workshops/*)
- Respons error dan rate limiting

### 5. [UI_UX_Design_Specification.md](UI_UX_Design_Specification.md)
**Spesifikasi Desain UI/UX**
- Sistem desain (palette warna, tipografi, ikonografi)
- Struktur layout (dashboard, 3D configurator, diagnosis, dll)
- Perpustakaan komponen (tombol, kartu, formulir)
- Elemen interaktif (loading states, notifikasi)
- Panduan desain responsif
- Dukungan aksesibilitas dan internasionalisasi

### 6. [Figma_Design_Creation_Instructions.md](Figma_Design_Creation_Instructions.md)
**Instruksi Pembuatan Desain Figma**
- Panduan langkah-demi-langkah pembuatan file desain Figma
- Instruksi setup sistem desain
- Spesifikasi komponen per layar
- Variasi dan state komponen
- Design tokens dan panduan prototyping
- Pendekatan alternatif dan proses handoff

## Struktur Proyek
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