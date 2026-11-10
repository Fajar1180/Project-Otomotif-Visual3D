# PROPOSAL PENGAJUAN STARTUP DIGITAL

**Judul:** Platform Otomotif AI (Project Pak Yogi)  
**Penyusun:** fajar1180 & ilhamalmunawar05-cpu  
**Versi:** 1.0  
**Tanggal:** 9 November 2026  
**Program:** UTS Startup Digital UKRI

---

## 1. Ringkasan Eksekutif

Platform Otomotif AI (Project Pak Yogi) adalah platform web-first yang menggabungkan Computer Vision (rekonstruksi 3D kendaraan) dan Conversational AI (RAG) untuk diagnosis komponen kendaraan serta panduan perbaikan DIY. Target: pemilik bengkel, pemilik kendaraan (mobil & motor), mekanik, dan penggemar DIY di Indonesia.

Masalah inti: pemilik kendaraan kesulitan mendiagnosa kerusakan sendiri, sehingga harus datang langsung ke bengkel tanpa estimasi biaya — membuang waktu dan biaya transportasi. Solusi: AI Storytelling Diagnosis (teks/audio → klasifikasi keparahan + langkah perbaikan + rekomendasi suku cadang) dan AI 3D Modification Configurator (visualisasi 3D modifikasi, penukaran komponen real-time, link afiliasi Shopee, pencari bengkel terdekat via Maps API).

Sumber pendapatan: komisi afiliasi Shopee dari penjualan suku cadang dan komponen modifikasi.

## 2. Identitas Startup

| Item | Isi |
|------|-----|
| Nama | Platform Otomotif AI (Project Pak Yogi) |
| Bentuk | Startup Digital (Web-First, Next.js + FastAPI) |
| Status | Fase Inisiasi (PRD v1.0) |
| Target pelanggan | Pemilik bengkel, pemilik kendaraan, mekanik, penggemar DIY |
| Lokasi | Indonesia |
| Tim | fajar1180 (PM, System Analyst, Backend, Frontend, QA); ilhamalmunawar05-cpu (System Analyst, Backend, Frontend, QA) |

## 3. Masalah dan Dampak

- Pemilik kendaraan mengalami kesulitan diagnosa kerusakan sendiri.
- Tidak tahu estimasi biaya sebelum datang ke bengkel.
- Membuang waktu dan biaya transportasi untuk kunjungan yang tidak perlu.
- Solusi saat ini: datang langsung ke bengkel konvensional dan bertanya langsung kepada mekanik.

## 4. Solusi dan Manfaat Inti

1. **AI Storytelling Diagnosis** — NLP/RAG menginterpretasi keluhan kendaraan (teks/audio), klasifikasi tingkat keparahan (DIY_EASY, DIY_HARD, WORKSHOP_REQUIRED), instruksi perbaikan langkah-demi-langkah, rekomendasi suku cadang.
2. **AI 3D Modification Configurator & Shopee Recommender** — visualisasi 3D modifikasi kendaraan, penukaran komponen real-time, link afiliasi Shopee, rekomendasi bengkel terdekat via Maps API.

Manfaat: diagnosa lebih cepat, estimasi biaya transparan, mengurangi kunjungan tidak perlu ke bengkel.

## 5. Produk (MVP)

Satu fitur inti: diagnosis satu kategori kerusakan (contoh: kerusakan mesin mobil).

- Input cerita keluhan (teks) + konteks kendaraan.
- Hasil diagnosis dengan tingkat keparahan (DIY_EASY/DIY_HARD/WORKSHOP_REQUIRED).
- Langkah perbaikan + rekomendasi suku cadang.

Endpoint: `POST /api/v1/diagnosis/analyze` (FastAPI), RAG pipeline dengan OpenAI/Claude.

Fitur ditunda: 3D Configurator, Shopee Affiliate, pencari bengkel via Maps, riwayat diagnosis, autentikasi.

## 6. Analisis Pasar

- Tren tinggi budaya modifikasi motor di Indonesia (Thailook, Bratstyle, Cafe Racer).
- Peluang monetisasi via Program Affiliate Shopee.
- Segmen: pemilik bengkel, pemilik kendaraan (mobil & motor), mekanik, penggemar DIY.

## 7. Model Bisnis (BMC)

| Blok | Isi |
|------|-----|
| Customer Segments | Pemilik bengkel, pemilik kendaraan, mekanik, penggemar DIY |
| Value Propositions | Diagnosis AI cepat & akurat, instruksi perbaikan, rekomendasi suku cadang, visualisasi 3D modifikasi |
| Channels | Platform web (Next.js), link afiliasi Shopee, Maps API |
| Customer Relationships | Self-service diagnosis, dukungan mekanik, chat AI avatar |
| Revenue Streams | Komisi afiliasi Shopee dari suku cadang dan komponen |
| Key Activities | Pengembangan model AI/RAG, rendering 3D, pemeliharaan API dan DB |
| Key Resources | Tim 2 orang, PostgreSQL + pgvector, LLM OpenAI/Claude, Celery + Redis |
| Key Partnerships | Shopee Affiliate, Maps API, penyedia LLM |
| Cost Structure | Biaya API LLM, infrastruktur server, biaya pengembangan tim |

Status semua blok: belum diuji (belum ada eksperimen atau wawancara calon pengguna).

## 8. Kebutuhan Non-Fungsional

- Performa: latensi < 200ms untuk respons diagnosis.
- Skalabilitas: pemrosesan async (Celery + Redis) untuk pengguna concurrent.
- Keamanan: sanitisasi input, autentikasi JWT, rate limiting.
- Maintainability: arsitektur modular, pengembangan TDD-first.

## 9. Milestone dan Timeline

| Milestone | Deskripsi | Target |
|-----------|-----------|--------|
| M0 | Project Kickoff & Finalisasi Arsitektur | Minggu 1 |
| M1 | Implementasi Skema Database & Unit Tests | Minggu 2 |
| M2 | Backend API (Diagnosis & 3D) + Frontend Skeleton | Minggu 3 |
| M3 | Modul RAG Diagnostik + Integrasi Shopee | Minggu 4 |
| M4 | Integrasi Fitur Penuh & QA | Minggu 5 |
| M5 | Rilis Production Ready | Minggu 6 |

## 10. Butuhan Dana

Biaya API LLM (OpenAI/Claude), infrastruktur server (PostgreSQL + pgvector, Celery + Redis), dan biaya pengembangan tim. Rincian anggaran akan disesuaikan dengan format anggaran UKRI.

## 11. Tim

- fajar1180 — Project Manager, System Analyst, Backend, Frontend, QA Testing
- ilhamalmunawar05-cpu — System Analyst, Backend Developer, Frontend Developer, QA Engineer

## 12. Kesimpulan

Platform Otomotif AI menawarkan solusi diagnosis kendaraan berbasis AI yang cepat, akurat (>85%), dan transparan biaya, mengurangi kunjungan tidak perlu ke bengkel dengan monetisasi melalui afiliasi Shopee. Siap untuk dikembangkan ke MVP dan diuji ke calon pengguna riil.

---
*Dokumen ini disesuaikan dengan isi PRD, SRS, ERD, API Spec, dan UI/UX Design Specification yang tersimpan di `docs/`.*