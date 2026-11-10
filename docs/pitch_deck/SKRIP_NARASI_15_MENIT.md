# SKRIP NARASI — Usulan Ide Startup Digital
**Durasi:** 15 menit  
**Topik:** Platform Otomotif AI (Project Pak Yogi)  
**Penyaji:** fajar1180 &amp; ilhamalmunawar05-cpu  

---

## Panduan Waktu (15 menit)

| Bagian | Waktu | Slide |
|--------|-------|-------|
| Pembuka & Perkenalan | 1 menit | Slide 1 |
| Masalah | 2 menit | Slide 2 |
| Solusi | 2 menit | Slide 3 |
| Produk (MVP) | 2 menit | Slide 4 |
| Pasar | 1 menit | Slide 5 |
| Model Bisnis | 1 menit | Slide 6 |
| Traction | 1 menit | Slide 7 |
| Tim | 1 menit | Slide 8 |
| Butuhan Dana | 1 menit | Slide 9 |
| Roadmap | 1 menit | Slide 10 |
| Penutup & QA | 2 menit | Slide 11 |

---

## Skrip Narasi Lengkap

### [0:00–1:00] Pembuka & Perkenalan (Slide 1)
"Assalamualaikum wr. wb. Selamat pagi/siang/sore, para pengajar dan rekan-rekan. Nama saya [Nama], bersama rekan saya [Nama]. Kami berasal dari tim Platform Otomotif AI, atau dikenal sebagai Project Pak Yogi.

Hari ini kami akan mempresentasikan usulan ide startup digital kami: sebuah platform web yang menggabungkan kecerdasan buatan untuk diagnosis kerusakan kendaraan dan konfigurasi modifikasi kendaraan dalam 3D. Presentasi ini akan memakan waktu sekitar 15 menit, dengan 11 slide. Mari kita mulai."

---

### [1:00–3:00] Masalah (Slide 2)
"Pertama, mari kita bahas masalah. Di Indonesia, banyak pemilik kendaraan — baik mobil maupun motor — yang kesulitan mendiagnosa kerusakan kendaraan mereka sendiri ketika terjadi gejala aneh.

Saat ini, solusi utama yang ada adalah datang langsung ke bengkel konvensional dan bertanya langsung kepada mekanik. Namun, ada tiga masalah di sini.

Pertama, tidak ada estimasi biaya dan kerusakan sebelum datang ke bengkel. Kedua, ini membuang waktu dan biaya transportasi, terutama jika kerusakan justru ringan dan bisa diatasi sendiri. Ketiga, tidak ada solusi mandiri yang cepat dan transparan bagi pemilik kendaraan.

Ini adalah pain point nyata yang kami ingin pecahkan."

---

### [3:00–5:00] Solusi (Slide 3)
"Kami menawarkan dua solusi inti.

Pertama, AI Storytelling Diagnosis. Pengguna menginputkan keluhan kerusakan kendaraan melalui teks atau audio. Sistem menggunakan NLP dan RAG untuk menginterpretasikan keluhan tersebut, mengklasifikasikan tingkat keparahan — apakah DIY mudah, DIY sulit, atau perlu bengkel — kemudian memberikan instruksi perbaikan langkah-demi-langkah dan rekomendasi suku cadang.

Kedua, AI 3D Modification Configurator dan Shopee Recommender. Pengguna dapat memvisualisasikan modifikasi kendaraan dalam 3D, menukarkan komponen secara real-time, mendapatkan link afiliasi Shopee untuk suku cadang, dan mencari bengkel terdekat melalui Maps API.

Manfaat utamanya: diagnosa lebih cepat, estimasi biaya lebih transparan, dan mengurangi kunjungan tidak perlu ke bengkel."

---

### [5:00–7:00] Produk / MVP (Slide 4)
"Untuk MVP, kami fokus pada satu fitur inti: diagnosis satu kategori kerusakan, contohnya kerusakan mesin mobil.

Produk MVP memiliki tiga fitur utama. Satu, input cerita keluhan dalam teks beserta konteks kendaraan. Dua, hasil diagnosis dengan tingkat keparahan: DIY_EASY, DIY_HARD, atau WORKSHOP_REQUIRED. Tiga, langkah perbaikan dan rekomendasi suku cadang.

Secara teknis, kami menggunakan endpoint FastAPI POST /api/v1/diagnosis/analyze dengan pipeline RAG yang dijalankan oleh OpenAI atau Claude. Fitur lain seperti konfigurator 3D, integrasi Shopee, pencari bengkel, riwayat diagnosis, dan autentikasi pengguna ditunda ke tahap berikutnya."

---

### [7:00–8:00] Pasar (Slide 5)
"Pasar target kami cukup lebar. Di Indonesia, budaya modifikasi kendaraan — terutama motor — mengalami pertumbuhan tinggi, dengan gaya seperti Thailook, Bratstyle, dan Cafe Racer.

Segmen pelanggan kami meliputi pemilik bengkel, pemilik kendaraan mobil dan motor, mekanik, serta penggemar DIY yang mencari referensi diagnosis. Peluang bisnis utama ada pada monetisasi melalui Program Affiliate Shopee."

---

### [8:00–9:00] Model Bisnis (Slide 6)
"Model bisnis kami sederhana: komisi afiliasi Shopee dari penjualan suku cadang dan komponen modifikasi yang direkomendasikan melalui platform.

Channel distribusi adalah platform web berbasis Next.js, link afiliasi Shopee, dan integrasi Maps API. Sisi biaya mencakup biaya API LLM, infrastruktur server seperti PostgreSQL dengan pgvector dan Celery plus Redis, serta biaya pengembangan tim."

---

### [9:00–10:00] Traction (Slide 7)
"Saat ini kami masih di fase inisiasi. Dokumentasi lengkap sudah siap: PRD versi 1.0, SRS dengan 26 kebutuhan fungsional, ERD, spesifikasi API OpenAPI 3.0, dan spesifikasi UI/UX desain.

Backend FastAPI untuk diagnosis, RAG, dan database pgvector sedang dalam pengembangan, serta frontend Next.js dengan React Three Fiber untuk rendering 3D.

Validasi ke calon pengguna riil dan eksperimen akurasi diagnosis lebih dari 85 persen dengan latensi API di bawah 200 milidetik masih akan kami lakukan setelah ini."

---

### [10:00–11:00] Tim (Slide 8)
"Tim kami terdiri dari dua orang dengan latar belakang multidisipiliner.

fajar1180 bertugas sebagai Project Manager, System Analyst, Backend, Frontend, dan QA Testing. Sementara ilhamalmunawar05-cpu bertugas sebagai System Analyst, Backend Developer, Frontend Developer, dan QA Engineer."

---

### [11:00–12:00] Butuhan Dana (Slide 9)
"Untuk mengembangkan platform ini, kami membutuhkan dana untuk tiga hal utama.

Pertama, biaya API LLM seperti OpenAI atau Claude untuk menjalankan pipeline RAG. Kedua, infrastruktur server, yaitu PostgreSQL dengan ekstensi pgvector untuk pencarian vektor, serta Celery dan Redis untuk pemrosesan asynchronous. Ketiga, biaya pengembangan tim sebanyak dua orang.

Rincian anggaran akan kami sesuaikan dengan format anggaran yang ditetapkan oleh UKRI."

---

### [12:00–13:00] Roadmap (Slide 10)
"Roadmap kami direncanakan dalam enam minggu hingga production ready.

Minggu satu: kickoff dan finalisasi arsitektur. Minggu dua: implementasi skema database dan unit tests. Minggu tiga: backend API diagnosis dan 3D beserta skeleton frontend. Minggu empat: modul RAG diagnostik dan integrasi Shopee. Minggu lima: integrasi fitur penuh dan QA. Dan minggu enam: rilis production ready."

---

### [13:00–15:00] Penutup & QA (Slide 11)
"Untuk menyimpulkan, Platform Otomotif AI menawarkan solusi diagnosis kendaraan berbasis AI yang cepat, akurat di atas 85 persen, dan transparan biaya. Kami ingin mengurangi kunjungan tidak perlu ke bengkel dengan monetisasi melalui komisi afiliasi Shopee.

Platform ini siap untuk dikembangkan ke MVP dan diuji langsung kepada calon pengguna riil.

Terima kasih atas perhatiannya. Kami siap menerima pertanyaan dari Bapak/Ibu pengajar dan rekan-rekan."

Wassalamualaikum wr. wb."

---

## Tips Presentasi
- Bicara nyatural, jangan membaca slide secara kata per kata.
- Gunakan slide sebagai pointer, sampaikan detail secara lisan.
- Sisa waktu 2 menit di akhir khusus untuk QA.
- Siapkan demo singkat endpoint `/api/v1/diagnosis/analyze` jika diminta.