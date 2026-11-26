# Otomotif AI — Visual 3D & Diagnosis Cerdas

Platform otomotif berbasis AI: pengguna mengunggah foto kendaraan untuk dijadikan
model 3D yang bisa dikonfigurasi, berkonsultasi soal gejala kerusakan lewat
diagnosis berbasis LLM + RAG, dan mencari sparepart lewat integrasi Shopee
Affiliate.

**Stack:** FastAPI (Python 3.12) · Next.js 16 + React 19 + TailwindCSS · PostgreSQL
16 + pgvector · Redis 7 · Celery · Three.js / React Three Fiber · Docker Compose

---

## Arsitektur

```
┌────────────────┐   HTTP/JSON    ┌──────────────┐   SQL    ┌─────────────────┐
│  Next.js 16    │ ─────────────► │   FastAPI    │ ───────► │ PostgreSQL 16   │
│  (App Router)  │  /api/v1/...   │   (uvicorn)  │          │ + pgvector      │
└───────┬────────┘                └──────┬───────┘          └─────────────────┘
        │                                │ enqueue
        │ /shopee/search                 ▼
        │                         ┌──────────────┐   ┌────────────────────┐
        │                         │    Redis     │◄─►│   Celery worker    │
        │                         │broker+result │   └─────────┬──────────┘
        │                         └──────────────┘             │
        │ Three.js render                            ┌─────────▼──────────┐
        └────────────────────────────────────────────│ 3D engine adapter  │
                                                     │ Replicate / HF     │
                                                     └────────────────────┘
```

- **Frontend** — App Router; state klien via Zustand; semua HTTP lewat
  `frontend/app/lib/api.ts` yang memakai `NEXT_PUBLIC_API_URL` sebagai basis
  (tidak ada `rewrites`, jadi path relatif `/api/...` akan 404). Autentikasi
  dijaga `frontend/middleware.ts` (cookie `otomotif_auth_token`).
- **Backend** — satu router per domain (`backend/app/routes/`), logika di
  `backend/app/services/` (LLM, RAG, Shopee, 3D engine). Generasi 3D asinkron:
  endpoint balas `202 Accepted` + `task_id`, worker Celery mengerjakan, klien
  mem-poll status.
- **Worker** — `backend/app/celery_app.py`; task di `backend/app/tasks/three_d.py`.
- **Data** — PostgreSQL + `pgvector` untuk embedding RAG; status task 3D disimpan
  di `backend/app/services/task_store.py`.

### Peta API

| Method | Path | Keterangan |
|--------|------|------------|
| `POST` | `/api/v1/auth/register` | Daftar, balikan token |
| `POST` | `/api/v1/auth/login` | Login, balikan token |
| `POST` | `/api/v1/auth/refresh` | Perpanjang token |
| `POST` | `/api/v1/auth/logout` | `204` |
| `POST` | `/api/v1/3d/generate` | Upload foto kendaraan → `202` + `task_id` |
| `GET`  | `/api/v1/3d/status/{task_id}` | Progres task 3D |
| `POST` | `/api/v1/3d/modify` | Ubah warna/part model hasil generate |
| `POST` | `/api/v1/diagnosis/analyze` | Analisis gejala → diagnosis + rekomendasi |
| `GET`  | `/api/v1/diagnosis/history` | Riwayat diagnosis |
| `GET` `POST` | `/api/v1/vehicles` | Katalog kendaraan (+ `GET /{vehicle_id}`) |
| `GET`  | `/api/v1/workshops` | Direktori bengkel (+ `GET /{workshop_id}`) |
| `POST` | `/shopee/search` | Cari sparepart (Shopee Affiliate) |
| `GET`  | `/health` | Health check |

Dokumentasi interaktif: `http://localhost:8000/docs`.

### Struktur repo

```
backend/   FastAPI app, routes, services, Celery tasks, tests/
frontend/  Next.js App Router (app/), komponen, store Zustand, middleware
docs/      DESIGN_SYSTEM.md, spesifikasi UI/UX, PRD, SRS, ERD, API spec
design/    Mockup HTML & design token
guides/    Panduan (Figma, development)
reports/ research/ survey/ startup-validation/   Riset & validasi produk
docker-compose.yml
```

---

## Menjalankan lokal (tanpa Docker)

**Prasyarat:** Python 3.12, Node 20, PostgreSQL 16 + pgvector, Redis 7.

1. **Konfigurasi**

   ```bash
   cp .env.example .env
   ```

   Wajib diisi: `POSTGRES_PASSWORD`, `JWT_SECRET` (≥ 32 char —
   `openssl rand -base64 32`). Untuk run di luar Docker set juga `DATABASE_URL`
   dan `REDIS_URL` (lihat komentar di `.env.example`); di dalam Docker keduanya
   diturunkan otomatis dari `POSTGRES_*`.

   Bila `ENVIRONMENT=production`, aplikasi menolak boot kalau `JWT_SECRET` masih
   default/kosong atau `DATABASE_URL` bukan PostgreSQL.

2. **Backend**

   ```bash
   cd backend
   python -m venv .venv && source .venv/Scripts/activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload --port 8000
   ```

3. **Worker Celery** (terminal terpisah, venv sama)

   ```bash
   cd backend && celery -A app.celery_app worker --loglevel=info
   ```

4. **Frontend** (terminal terpisah)

   ```bash
   cd frontend
   npm ci
   npm run dev     # http://localhost:3000
   ```

> **Catatan:** Backend bisa dijalankan lokal tanpa Docker dan tanpa Redis. Set
> `CELERY_ALWAYS_EAGER=true` di `.env` agar task Celery dieksekusi sinkron
> (tanpa worker/broker) — cukup untuk development dan pengujian. 3D generate
> tetap balas `202` + `task_id`, tetapi diproses segera oleh aplikasi itu sendiri.

---

## Akun Demo / Dummy Login

Dua akun sudah ter-seed melalui `backend/seed/seed_auth.py` (idempotent, jalankan
`python -m seed.seed_auth` dari `backend/` atau biarkan startup seeding handle):

| Role | Email | Password | Kegunaan |
|------|-------|----------|----------|
| `user` | `user@otomotif.ai` | `UserOtomotif2026!` | Login sebagai pengguna biasa: upload foto, diagnosis, lihat riwayat |
| `admin` | `admin@otomotif.ai` | `AdminOtomotif2026!` | Login sebagai admin: akses fitur manajemen data |

---

## Menjalankan dengan Docker Compose

**Prasyarat:** Docker + Compose v2, `.env` terisi seperti di atas.

```bash
docker compose up -d --build
docker compose ps
docker compose logs -f api
```

| Service | Port host | Keterangan |
|---------|-----------|------------|
| `frontend` | `${FRONTEND_PORT:-3000}` | Next.js produksi (`npm ci && npm run build && npm start`) |
| `api` | `${API_PORT:-8000}` | FastAPI/uvicorn |
| `celery-worker` | — | Worker antrean 3D |
| `postgres` | `127.0.0.1:${POSTGRES_PORT:-5432}` | pgvector/pg16, volume `postgres_data` |
| `redis` | — (internal) | Broker + hasil task; sengaja tidak dipublikasikan |

- Compose gagal start bila `POSTGRES_PASSWORD` atau `JWT_SECRET` kosong
  (`${VAR:?...}`) — tidak ada fallback diam-diam ke kredensial default.
- `NEXT_PUBLIC_API_URL` di-inline Next.js saat **build**; mengubahnya perlu
  rebuild: `docker compose up -d --build frontend`.
- `api` dan `celery-worker` memakai image yang sama (`backend/Dockerfile`);
  `.dockerignore` menjaga `.env`, `.venv`, dan `generated_meshes/` keluar dari image.

Hentikan: `docker compose down` (`-v` untuk menghapus volume data).

---

## Pengujian

```bash
cd backend && python -m pytest        # 25 passed: unit, auth, 3D, diagnosis, E2E
cd frontend && npm run build          # type-check + build produksi
```

`npm test` di frontend masih placeholder — belum ada test UI (lihat batasan di
`docs/DESIGN_SYSTEM.md`).

---

## Variabel environment

| Variabel | Wajib | Keterangan |
|----------|-------|-----------|
| `POSTGRES_USER` `POSTGRES_PASSWORD` `POSTGRES_DB` | ya | Kredensial database |
| `JWT_SECRET` | ya | ≥ 32 char, non-default di production |
| `ENVIRONMENT` | — | `production` mengaktifkan fail-fast config |
| `NEXT_PUBLIC_API_URL` | ya (build) | Basis URL API dari browser |
| `OPENROUTER_API_KEY` | untuk diagnosis | LLM |
| `SHOPEE_APP_ID` `SHOPEE_APP_KEY` `SHOPEE_APP_SECRET` | untuk Shopee | Affiliate API |
| `THREE_D_ENGINE` | — | `replicate` / `huggingface` |
| `REPLICATE_API_TOKEN`, `HUGGINGFACE_API_TOKEN` | sesuai engine | Kredensial 3D |

Daftar lengkap di `.env.example`. **Jangan pernah commit `.env`.**

---

## Dokumentasi

- [`docs/DESIGN_SYSTEM.md`](docs/DESIGN_SYSTEM.md) — palet warna, tipografi,
  komponen, dan alur halaman, diturunkan langsung dari kode
  (`tailwind.config.ts`, `globals.css`) agar tidak bisa drift.
- [`docs/prd/PRD_Project_Pak_Yogi.md`](docs/prd/PRD_Project_Pak_Yogi.md) — PRD
- [`docs/srs/SRS_Project_Pak_Yogi.md`](docs/srs/SRS_Project_Pak_Yogi.md) — SRS
- [`docs/erd/ERD_Project_Pak_Yogi.md`](docs/erd/ERD_Project_Pak_Yogi.md) — ERD
- [`docs/api/API_Spec_Project_Pak_Yogi.md`](docs/api/API_Spec_Project_Pak_Yogi.md) — API spec
- [`docs/ui-ux/UI_UX_Design_Specification.md`](docs/ui-ux/UI_UX_Design_Specification.md) — spesifikasi UI/UX
- [`STARTUP_METHODOLOGY.md`](STARTUP_METHODOLOGY.md) — metodologi & validasi startup

## Batasan yang diketahui

- Generasi 3D bergantung pada penyedia eksternal (Replicate/HuggingFace); tanpa
  token, endpoint tetap balas `202` tetapi task gagal di worker.
- Skema DB dibuat lewat `create_all` saat startup — belum ada Alembic, perubahan
  skema butuh migrasi manual.
- Next.js 16.4.3 masih kena advisory keamanan yang memblokir `next build` sekali
  per run (percobaan kedua lanjut); perlu upgrade.

---
*Disusun oleh: Fajar1180 (PM/Developer) · ilhamalmunawar05-cpu (System Analyst/Developer)*
