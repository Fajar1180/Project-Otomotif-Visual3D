# Panduan Manual Pembuatan File Figma
## Platform Otomotif AI - Project Pak Yogi

**Target:** Membuat file desain Figma lengkap dengan sistem desain, komponen, dan layar  
**Akun:** organisasi pak-yogi (atau akun personal)  
**Nama File:** Project_Pak_Yogi_Design  
**Tanggal:** 19 Oktober 2026

---

## Prasyarat

### 1. Setup Akun Figma
- [ ] Buat/login akun Figma di https://figma.com
- [ ] Install Figma desktop app (direkomendasikan) atau gunakan versi web
- [ ] Join tim/organisasi "pak-yogi" (jika ada)

### 2. Materi Persiapan
- [ ] `design/figma-design-specification.json` - Design tokens dan spec komponen
- [ ] Folder `design/mockups/` - HTML mockups sebagai referensi visual
- [ ] `docs/UI_UX_Design_Specification.md` - Dokumentasi desain lengkap

---

## Phase 1: Buat File Figma Baru (5 menit)

### Langkah 1.1: Buat File
1. Buka Figma
2. Klik **"New design file"** 
3. Rename file: **Project_Pak_Yogi_Design**
4. Simpan ke tim "pak-yogi" (atau Drafts)

### Langkah 1.2: Setup Halaman
Buat 4 halaman (sidebar kiri):
1. **🎨 Design System** - Warna, tipografi, komponen
2. **📱 Screens** - Semua layar utama
3. **🔄 Prototypes** - User flows yang terlink
4. **📦 Assets** - Ikon, gambar, exports

---

## Phase 2: Setup Design System (30 menit)

### Halaman: 🎨 Design System

### Langkah 2.1: Color Styles

1. **Buat frame:** "Color Palette" (1200x800px)

2. **Warna Primary** - Buat 3 rectangle (200x100px masing-masing):
   - Primary Dark: `#0A2463` → Right-click → Create color style → Nama: "Primary/Dark"
   - Primary Main: `#1E4E79` → Create style: "Primary/Main"
   - Primary Light: `#2563AB` → Create style: "Primary/Light"

3. **Warna Secondary** - Proses sama:
   - Secondary Dark: `#92400E` → "Secondary/Dark"
   - Secondary Main: `#D97706` → "Secondary/Main"
   - Secondary Light: `#F59E0B` → "Secondary/Light"

4. **Warna Status**:
   - Success: `#059669` → "Status/Success" (DIY Easy)
   - Warning: `#D97706` → "Status/Warning" (DIY Hard)
   - Error: `#DC2626` → "Status/Error" (Bengkel)
   - Info: `#2563AB` → "Status/Info"

5. **Warna Neutral**:
   - Dark: `#111827` → "Neutral/Dark"
   - Gray: `#6B7280` → "Neutral/Gray"
   - Light: `#F3F4F6` → "Neutral/Light"
   - White: `#FFFFFF` → "Neutral/White"

**Pro tip:** Group warna dengan slash notation (Primary/Dark) untuk organize styles

### Langkah 2.2: Typography Styles

1. **Buat frame:** "Typography Scale" (1200x1000px)

2. **Install Font:** Inter (Google Fonts)
   - Menu → File → Font settings → Tambah "Inter"

3. **Buat Text Styles:**

**Heading 1:**
- Buat teks: "Heading 1 - Main Page Headings"
- Font: Inter Bold
- Ukuran: 32px (2rem)
- Line height: 44.8px (140%)
- Letter spacing: -0.64px (-2%)
- Right-click → Create text style → "Heading/H1"

**Heading 2:**
- Teks: "Heading 2 - Section Headings"
- Inter Bold, 24px, line height 32px, -0.24px
- Style: "Heading/H2"

**Heading 3:**
- Teks: "Heading 3 - Card Titles"
- Inter Semibold, 20px, line height 25.6px, 0px
- Style: "Heading/H3"

**Heading 4:**
- Teks: "Heading 4 - Component Headings"
- Inter Semibold, 18px, line height 24px, 0px
- Style: "Heading/H4"

**Body:**
- Teks: "Body - Regular text untuk konten dan deskripsi"
- Inter Regular, 16px, line height 25.6px (160%), 0px
- Style: "Body/Regular"

**Small:**
- Teks: "Small - Label dan teks sekunder"
- Inter Regular, 14px, line height 19.6px, 0px
- Style: "Body/Small"

**Caption:**
- Teks: "Caption - Metadata dan caption"
- Inter Medium, 12px, line height 16px, 0.12px
- Style: "Body/Caption"

### Langkah 2.3: Sistem Spacing

1. **Buat frame:** "Spacing Grid" (800x600px)
2. Buat rectangle menunjukkan grid 8px:
   - 4px (xs)
   - 8px (sm) - unit dasar
   - 16px (md)
   - 24px (lg)
   - 32px (xl)
   - 48px (2xl)

**Pro tip:** Gunakan Auto Layout dengan spacing 8px untuk konsistensi

### Langkah 2.4: Library Komponen

#### Komponen Tombol

1. **Buat frame:** "Buttons" (1000x600px)

2. **Button - Primary:**
   - Rectangle: 120x48px
   - Background: Gradient linear 135° (#1E4E79 → #2563AB)
   - Border radius: 8px
   - Teks: "Button Text" (Inter Semibold, 16px, white)
   - Padding: 12px vertikal, 24px horizontal (Auto Layout)
   - Create Component: Cmd/Ctrl+Alt+K → Nama: "Button/Primary"

3. **Tambah Variants:**
   - Default state (dibuat)
   - Hover: Gradient sedikit lebih gelap + shadow
   - Active: Lebih gelap lagi
   - Disabled: Abu-abu + 50% opacity

4. **Button - Secondary:**
   - Ukuran sama (120x48px)
   - Background: transparan
   - Border: 2px solid Primary/Main
   - Warna teks: Primary/Main
   - Create Component: "Button/Secondary"
   - Tambah 4 variants yang sama

5. **Button - Ghost:**
   - Tanpa background, tanpa border
   - Hanya teks (warna Primary/Main)
   - Padding: 8px 16px
   - Component: "Button/Ghost"

#### Komponen Kartu

1. **Buat frame:** "Cards" (1200x800px)

2. **Base Card:**
   - Rectangle: 380x300px
   - Background: White
   - Border radius: 12px
   - Shadow: 0px 2px 8px rgba(0,0,0,0.1)
   - Auto Layout: vertikal, padding 24px
   - Create Component: "Card/Base"

3. **Card Variants:**
   - **Easy Severity:** Tambah border kiri 4px solid Success
   - **Hard Severity:** Border kiri Warning
   - **Workshop Severity:** Border kiri Error

4. **Status Card (Recent Diagnosis):**
   - Gunakan Card/Base
   - Tambah: Header (icon + judul), Area konten, Status badges
   - Component: "Card/Status"

#### Komponen Badge

1. **Buat frame:** "Badges" (800x400px)

2. **Severity Easy:**
   - Rectangle: auto width x 32px
   - Background: `#ECFDF5`
   - Border radius: 16px (bentuk pil)
   - Teks: "DIY EASY" (Inter Semibold, 14px, `#065F46`)
   - Padding: 4px 12px (Auto Layout)
   - Component: "Badge/Severity-Easy"

3. **Severity Hard:**
   - Background: `#FFFBEB`
   - Teks: "DIY HARD" (warna `#92400E`)
   - Component: "Badge/Severity-Hard"

4. **Severity Workshop:**
   - Background: `#FEF2F2`
   - Teks: "WORKSHOP REQUIRED" (warna `#991B1B`)
   - Component: "Badge/Severity-Workshop"

#### Komponen Input

1. **Text Input:**
   - Rectangle: 360x48px
   - Background: White
   - Border: 2px solid `#E5E7EB`
   - Border radius: 8px
   - Placeholder teks: Inter Regular 16px Gray
   - Component: "Input/Text"
   - Variants: Default, Focused (border Primary/Light + shadow), Error

2. **Textarea:**
   - Style sama, tinggi 150px
   - Component: "Input/Textarea"

---

## Phase 3: Desain Layar (60 menit)

### Halaman: 📱 Screens

### Langkah 3.1: Layar Dashboard

1. **Buat frame:** "Dashboard" (1920x1080px)

2. **Navigation Bar** (atas, tinggi 64px):
   - Rectangle: full width x 64px
   - Gradient background: Primary/Dark → Primary/Main (135°)
   - Teks logo: "🚗 OTOMOTIF AI" (putih, H3)
   - Search input (lebar 300px)
   - Auto Layout: horizontal, space-between

3. **Sub Navigation Menu:**
   - Di bawah navbar, background sama
   - Item: Dashboard, 3D Configurator, AI Diagnosis, Suku Cadang, Bengkel, Riwayat
   - Horizontal Auto Layout, gap 24px
   - Active state: background putih 20% opacity

4. **Dashboard Header:**
   - Padding atas: 32px
   - H1: "Dashboard"
   - Body/Small: "Selamat datang di Platform Otomotif AI"
   - Margin bottom: 32px

5. **Cards Grid:**
   - Auto Layout: horizontal wrap, 3 kolom
   - Gap: 24px
   - Kartu:
     - Recent Diagnosis (gunakan component Card/Status)
     - Quick 3D Configurator (Card/Base + 4 langkah)
     - Statistik (Card/Base + 4 metrik grid)

6. **Quick Actions:**
   - Judul section: "Quick Actions" (H2)
   - 4 action cards: Diagnosis, Suku Cadang, Bengkel, Pengaturan
   - Auto Layout: horizontal, gap 16px

**Referensi:** Lihat `design/mockups/dashboard.html` untuk visual

### Langkah 3.2: Layar 3D Configurator

1. **Buat frame:** "3D Configurator" (1920x1080px)

2. **Layout:** Horizontal Auto Layout, 2 section

3. **Kiri: Canvas Area (lebar 70%):**
   - Background: Gradient `#f5f5f5` → `#e8e8e8` (135°)
   - Placeholder: Icon besar 🎨 (tengah)
   - Toolbar (bawah tengah):
     - Frame: Auto Layout horizontal, background putih
     - Border radius: 12px
     - Shadow: 0 4px 12px rgba(0,0,0,0.15)
     - Tombol: Reset, Zoom In, Zoom Out, Rotate, Save
     - Gap: 16px, padding: 12px 24px

4. **Kanan: Component Panel (lebar 30%):**
   - **Panel Header:**
     - Background: Light
     - Padding: 24px
     - Judul: "Component Selector" (H3)
     - Border bottom: 1px Light

   - **Component Sections** (scrollable):
     - Section: Wheels 🛞
       - Collapsible header (Auto Layout)
       - Item: 2 komponen roda
       - Tiap item: nama, rentang harga, tombol Preview + Apply
     - Section: Exhaust 🔥
     - Section: Body Kit 🎨
     - Section: Suspension ⚙️

   - **Legend (bawah):**
     - Background: Light
     - 3 item legend dengan dot berwarna
     - Padding: 24px

**Referensi:** `design/mockups/3d-configurator.html`

### Langkah 3.3: Layar AI Diagnosis

1. **Buat frame:** "AI Diagnosis" (1920x1080px)

2. **Layout:** Horizontal Auto Layout, 2 kolom (1fr 2fr)

3. **Kiri: Input Panel (lebih sempit):**
   - Background card putih
   - Padding: 24px
   - Section (vertikal Auto Layout, gap 20px):
     - **Judul:** "Ceritakan Masalah Kendaraan Anda" (H3)
     - **Textarea:** Component Input/Textarea
       - Placeholder: "Contoh: Motor Vario saya..."
       - Tombol mic (bawah kanan, floating)
     - **Vehicle Selector:** Dropdown input
     - **Sample Questions:** 4 kartu pertanyaan yang bisa diklik
     - **Analyze Button:** Button/Primary full width

4. **Kanan: Result Panel (lebih lebar):**
   - Background card putih
   - Padding: 24px
   - Section (vertikal Auto Layout):
     - **Severity Badge:** Component Badge/Severity-Easy
     - **Conclusion:** H2 teks "Kerusakan terindikasi pada..."
     - **Confidence Score:** 
       - Label + progress bar (92%)
       - Bar: 100px x 8px, terisi 92%
     - **Section: Penjelasan Teknis** (H4 + body text)
     - **Section: Langkah Perbaikan:**
       - 7 item langkah (lingkaran bernomor + teks)
       - Auto Layout vertikal, gap 12px
     - **Section: Suku Cadang:**
       - 2 kartu part (icon + nama + harga + link Shopee)
       - Auto Layout, gap 16px

**Referensi:** `design/mockups/ai-diagnosis.html`

### Langkah 3.4: Layar Pencari Bengkel (Opsional)

1. **Buat frame:** "Workshop Finder" (1920x1080px)
2. **Layout:** 70% map view + 30% filter panel
3. Gunakan placeholder untuk area map
4. Panel kanan: Location search, filter (radius, rating, specialty)

### Langkah 3.5: Layar Autentikasi (Opsional)

1. **Login Frame:** 1920x1080px
   - Card terpusat: 480x600px
   - Logo, email input, password input, tombol login, tombol OAuth
2. **Register Frame:** Layout serupa, field lebih banyak
3. **Forgot Password Frame:** Disederhanakan, hanya email input

---

## Phase 4: Prototyping (20 menit)

### Halaman: 🔄 Prototypes

### Langkah 4.1: Buat Interaksi

1. **Switch ke Prototype mode** (kanan atas)

2. **Main User Flow:**
   - Login → Dashboard: Klik tombol "Login"
   - Dashboard → 3D Configurator: Klik kartu "Quick 3D Configurator"
   - Dashboard → AI Diagnosis: Klik aksi "Diagnosis Story"
   - AI Diagnosis Input → Result: Klik tombol "Analisis"

3. **Interaksi Komponen:**
   - Button hover states: On hover → Ganti ke variant hover
   - Card hover: On hover → Animasi lift (4px ke atas)
   - Section collapse: Klik header → Toggle visibility

4. **Transisi:**
   - Transisi layar: Smart Animate, 300ms, Ease Out
   - Hover effects: Instant atau 100ms

### Langkah 4.2: Buat Presentasi

1. **Set starting frame:** Dashboard
2. **Test prototype:** Klik Play (▶) button kanan atas
3. **Share:** Klik Share → Copy link → Kirim ke tim

---

## Phase 5: Dokumentasi Komponen (15 menit)

### Di Halaman Design System

1. **Untuk setiap komponen:**
   - Tambah teks deskripsi di samping komponen
   - Dokumentasikan props/variants
   - Catat pedoman penggunaan

2. **Contoh - Button/Primary:**
   ```
   Button - Primary
   
   Penggunaan: Main CTAs, form submits, aksi primer
   States: Default, Hover, Active, Disabled
   Sizes: Default (tinggi 48px), Large (56px)
   
   Props:
   - Text (string)
   - Icon (opsional)
   - Full width (boolean)
   ```

---

## Phase 6: Developer Handoff (10 menit)

### Langkah 6.1: Setup Inspect Panel

1. **Enable Dev Mode:** Switch mode (kanan atas)
2. **Cek pengukuran:** Semua spacing dalam kelipatan 8px
3. **Verifikasi kode warna:** Match design/figma-design-specification.json

### Langkah 6.2: Export Assets

1. **Ikon:**
   - Select semua ikon
   - Panel kanan → Export → SVG, 24px
   - Export ke: `exports/icons/`

2. **Komponen:**
   - Export state komponen sebagai PNG
   - Skala 2x untuk retina

3. **Design Tokens:**
   - Gunakan plugin: "Design Tokens" atau "Style Dictionary"
   - Export JSON dengan semua warna, tipografi, spacing

### Langkah 6.3: Dokumentasi

1. **Tambah README di Figma:**
   - Buat frame: "README - Developer Guide"
   - Dokumentasikan:
     - Struktur file
     - Konvensi penamaan komponen
     - Cara menggunakan design tokens
     - Link ke GitHub repo

2. **Comments:**
   - Tambah komentar untuk interaksi kompleks
   - Tag developers dengan @mentions

---

## Phase 7: Final Review (10 menit)

### Checklist

**Design System:**
- [ ] 11 color styles dibuat (Primary x3, Secondary x3, Status x4, Neutral x1)
- [ ] 7 text styles dibuat (H1-H4, Body, Small, Caption)
- [ ] Grid spacing terdokumentasi (base 8px)
- [ ] Semua komponen dibuat dengan variants

**Layar:**
- [ ] Dashboard (1920x1080) lengkap
- [ ] 3D Configurator lengkap
- [ ] AI Diagnosis lengkap
- [ ] Workshop Finder (opsional) lengkap
- [ ] Layar Auth (opsional) lengkap

**Prototyping:**
- [ ] Main user flows terlink
- [ ] Interaksi komponen berfungsi
- [ ] Transisi smooth (300ms)
- [ ] Starting frame di-set

**Developer Handoff:**
- [ ] Dev Mode enabled
- [ ] Pengukuran terverifikasi (grid 8px)
- [ ] Asset export dipersiapkan
- [ ] Dokumentasi ditambahkan

---

## Export & Share

### Langkah Final

1. **Organize Layers:**
   - Rename semua frame dengan jelas
   - Group komponen terkait
   - Lock elemen background

2. **Clean Up:**
   - Hapus komponen yang tidak dipakai
   - Merge duplicate styles
   - Update deskripsi komponen

3. **Share Link:**
   - Klik "Share" (kanan atas)
   - Set permissions: "Anyone with link can view"
   - Copy link
   - Bagikan ke tim: fajar1180, ilhamalmunawar05-cpu

4. **GitHub Integration:**
   - Tambah link Figma ke GitHub README.md
   - Update issue #14 dengan link file Figma
   - Tandai issue sebagai "Done"

---

## Troubleshooting

### Masalah Umum

**Font tidak tersedia:**
- Install font Inter dari Google Fonts
- Upload file font custom di Figma settings

**Warna tidak match:**
- Double check kode HEX di `design/figma-design-specification.json`
- Gunakan color picker untuk presisi

**Auto Layout tidak bekerja:**
- Pastikan parent frame memiliki Auto Layout enabled
- Cek direction (horizontal/vertical)
- Verifikasi nilai padding/gap

**Component variants hilang:**
- Re-create component sebagai main component
- Tambah variants via panel kanan: Component → Variants

**Export gagal:**
- Cek batas ukuran file
- Export dalam batch kecil
- Gunakan SVG untuk ikon, PNG untuk raster

---

## Referensi

### File Referensi
- `design/figma-design-specification.json` - Design tokens lengkap
- `design/mockups/dashboard.html` - Referensi visual Dashboard
- `design/mockups/3d-configurator.html` - Referensi Configurator
- `design/mockups/ai-diagnosis.html` - Referensi Diagnosis
- `docs/UI_UX_Design_Specification.md` - Dokumentasi desain lengkap

### Link
- Figma Help: https://help.figma.com
- Inter Font: https://fonts.google.com/specimen/Inter
- Design Tokens Plugin: Figma Community
- Auto Layout Guide: https://help.figma.com/hc/en-us/articles/360040451373

### Kontak Tim
- Project Manager: fajar1180 (GitHub)
- Designer: ilhamalmunawar05-cpu (GitHub)
- Repository: https://github.com/Fajar1180/Project-Otomotif-Visual3D

---

## Estimasi Waktu

- **Phase 1:** Setup (5 menit)
- **Phase 2:** Design System (30 menit)
- **Phase 3:** Layar (60 menit)
- **Phase 4:** Prototyping (20 menit)
- **Phase 5:** Dokumentasi (15 menit)
- **Phase 6:** Handoff (10 menit)
- **Phase 7:** Review (10 menit)

**Total:** ~2.5 jam untuk file Figma lengkap

---

**STATUS: SIAP UNTUK IMPLEMENTASI** ✅  
**Last Updated:** 19 Oktober 2026  
**Version:** 1.0

*Ikuti panduan ini langkah-demi-langkah untuk membuat file desain Figma production-ready*