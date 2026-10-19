# Spesifikasi Kebutuhan Perangkat Lunak (SRS)
## Platform Otomotif AI (Project Pak Yogi)

### 1. Pendahuluan
Dokumen ini menspesifikasikan kebutuhan perangkat lunak untuk Platform Otomotif AI (Project Pak Yogi), aplikasi Web-First untuk diagnosis kendaraan dan visualisasi modifikasi.

#### 1.1 Tujuan
Memberikan deskripsi lengkap kebutuhan fungsional dan non-fungsional untuk Platform Otomotif AI.

#### 1.2 Ruang Lingkup
Sistem mencakup:
- Visualisasi modifikasi kendaraan 3D dengan rekomendasi suku cadang berbasis AI
- Diagnosis AI conversational untuk masalah kendaraan via input bahasa natural
- Integrasi dengan Shopee Affiliate untuk pembelian suku cadang
- Integrasi pencari bengkel

#### 1.3 Definisi, Akronim, dan Singkatan
- **AI:** Kecerdasan Buatan (Artificial Intelligence)
- **RAG:** Retrieval-Augmented Generation
- **LLM:** Large Language Model
- **TDD:** Test-Driven Development
- **REST:** Representational State Transfer
- **API:** Application Programming Interface
- **ERD:** Entity Relationship Diagram

#### 1.4 Referensi
1. [PRD_Project_Pak_Yogi.md](PRD_Project_Pak_Yogi.md) - Dokumen Kebutuhan Proyek
2. Skema database di ide-dasar.txt
3. Spesifikasi API di ide-dasar.txt

#### 1.5 Ikhtisar
- Bagian 2: Deskripsi Umum
- Bagian 3: Kebutuhan Spesifik (Fungsional & Non-fungsional)
- Bagian 4: Kebutuhan Antarmuka Eksternal
- Bagian 5: Fitur Sistem
- Bagian 6: Kebutuhan Non-fungsional Lainnya

### 2. Deskripsi Umum
#### 2.1 Perspektif Produk
Aplikasi web mandiri dengan layanan API backend, database PostgreSQL, dan integrasi dengan layanan eksternal (Shopee API, Google Maps API).

#### 2.2 Fungsi Produk
| Fungsi | Deskripsi |
|----------|-------------|
| Visualisasi 3D | Rendering model 3D real-time dan modifikasi |
| Diagnosis AI | Pemrosesan bahasa natural untuk analisis masalah |
| Rekomendasi Suku Cadang | Saran suku cadang cerdas dengan link affiliate |
| Pencari Bengkel | Penemuan bengkel berbasis lokasi |

#### 2.3 Kelas Pengguna dan Karakteristik
| Tipe Pengguna | Deskripsi |
|-----------|-------------|
| Pemilik Kendaraan | Mencari diagnosis dan panduan perbaikan untuk kendaraannya |
| Penggemar DIY | Mencari instruksi perbaikan langkah-demi-langkah |
| Mekanik | Menggunakan platform sebagai alat referensi diagnosis |
| Pemilik Bengkel | Terdaftar di pencari bengkel untuk akuisisi pelanggan |

#### 2.4 Lingkungan Operasional
- Web browser: Chrome, Firefox, Safari (versi terbaru)
- Backend: Server Linux/Windows dengan Python 3.8+
- Database: PostgreSQL 14+ dengan ekstensi pgvector
- Frontend: Node.js 16+, Next.js 13+

#### 2.5 Kendala Desain dan Implementasi
- Harus menggunakan metodologi Test-Driven Development
- Frontend: Next.js App Router, React Three Fiber
- Backend: FastAPI, Python async
- Database: PostgreSQL + pgvector untuk vector search
- Budget: Tools open-source + layanan cloud (Vercel, Render, dll)

#### 2.6 Dokumentasi Pengguna
- Sistem bantuan online terintegrasi di platform
- Dokumentasi API via OpenAPI/Swagger
- Dokumentasi developer di file CODEOWNERS dan CONTRIBUTING

### 3. Kebutuhan Spesifik

#### 3.1 Kebutuhan Fungsional

##### 3.1.1 Autentikasi Pengguna & Profil
**FR-001:** Sistem HARUS mengizinkan pengguna membuat akun dengan email/password
**FR-002:** Sistem HARUS mendukung login Google OAuth sebagai alternatif
**FR-003:** Sistem HARUS mempertahankan state sesi pengguna dengan token JWT
**FR-004:** Sistem HARUS mengizinkan update profil (nama, kendaraan favorit, lokasi)

##### 3.1.2 3D Vehicle Configurator
**FR-005:** Sistem HARUS menampilkan model 3D kendaraan interaktif di browser
**FR-006:** Sistem HARUS mengizinkan pengguna memilih dan menukar komponen kendaraan (roda, knalpot, dll)
**FR-007:** Sistem HARUS menyorot komponen yang dimodifikasi dengan indikator visual
**FR-008:** Sistem HARUS generate ID modifikasi unik untuk setiap konfigurasi
**FR-009:** Sistem HARUS menyimpan konfigurasi pengguna ke profil mereka

##### 3.1.3 Mesin Diagnosis AI
**FR-010:** Sistem HARUS menerima input bahasa natural (teks atau suara) yang mendeskripsikan masalah kendaraan
**FR-011:** Sistem HARUS memproses input melalui RAG pipeline dengan embedding khusus kendaraan
**FR-012:** Sistem HARUS mengembalikan hasil diagnosis dengan:
  - ID Diagnosis dan judul
  - Penjelasan teknis
  - Tingkat keparahan (DIY_EASY, DIY_HARD, WORKSHOP_REQUIRED)
  - Instruksi perbaikan langkah-demi-langkah (array JSONB)
  - Daftar suku cadang yang direkomendasikan
  - Saran bengkel terdekat (jika tingkat keparahan = WORKSHOP_REQUIRED)
**FR-013:** Sistem HARUS melakukan caching query sering untuk memperbaiki response time
**FR-014:** Sistem HARUS menyediakan skor kepercayaan untuk setiap diagnosis

##### 3.1.4 Integrasi Shopee Affiliate
**FR-015:** Sistem HARUS mengekstrak kata kunci dari diagnosis untuk mencari katalog Shopee
**FR-016:** Sistem HARUS generate link affiliate untuk suku cadang yang direkomendasikan
**FR-017:** Sistem HARUS menampilkan estimasi harga dan ketersediaan dari Shopee
**FR-018:** Sistem HARUS melacak klik pada link affiliate untuk analitik

##### 3.1.5 Pencari Bengkel
**FR-019:** Sistem HARUS terintegrasi dengan Google Maps API untuk layanan lokasi
**FR-020:** Sistem HARUS menampilkan bengkel dalam radius 25km untuk diagnosis WORKSHOP_REQUIRED
**FR-021:** Sistem HARUS menampilkan rating bengkel, spesialisasi, dan info kontak
**FR-022:** Sistem HARUS menyediakan navigasi turn-by-turn ke bengkel yang dipilih

##### 3.1.6 Fungsi Administratif
**FR-023:** Administrator HARUS mengelola merek/model kendaraan di database
**FR-024:** Administrator HARUS mengupdate mapping gejala-penyakit
**FR-025:** Administrator HARUS memoderasi listing bengkel
**FR-026:** Sistem HARUS mencatat semua request API untuk keperluan audit

#### 3.2 Kebutuhan Non-Fungsional

##### 3.2.1 Kebutuhan Performa
**NFR-001:** Response time API diagnosis HARUS < 500ms untuk 95% request
**NFR-002:** Waktu load model 3D HARUS < 3 detik di perangkat mobile
**NFR-003:** Sistem HARUS mendukung 100 pengguna concurrent tanpa degradasi
**NFR-004:** Query database dengan vector search HARUS selesai < 200ms

##### 3.2.2 Kebutuhan Keamanan (Safety)
**NFR-005:** Sistem HARUS menampilkan disclaimer bahwa diagnosis bersifat advisory only
**NFR-006:** Masalah keamanan kritis HARUS selalu merekomendasikan kunjungan bengkel profesional
**NFR-007:** Semua peringatan keamanan medis/kimia HARUS disertakan dalam langkah perbaikan

##### 3.2.3 Kebutuhan Keamanan (Security)
**NFR-008:** Semua input pengguna HARUS disanitasi untuk mencegah XSS/SQL injection
**NFR-009:** Password HARUS di-hash menggunakan bcrypt dengan salt
**NFR-010:** Endpoint API HARUS memerlukan autentikasi (kecuali endpoint diagnosis publik)
**NFR-011:** Rate limiting HARUS diterapkan untuk mencegah penyalahgunaan (100 req/jam/IP)
**NFR-012:** Token JWT HARUS expired setelah 24 jam dengan mekanisme refresh

##### 3.2.4 Kebutuhan Portabilitas
**NFR-013:** Frontend HARUS responsif di mobile (lebar 320px) dan desktop (lebar 1920px)
**NFR-014:** Backend HARUS deploy ke container Docker
**NFR-015:** Migrasi database HARUS terkontrol versi

##### 3.2.5 Kebutuhan Maintainability
**NFR-016:** Kode HARUS mengikuti standar PEP 8 (Python) dan ESLint (JavaScript)
**NFR-017:** Minimal 80% test coverage diperlukan untuk semua kode baru
**NFR-018:** Dokumentasi HARUS diupdate dengan setiap rilis fitur
**NFR-019:** Logging HARUS mengikuti format terstruktur (JSON) untuk kompatibilitas ELK stack

### 4. Kebutuhan Antarmuka Eksternal

#### 4.1 Antarmuka Pengguna
**UI-001:** Frontend HARUS menggunakan Tailwind CSS untuk styling konsisten
**UI-002:** Kanvas 3D HARUS memenuhi minimal 60vh di halaman diagnosis
**UI-003:** Skema warna HARUS menggunakan palet automotive-inspired (dark blues, metallic grays)
**UI-004:** Tipografi HARUS memprioritaskan keterbacaan (Inter atau sans-serif serupa)

#### 4.2 Antarmuka Hardware
**HI-001:** Sistem HARUS mendukung input mikrofon untuk diagnosis suara
**HI-002:** Sistem HARUS mendukung input kamera untuk fitur computer vision masa depan
**HI-003:** Event sentuh HARUS didukung untuk interaksi mobile

#### 4.3 Antarmuka Perangkat Lunak
**SI-001:** Backend HARUS mengekspos RESTful JSON API di bawah `/api/v1/`
**SI-002:** Database HARUS menggunakan PostgreSQL dengan ekstensi pgvector
**SI-003:** API Eksternal:
  - Shopee Affiliate API (untuk pencarian produk dan generate link)
  - Google Maps API (untuk geolokasi bengkel)
  - OpenAI/Claude API (untuk LLM di RAG pipeline)
**SI-004:** Autentikasi HARUS menggunakan JWT dengan refresh tokens

#### 4.4 Antarmuka Komunikasi
**CI-001:** Sistem HARUS berkomunikasi via HTTPS saja
**CI-002:** Request API HARUS menggunakan format JSON
**CI-003:** Koneksi WebSocket HARUS digunakan untuk update 3D real-time
**CI-004:** Notifikasi email HARUS menggunakan SMTP untuk alert pengguna

### 5. Fitur Sistem

#### 5.1 Fitur: 3D Vehicle Configurator
**Deskripsi:** Visualisasi 3D interaktif mengizinkan pengguna memodifikasi tampilan kendaraan
**Stimulus:** Pengguna memilih kategori komponen (roda, knalpot, body kit)
**Respons:**
  - Tampilkan opsi yang tersedia di panel scrollable
  - Preview komponen yang dipilih di model 3D real-time
  - Konfirmasi pemilihan dengan tombol "Apply"
  - Update ID modifikasi dan simpan ke profil pengguna

#### 5.2 Fitur: Mesin Diagnosis AI
**Deskripsi:** AI conversational yang menginterpretasi masalah kendaraan dan memberikan solusi
**Stimulus:** Pengguna submit deskripsi bahasa natural masalah kendaraan
**Respons:**
  - Proses input melalui RAG pipeline dengan embedding gejala
  - Ambil top-k diagnosis yang cocok dengan skor kepercayaan
  - Generate penjelasan detail menggunakan LLM dengan konteks teknis
  - Klasifikasikan tingkat keparahan berdasarkan kompleksitas perbaikan dan implikasi keamanan
  - Kembalikan JSON terstruktur dengan detail diagnosis, langkah perbaikan, suku cadang, bengkel

#### 5.3 Fitur: Integrasi Shopee Affiliate
**Deskripsi:** Monetisasi melalui link affiliate untuk suku cadang yang direkomendasikan
**Stimulus:** Diagnosis mengembalikan daftar suku cadang yang direkomendasikan
**Respons:**
  - Ekstrak kata kunci (nama suku cadang, model kendaraan, brand) dari diagnosis
  - Query Shopee Affiliate API untuk produk yang cocok
  - Generate link affiliate yang dapat dilacak dengan parameter UTM
  - Tampilkan harga, ketersediaan, dan rating penjual
  - Catat event klik untuk atribusi revenue

#### 5.4 Fitur: Pencari Bengkel
**Deskripsi:** Menemukan bengkel perbaikan terdekat untuk masalah kompleks
**Stimulus:** Tingkat keparahan diagnosis = WORKSHOP_REQUIRED
**Respons:**
  - Dapatkan lokasi pengguna (dengan izin) atau gunakan aproksimasi berbasis IP
  - Query Google Maps Place API untuk "auto repair" dalam radius
  - Filter hasil berdasarkan spesialisasi kendaraan jika tersedia di database
  - Tampilkan hasil dalam tampilan list dan map dengan sorting jarak
  - Sediakan tombol "Navigasi" meluncurkan aplikasi maps eksternal

### 6. Kebutuhan Non-Fungsional Lainnya

#### 6.1 Reliabilitas
- Sistem HARUS mencapai uptime bulanan 99.5%
- Backup database HARUS terjadi harian dengan point-in-time recovery
- Error rate HARUS dimonitor dan di-alert via metrik SLO/SLI

#### 6.2 Maintainability
- Technical debt HARUS dilacak dan diatasi di sprint planning
- Code review HARUS mandatory untuk semua perubahan production
- Update dependency HARUS diuji di staging sebelum production

#### 6.3 Portabilitas
- Artifact deployment HARUS berbentuk versi dan immutable
- Infrastruktur HARUS didefinisikan sebagai kode (Terraform/CloudFormation)
- Variabel environment HARUS mengelola perbedaan konfigurasi

#### 6.4 Usability
- Platform HARUS mencapai skor SUS > 75 dalam user testing
- Pesan error HARUS user-friendly dan actionable
- Tooltip bantuan HARUS tersedia untuk fitur kompleks
- Loading state HARUS ditampilkan untuk semua operasi asynchronous

### 7. Lampiran

#### 7.1 Glosarium
- **DIY_EASY:** Perbaikan butuh tools basic (< 1 jam)
- **DIY_HARD:** Perbaikan butuh skill/tools menengah (1-4 jam)
- **WORKSHOP_REQUIRED:** Perbaikan butuh peralatan/keahlian profesional
- **pgvector:** Ekstensi PostgreSQL untuk similarity search vektor
- **RAG:** Teknik menggabungkan retrieval dengan generation untuk AI grounded
- **TDD:** Praktik development menulis test sebelum implementasi

#### 7.2 Model Analisis
*Definisi entitas dari skema database:*
- **vehicles:** id (UUID), brand (string), model (string), year_start/end (int), category (string)
- **symptoms:** id (UUID), symptom_code (string), description (text), category (string), embedding (vector)
- **diagnoses:** id (UUID), title (string), technical_explanation (text), severity_level (enum), repair_steps (JSONB)
- **spare_parts:** id (UUID), part_name (string), part_number (string), brand (string), price_min/max (numeric), shopee_item_id/shop_id (string), default_shopee_url (text)
- **workshops:** id (UUID), name (string), address (text), latitude/longitude (double), rating (numeric), specialties (text array)
- **mappings:** symptom_id/diagnosis_id (UUID foreign keys), confidence_weight (float); diagnosis_id/spare_part_id (UUID foreign keys), is_primary (boolean)

#### 7.3 To Be Determined (TBD)
- Struktur komisi affiliate Shopee pasti untuk difinalisasi
- Batas penggunaan Google Maps API dan proyeksi biaya
- Keputusan final provider LLM (OpenAPI vs Claude vs open-source)
- Roadmap mobile app (Fase 2)

---
*Versi Dokumen 1.0 | Dibuat: 19 Oktober 2026*
