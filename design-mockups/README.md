# Design Mockups - Project Otomotif AI (Project Pak Yogi)

## Overview
Folder ini berisi HTML mockups untuk semua screen utama dari Platform Otomotif AI. Mockups ini dibuat berdasarkan spesifikasi lengkap di `UI_UX_Design_Specification.md`.

## Files

### 1. dashboard.html
**Dashboard Screen** - Halaman utama aplikasi
- Recent diagnosis dengan status badges
- Quick 3D configurator dengan 4-step process
- Statistics cards (diagnosis, konfigurasi, parts, bengkel)
- Quick actions shortcuts

**Preview:** Buka file di browser untuk melihat design

### 2. 3d-configurator.html
**3D Configurator Screen** - Interface untuk modifikasi 3D kendaraan
- Canvas area untuk 3D viewport (70% width)
- Right panel dengan component selector (30% width)
- Component categories: Wheels, Exhaust, Body Kit, Suspension
- Preview & Apply buttons untuk setiap part
- Toolbar: Reset, Zoom In/Out, Rotate, Save
- Legend panel dengan status indicators

**Preview:** Buka file di browser untuk melihat design

### 3. ai-diagnosis.html
**AI Diagnosis Screen** - Interface untuk diagnosis AI
- Input panel (left side):
  - Textarea dengan mic button untuk voice input
  - Vehicle selector dropdown
  - Sample questions untuk quick start
  - Analyze button
- Result panel (right side):
  - Severity badge (DIY Easy/Hard/Workshop Required)
  - Confidence score dengan visual bar
  - Technical explanation
  - Step-by-step repair instructions
  - Recommended spare parts dengan Shopee affiliate links
  - Workshop suggestions (untuk severity = WORKSHOP_REQUIRED)

**Preview:** Buka file di browser untuk melihat design

## Design System

### Color Palette
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

### Typography
- **Font Family:** Inter (system fallback: -apple-system, BlinkMacSystemFont, 'Segoe UI')
- **Heading 1:** Bold, 2rem
- **Heading 2:** Bold, 1.5rem
- **Body:** Regular, 1rem
- **Small:** Regular, 0.875rem

### Components
- **Buttons:** 8px border-radius, gradient background untuk primary
- **Cards:** 12px border-radius, box-shadow untuk depth
- **Badges:** 16px border-radius untuk status pills
- **Inputs:** 8px border-radius, 2px border

## How to Use

### 1. Preview Mockups
```bash
# Buka salah satu file di browser
cd design-mockups
start dashboard.html          # Windows
open dashboard.html           # macOS
xdg-open dashboard.html       # Linux
```

### 2. Import to Figma
Mockups ini bisa di-screenshot dan digunakan sebagai reference di Figma, atau:
1. Buka Figma
2. Create new Design file
3. Screenshot mockups atau copy CSS styles
4. Rebuild components di Figma dengan design tokens yang sama

### 3. Export for Development
CSS variables sudah didefinisikan di `:root` setiap file, bisa langsung di-copy ke production CSS.

## Responsive Design
Semua mockups sudah responsive dengan breakpoints:
- **Desktop:** > 1200px (grid layout penuh)
- **Tablet:** 768px - 1200px (adjusted columns)
- **Mobile:** < 768px (single column, stacked layout)

## Next Steps

### For Designers
1. Screenshot mockups sebagai reference
2. Buat Figma file baru: "Project_Pak_Yogi_Design"
3. Setup design tokens dari CSS variables
4. Rebuild components dengan variants
5. Create prototypes dengan interactions

### For Developers
1. Review mockups untuk understand layout structure
2. Extract CSS variables untuk production
3. Implement components dengan framework pilihan (Next.js + Tailwind)
4. Integrate dengan backend API

## Additional Screens (To Be Created)
- [ ] Workshop Finder (map + list view)
- [ ] Authentication (login/register)
- [ ] User Profile/Settings
- [ ] Spare Parts Catalog
- [ ] History/Dashboard Analytics

## Notes
- Mockups ini adalah **high-fidelity prototypes** dengan real CSS styling
- Semua colors, typography, spacing mengikuti spesifikasi di `UI_UX_Design_Specification.md`
- Icons menggunakan emoji untuk simplicity (production bisa gunakan Material Icons atau custom SVG)
- 3D canvas menggunakan placeholder (production akan integrate React Three Fiber)

---
*Created: 2026-10-19*  
*Based on: UI_UX_Design_Specification.md*  
*Project: Platform Otomotif AI (Project Pak Yogi)*