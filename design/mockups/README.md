# Design Mockups - Project Otomotif AI (Project Pak Yogi)

## Ikhtisar
Folder ini berisi HTML mockups untuk semua layar utama dari Platform Otomotif AI. Mockups ini dibuat berdasarkan spesifikasi lengkap di `docs/UI_UX_Design_Specification.md`.

## Files

### 1. dashboard.html
**Layar Dashboard** - Halaman utama aplikasi
- Recent diagnosis dengan status badges
- Quick 3D configurator dengan proses 4-langkah
- Statistics cards (diagnosis, konfigurasi, parts, bengkel)
- Quick actions shortcuts

**Preview:** Buka file di browser untuk melihat design

### 2. 3d-configurator.html
**Layar 3D Configurator** - Interface untuk modifikasi 3D kendaraan
- Canvas area untuk 3D viewport (lebar 70%)
- Right panel dengan component selector (lebar 30%)
- Kategori komponen: Wheels, Exhaust, Body Kit, Suspension
- Preview & Apply buttons untuk setiap part
- Toolbar: Reset, Zoom In/Out, Rotate, Save
- Legend panel dengan status indicators

**Preview:** Buka file di browser untuk melihat design

### 3. ai-diagnosis.html
**Layar AI Diagnosis** - Interface untuk diagnosis AI
- Input panel (sisi kiri):
  - Textarea dengan tombol mic untuk voice input
  - Vehicle selector dropdown
  - Sample questions untuk quick start
  - Analyze button
- Result panel (sisi kanan):
  - Severity badge (DIY Easy/Hard/Workshop Required)
  - Confidence score dengan visual bar
  - Penjelasan teknis
  - Instruksi perbaikan langkah-demi-langkah
  - Suku cadang yang direkomendasikan dengan link affiliate Shopee
  - Saran bengkel (untuk severity = WORKSHOP_REQUIRED)

**Preview:** Buka file di browser untuk melihat design

## Sistem Desain

### Palette Warna
```css
Primary Colors:
- primary-dark: #0A2463
- primary-main: #1E4E79
- primary-light: #2563AB

Secondary Colors:
- secondary-dark: #92400E
- secondary-main: #D97706
- secondary-light: #F59E0B

Status Colors:
- success: #059669 (DIY Easy)
- warning: #D97706 (DIY Hard)
- error: #DC2626 (Workshop Required)

Neutral:
- dark: #111827
- gray: #6B7280
- light: #F3F4F6
- white: #FFFFFF
```

### Tipografi
- **Font Family:** Inter (system fallback: -apple-system, BlinkMacSystemFont, 'Segoe UI')
- **Heading 1:** Bold, 2rem
- **Heading 2:** Bold, 1.5rem
- **Body:** Regular, 1rem
- **Small:** Regular, 0.875rem

### Komponen
- **Buttons:** 8px border-radius, gradient background untuk primary
- **Cards:** 12px border-radius, box-shadow untuk depth
- **Badges:** 16px border-radius untuk status pills
- **Inputs:** 8px border-radius, 2px border

## Cara Menggunakan

### 1. Preview Mockups
```bash
# Buka salah satu file di browser
cd design-mockups
start dashboard.html          # Windows
open dashboard.html           # macOS
xdg-open dashboard.html       # Linux
```

### 2. Import ke Figma
Mockups ini bisa di-screenshot dan digunakan sebagai referensi di Figma, atau:
1. Buka Figma
2. Buat file Design baru
3. Screenshot mockups atau copy CSS styles
4. Rebuild komponen di Figma dengan design tokens yang sama

### 3. Export untuk Development
CSS variables sudah didefinisikan di `:root` setiap file, bisa langsung di-copy ke production CSS.

## Desain Responsif
Semua mockups sudah responsif dengan breakpoints:
- **Desktop:** > 1200px (grid layout penuh)
- **Tablet:** 768px - 1200px (kolom disesuaikan)
- **Mobile:** < 768px (single column, stacked layout)

## Next Steps

### Untuk Designers
1. Screenshot mockups sebagai referensi
2. Buat Figma file baru: "Project_Pak_Yogi_Design"
3. Setup design tokens dari CSS variables
4. Rebuild komponen dengan variants
5. Buat prototypes dengan interaksi

### Untuk Developers
1. Review mockups untuk memahami struktur layout
2. Ekstrak CSS variables untuk production
3. Implement komponen dengan framework pilihan (Next.js + Tailwind)
4. Integrate dengan backend API

## Layar Tambahan (Akan Dibuat)
- [ ] Workshop Finder (map + list view)
- [ ] Authentication (login/register)
- [ ] User Profile/Settings
- [ ] Spare Parts Catalog
- [ ] History/Dashboard Analytics

## Catatan
- Mockups ini adalah **high-fidelity prototypes** dengan real CSS styling
- Semua warna, tipografi, spacing mengikuti spesifikasi di `docs/UI_UX_Design_Specification.md`
- Ikon menggunakan emoji untuk simplicity (production bisa gunakan Material Icons atau custom SVG)
- 3D canvas menggunakan placeholder (production akan integrate React Three Fiber)

---
*Dibuat: 19 Oktober 2026*  
*Berdasarkan: UI_UX_Design_Specification.md*  
*Proyek: Platform Otomotif AI (Project Pak Yogi)*