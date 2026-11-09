# Aturan Kerja Tim (RULES)

**Proyek:** Sistem Informasi Kolaborasi Pendidikan dan Industri — Kelompok 6
**Berlaku untuk:** seluruh anggota tim, baik mengerjakan manual maupun dibantu AI.
**Acuan utama:** Dokumen Perencanaan Proyek (KAK, PRD, Sprint Backlog) + repo [baneeishaque/ai-agent-rules](https://github.com/baneeishaque/ai-agent-rules).

---

## 1. Aturan Branch (WAJIB)

1. **Sebelum mengerjakan fitur, wajib buat branch khusus** untuk fitur tersebut.
   Jangan langsung mengerjakan di `main`.
   - Format penamaan: `feature/<nama-fitur>` (contoh: `feature/login`, `feature/pengajuan-penempatan`)
   - Buat dari `develop`: `git checkout develop && git pull && git checkout -b feature/login`
2. **Sebelum push ke `main`, wajib membuat Pull Request (PR) terlebih dahulu.**
   - PR dari `feature/xxx` → `develop` untuk review harian.
   - PR dari `develop` → `main` hanya dibuka **Project Manager** (rilis).
3. **Dilarang push branch jika fitur yang dikerjakan masih ada error.**
   - Wajib lulus uji lokal dulu (fitur jalan, tidak ada error baru) sebelum push.
   - Progress boleh di-commit sebagai draf hanya jika tertulis jelas `[WIP]` dan **tidak** dibuat PR.
4. **`main` tidak boleh diganggu gugat** — hanya Project Manager (Muhammad Fajar Nurjaman) yang boleh merge ke `main`, menghapus/memforce-push `main`, atau mengubah proteksi branch.
5. **Commit message wajib Conventional Commits** (dari ai-agent-rules):
   - Pola: `type(scope): judul`
   - Type: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
   - Contoh: `feat(auth): tambah endpoint login dan reset password`
   - Satu commit = satu perubahan logis (atomic), jangan menumpuk fitur beda dalam satu commit.

## 2. Aturan Dokumentasi Progress (WAJIB)

Setiap progres yang dikerjakan **wajib dicatat** di folder `Dokumen/`:

```
Dokumen/
├── Frontend/
│   └── PROGRESS.md   ← catatan progress pihak Frontend
└── Backend/
    └── PROGRESS.md   ← catatan progress pihak Backend
```

- Isi setiap entri: tanggal, ID Sprint Backlog (`S1-xx`/`S2-xx`), branch yang dipakai, poin yang sudah dikerjakan, status, catatan/kendala.
- Update **minimal sekali selesai satu item** atau **akhir hari kerja**.
- File ini ikut di-commit bersama branch fitur (atau minimal saat buat PR).
- QA & Documentation mencatat di `Dokumen/QA/PROGRESS.md` (dibuat saat tahap pengujian).

## 3. Aturan Pull Request

1. PR dibuat lewat GitHub (atau `gh pr create`), wajib memuat:
   - Judul mengikuti Conventional Commits.
   - Deskripsi: apa yang berubah, ID Sprint Backlog, cara menguji.
   - Link issue (mis. `Closes #3`).
2. Minimal **1 review** sebelum merge. Reviewer: Project Manager atau System Analyst.
3. PR harus **mergeable tanpa konflik** — sering `git pull` dari `develop` untuk mencegah konflik menumpuk.
4. Jangan merge PR sendiri (kecuali memang diizinkan reviewer).

## 4. Aturan Pakai AI / Copilot (AI-Assisted Coding)

Diambil dari [baneeishaque/ai-agent-rules](https://github.com/baneeishaque/ai-agent-rules):

1. **Transparan:** sebutkan di deskripsi PR jika kode dibuat/bantuan AI (tool apa, bagian mana).
2. **Kode AI = kode kamu.** Wajib pahami, wajib uji, wajib bisa menjelaskan saat review. AI tidak menghapus tanggung jawab review.
3. **Jangan pernah** minta AI menulis rahasia (password, token, `.env`) ke file yang ikut ter-commit.
4. AI boleh dipakai untuk menulis kode, test, dan dokumentasi; **tidak** boleh dipakai untuk men-*skip* review atau menekan error tanpa paham penyebabnya.
5. Rencana dulu, baru eksekusi: untuk fitur besar, tulis rencana singkat di issue sebelum coding (AI maupun manual).

## 5. Aturan Keamanan & Repo

1. `.env`, kredensial, dan file sampah **tidak boleh** ikut commit — sudah dijaga `.gitignore` Laravel.
2. Jangan commit file `.env` hasil salinan `.env.example`; setiap dev punya `.env` lokal sendiri.
3. Data dummy untuk testing dibuat lewat **Seeder**, bukan data asli pengguna.
4. Dilarang force-push ke branch bersama (`develop`, `main`).

## 6. Alur Kerja Standar (Ringkasan)

```bash
# 1. Ambil kode terbaru
git checkout develop && git pull

# 2. Buat branch fitur
git checkout -b feature/nama-fitur

# 3. Kerjakan + uji lokal sampai TANPA ERROR
# 4. Catat progress di Dokumen/Frontend/PROGRESS.md atau Dokumen/Backend/PROGRESS.md

# 5. Commit dengan pesan Conventional Commits
git add -A && git commit -m "feat(scope): pesan"

# 6. Push branch & buka PR
git push -u origin feature/nama-fitur
gh pr create --base develop --head feature/nama-fitur --title "feat(scope): pesan" --body "ID: S1-xx"

# 7. Tunggu review, merge oleh reviewer
```

---

## Referensi

| Sumber | Dipakai untuk |
|---|---|
| Dokumen Perencanaan Proyek (Kelompok 6) | Sprint Backlog, Definition of Done, matriks hak akses |
| [ai-agent-rules](https://github.com/baneeishaque/ai-agent-rules) | Conventional Commits, PR management, aturan AI, keamanan |
| [panduan setup repo](./README.md) | Setup lingkungan lokal & alur tim |
