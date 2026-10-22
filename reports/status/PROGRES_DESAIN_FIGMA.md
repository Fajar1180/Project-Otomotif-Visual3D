# Progres Desain Figma — Project Pak Yogi

Terakhir diperbarui: 19 Oktober 2026

## Status

| Tahap | Status | Catatan |
|-------|--------|---------|
| 1. File Figma | Selesai | `Project_Pak_Yogi_Design` |
| 2. Design System | Selesai | 14 color style, 7 text style, 5 komponen |
| 3. Layar Utama | Selesai | Dashboard, Konfigurasi 3D, Diagnosis AI (1920×1080) |
| 4. Prototyping | **Belum** | Terhambat limit MCP |
| 5. Dokumentasi komponen | **Belum** | Deskripsi komponen belum diisi |
| 6. Handoff pengembang | **Belum** | Code Connect belum disiapkan |

## Akses File

- URL: https://www.figma.com/design/15sd06ulTtQidYcKu1lPDb
- Nama file: `Project_Pak_Yogi_Design`
- Pemilik/akun: catuk ptinti (catukptinti@gmail.com)
- Tim: `catuk ptinti's team` — key `team::1693893847498823315`
- Plan: **Starter** — maksimal 3 halaman per file, ada batas panggilan Figma MCP

## Halaman

1. `🎨 Design System` — papan token warna & tipografi, pustaka komponen
2. `📱 Screens` — 3 frame layar 1920×1080
3. `🔄 Prototypes` — masih kosong

## Design System

### Color Style (14)
| Nama | Hex |
|------|-----|
| Primary/Dark | #0A2463 |
| Primary/Main | #1E4E79 |
| Primary/Light | #2563AB |
| Secondary/Dark | #92400E |
| Secondary/Main | #D97706 |
| Secondary/Light | #F59E0B |
| Status/Success | #059669 |
| Status/Warning | #D97706 |
| Status/Error | #DC2626 |
| Status/Info | #2563AB |
| Neutral/Dark | #111827 |
| Neutral/Gray | #6B7280 |
| Neutral/Light | #F3F4F6 |
| Neutral/White | #FFFFFF |

### Text Style (7) — font Inter
| Nama | Gaya | Ukuran | Line height |
|------|------|--------|-------------|
| Heading/H1 | Bold | 32 | 140% |
| Heading/H2 | Bold | 24 | 120% |
| Heading/H3 | Semi Bold | 20 | 120% |
| Heading/H4 | Semi Bold | 18 | 120% |
| Body/Regular | Regular | 16 | 160% |
| Body/Small | Regular | 14 | 140% |
| Body/Caption | Medium | 12 | 100% |

### Komponen (component set)
- `Tombol` — varian `Gaya=Primary`, `Gaya=Secondary`, `Gaya=Ghost`; radius 8px, padding 12/24
- `Badge` — varian `Tingkat=DIY Mudah`, `DIY Sulit`, `Butuh Bengkel`; radius 16px
- `Kartu/Dasar` — 360×200, radius 12px, border 1px #E5E7EB
- `Input/Teks` — 360×48, radius 8px, border 2px #E5E7EB

## Layar

Semua frame berukuran 1920×1080, tersusun horizontal di halaman `📱 Screens` (x = 0, 2000, 4000).

### Dashboard
- Navbar gradient #0A2463 → #1E4E79, sub-nav 6 menu (Dashboard aktif)
- 3 kartu: Diagnosis Terakhir (aksen hijau, badge DIY Mudah), Konfigurasi 3D (4 langkah), Statistik (12/5/28/3)
- 4 kartu Aksi Cepat: Diagnosis Masalah, Kustomisasi 3D, Cari Bengkel, Beli Suku Cadang
- Footer: "Platform Otomotif AI · Proyek Pak Yogi · Sprint 1"

### Konfigurasi 3D
- Kanvas kiri 1344px + toolbar melayang (Reset, Zoom +, Zoom −, Putar, Simpan)
- Panel kanan 576px: akordeon kategori Roda (terbuka, 2 item), Knalpot, Body Kit, Suspensi
- Kartu item: nama, harga, status stok, tombol Pratinjau & Pasang
- Legenda stok + total penyesuaian Rp 1.850.000

### Diagnosis AI
- Panel kiri: textarea + tombol rekam, pemilih kendaraan, 4 contoh pertanyaan, tombol Analisis Sekarang
- Panel kanan: badge Butuh Bengkel, keyakinan 92%, penjelasan teknis CVT, 6 langkah perbaikan, 2 kartu suku cadang (V-Belt Rp 95.000, Roller CVT Rp 140.000), bengkel terdekat

## Yang Belum Selesai

### 1. Penyambungan prototipe (prioritas)
Semua frame belum punya interaksi. Langkah:

1. Buka halaman `📱 Screens`, pilih frame `Dashboard`, aktifkan tab **Prototype** di panel kanan.
2. Klik teks **"Mulai Kustomisasi"** → tarik panah ke frame `Konfigurasi 3D`. Trigger **On click**, Navigate to, Smart Animate 300ms, Ease out.
3. Klik teks **"Lihat Detail"** → ke frame `Diagnosis AI`.
4. Di frame `Konfigurasi 3D` dan `Diagnosis AI`: klik menu **"Dashboard"** di sub-nav → kembali ke frame `Dashboard`.
5. Tandai setiap frame sebagai flow starting point (ikon ▶ pada panel Prototype): `Alur Utama`, `Alur Konfigurasi`, `Alur Diagnosis`.

Catatan: sudah dicoba otomatis lewat Figma MCP (`setReactionsAsync` + `flowStartingPoints`) tetapi gagal karena batas panggilan plan Starter. Kalau limit sudah pulih, bisa dijalankan ulang otomatis.

### 2. Dokumentasi komponen
Isi kolom deskripsi setiap komponen: tujuan, kapan dipakai, aturan padding, larangan. Gunakan panel kanan → bagian deskripsi komponen.

### 3. Handoff pengembang
- Tambahkan Code Connect untuk komponen `Tombol`, `Badge`, `Kartu/Dasar`, `Input/Teks` setelah komponen React-nya ada.
- Ekspor token warna/tipografi dari Figma sebagai variabel, samakan dengan `DESIGN.md` di repo.

### 4. Layar tambahan (opsional, butuh halaman/plan lebih besar)
- Pencarian Bengkel (peta + daftar)
- Login & Daftar
- Profil / Pengaturan
- Katalog Suku Cadang
- Riwayat Diagnosis

## Batasan yang Perlu Diketahui Tim

- Plan Starter hanya mengizinkan **3 halaman per file**. Layar tambahan harus masuk ke halaman `📱 Screens` atau dibuat file terpisah.
- Figma MCP punya kuota panggilan; kalau habis, otomatisasi berhenti sampai limit direset.
- Font Inter harus terpasang di aplikasi Figma agar teks tidak berubah tampilan.

## Jalur Sementara: Canva

Karena Figma MCP kena batas panggilan, desain layar dialihkan sementara ke Canva sebagai **deck presentasi** (bukan file komponen).

- Judul: `OTOMOTIF AI` — ID `DAHYdFVr81I`
- Edit: https://www.canva.com/d/OOdRQgtqK7AJ52p
- Lihat: https://www.canva.com/d/H_EccmNyAe0YphZ
- 4 slide 16:9 (1920×1080): 1 sampul, 2 Dashboard, 3 Konfigurasi 3D, 4 Diagnosis AI
- Isi layar = hasil render `design/mockups/*.html` (gambar, bukan elemen vektor terpisah)

Keterbatasan Canva untuk pekerjaan ini:
- Tidak ada komponen/varian/auto layout → Design System tidak bisa dibangun di Canva
- Gambar layar tidak bisa diedit per elemen; revisi harus lewat file Figma/HTML lalu render ulang
- Jadi Canva dipakai untuk presentasi & review cepat, Figma tetap sumber desain

## Riwayat Pembaruan

- 19 Okt 2026 — Figma: file dibuat, 3 halaman, Design System (14 color style, 7 text style, 5 komponen), 3 frame layar 1920×1080. Prototype gagal karena kuota MCP.
- 19 Okt 2026 — Canva: render `design/mockups/*.html` → 3 PNG (1920×1080) → unggah sebagai aset → deck `OTOMOTIF AI` 4 slide diisi screenshot, disimpan (committed) dan diverifikasi lewat thumbnail.
- 19 Okt 2026 — Catatan progres ini dibuat dan di-push agar tim bisa meneruskan.

## Langkah Berikutnya (urut prioritas)

1. Sambungkan prototype di Figma (langkah manual ada di bagian "Yang Belum Selesai").
2. Verifikasi visual frame `Konfigurasi 3D` — satu-satunya layar yang belum dicek ulang setelah rebuild.
3. Isi deskripsi komponen di Figma.
4. Tambah slide spesifikasi (palet, tipografi, komponen) ke deck Canva bila dipakai untuk presentasi.
5. Ganti placeholder judul slide Canva yang menduplikasi heading di dalam gambar.

## Berkas Terkait di Repo
- `docs/UI_UX_Design_Specification.md` — spesifikasi desain lengkap
- `DESIGN.md` — token desain
- `design/figma-design-specification.json` — token format JSON
- `design/mockups/dashboard.html`, `3d-configurator.html`, `ai-diagnosis.html` — mockup HTML acuan
- `FIGMA_MANUAL_GUIDE.md` — panduan langkah manual
