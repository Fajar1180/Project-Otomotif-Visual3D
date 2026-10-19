# Instruksi Pembuatan File Desain Figma
## Platform Otomotif AI (Project Pak Yogi)

### Ikhtisar
Dokumen ini menyediakan instruksi komprehensif untuk membuat desain Figma untuk platform Otomotif AI, berdasarkan Spesifikasi Desain UI/UX.

### Akses yang Diperlukan
Untuk membuat file Figma ini, Anda memerlukan:
- Akun Figma dengan izin yang tepat
- Akses ke organisasi/tim proyek: **pak-yogi** (atau serupa)
- Kemampuan membuat file Figma baru di proyek

### Keterbatasan Saat Ini
Di lingkungan sandbox saat ini, pembuatan file Figma langsung terbatas karena batasan autentikasi dan akses API. Pendekatan berikut menyediakan spesifikasi desain lengkap yang dapat diimpor ke Figma.

---

### Langkah Pembuatan File Desain Figma

#### Langkah 1: Buat File Figma Baru
1. Login ke Figma dengan akun yang sesuai
2. Navigasi ke proyek/organisasi **pak-yogi**
3. Klik "New file" → "Design" (atau "FigJam" untuk prototyping)
4. Nama File: **Project_Pak_Yogi_Design**

#### Langkah 2: Setup Sistem Desain
1. **Buat Main Frame:** "Dashboard - Main View" (1920x1080px)
2. **Setup Color Styles:**
   - Primary Dark (#0A2463)
   - Primary Main (#1E4E79)
   - Primary Light (#2563AB)
   - Secondary Dark (#92400E)
   - dst.

3. **Typography Styles:** Buat text styles untuk h1-h4, body, caption
4. **Component Styles:** Buat button styles, card variants, severity badges

#### Langkah 3: Buat Layar Utama

##### 3.1 Layar Dashboard
```
Komponen:
- Top Navigation (fixed, tinggi 64px)
- Sidebar navigation (collapsed/expanded)
- Kartu Dashboard:
  • Recent Diagnosis (status card)
  • Quick 3D Configurator (CTA card)
- Quick Action Buttons
- User Profile/Logout
```

##### 3.2 Layar 3D Configurator
```
Komponen:
- 3D Canvas Area (lebar 70%)
- Right Panel (lebar 30%)
  • Component Tree (kategori collapsible)
  • Preview cards (hover effects)
  • Apply buttons
- Legend panel (bawah, indikator status)
- Toolbar (zoom, reset, save)
```

##### 3.3 Layar AI Diagnosis
```
Komponen:
- Input Section (atas)
  • Textarea dengan tombol mic
  • Tombol sample question
  • Vehicle context selector
- Result Panel (area utama)
  • Severity indicator (badge)
  • AI explanation section
  • Repair steps (collapsible list)
  • Parts recommendations (cards)
  • Workshop suggestions (list/map toggle)
```

##### 3.4 Layar Pencari Bengkel
```
Komponen:
- Map View (area utama)
- Filter Panel (sidebar kanan)
  • Location search
  • Radius selector
  • Rating filter
  • Specialty filter
- List View (toggle)
- Workshop detail panel
```

##### 3.5 Layar Autentikasi
```
Komponen:
- Login form (email/password + OAuth)
- Register form
- Forgot password
- Email verification
```

#### Langkah 4: Buat Komponen

##### 4.1 Variasi Tombol
```
.btn-primary { /* gradient style */ }
.btn-secondary { /* outline style */ }
.btn-ghost { /* text only */ }
.btn-disabled { /* disabled state */ }
```

##### 4.2 Kartu Status
```
.card { /* base style */ }
.card.severity-easy { /* green border */ }
.card.severity-hard { /* orange border */ }
.card.severity-workshop { /* red border */ }
.card.hover { /* lift effect */ }
```

##### 4.3 Indikator Tingkat Keparahan
```
.badge {
  .severity-easy { background: #ECFDF5, color: #065F46 }
  .severity-hard { background: #FFFBEB, color: #92400E }
  .severity-workshop { background: #FEF2F2, color: #991B1B }
}
```

##### 4.4 Elemen Form
```
.input-group {
  .label { /* label style */ }
  .input-field { /* input style */ }
  .error-message { /* error style */ }
}
```

#### Langkah 5: Buat Design Tokens

##### 5.1 Color Tokens
```json
{
  "colors": {
    "primary": {
      "dark": "#0A2463",
      "main": "#1E4E79", 
      "light": "#2563AB"
    },
    "secondary": {
      "dark": "#92400E",
      "main": "#D97706",
      "light": "#F59E0B"
    }
  }
}
```

##### 5.2 Typography Tokens
```json
{
  "typography": {
    "h1": { "fontFamily": "Inter", "fontWeight": "Bold", "fontSize": "2.5rem", "lineHeight": "3.2rem" },
    "h2": { "fontFamily": "Inter", "fontWeight": "Bold", "fontSize": "2rem", "lineHeight": "2.8rem" },
    "body": { "fontFamily": "Inter", "fontWeight": "Regular", "fontSize": "1rem", "lineHeight": "1.6rem" }
  }
}
```

#### Langkah 6: Setup Prototypes
```
- Buat clickable hotspots pada komponen 3D configurator
- Link layar untuk main user flows:
  • Dashboard → 3D Configurator → Diagnosis → Bengkel
  • Login → Dashboard
  • Diagnosis → Results → Parts/Bengkel
- Buat transisi dengan easing yang tepat
```

#### Langkah 7: Dokumentasi dan Setup Sistem

##### 7.1 Dokumentasi Komponen
Untuk setiap komponen, dokumentasikan:
- Props/States
- Pola interaksi
- Catatan aksesibilitas
- Variasi
- Pedoman penggunaan

##### 7.2 Dokumentasi Sistem Desain
```
Dokumentasi harus mencakup:
- Penggunaan palette warna
- Skala tipografi
- Sistem spacing (grid 8px)
- Layer shadow
- Sistem border radius
- Skala Z-index
```

---

### Alternatif: Pembuatan Figma Manual

Jika pembuatan tool langsung tidak mungkin, Anda bisa:

1. **Import dari Kode:** Ekspor CSS dari spesifikasi ini sebagai:
   - Kode komponen di Figma
   - Dokumentasi di Figma Comments
   - Design tokens sebagai Figma variables

2. **Setup Manual:**
   - Buat frame sesuai dimensi yang dispesifikasikan
   - Terapkan warna, tipografi, spacing seperti yang dispesifikasikan
   - Bangun komponen menggunakan struktur CSS yang disediakan sebagai referensi

3. **Kolaborasi dengan Tim Desain:**
   - Bagikan spesifikasi ini ke tim desain
   - Berikan spec komponen dan design tokens yang jelas
   - Gunakan sebagai base untuk iterasi desain final

---

### Rekomendasi Export/Import

#### Langkah 8: Export Design Assets
```
- Export SVG icons (semua variasi 24px)
- Export component states (hover, active, disabled)
- Export dark theme variants (untuk implementasi developer)
- Export design tokens sebagai JSON/CSS custom properties
```

#### Langkah 9: Developer Handoff
```
- Buat figma-plugin.json dengan component props
- Ekspor spesifikasi komponen ke developer portal
- Buat prototype interaktif untuk feedback
- Setup design review comments
```

---

### Ringkasan Kemajuan Proyek

#### Dokumen yang Dibuat (✅)
1. **PRD (Dokumen Kebutuhan Proyek)**
2. **SRS (Spesifikasi Kebutuhan Perangkat Lunak)** 
3. **ERD (Diagram Relasi Entitas)**
4. **Spesifikasi API**
5. **Spesifikasi Desain UI/UX**

#### Sedang Berlangsung
- [x] Deliverable dokumentasi
- [x] Spesifikasi desain
- [ ] Pembuatan file desain Figma (memerlukan setup manual)

#### Langkah Selanjutnya
1. **Pembuatan File Figma Manual:** Karena keterbatasan sandbox, file desain Figma perlu dibuat manual menggunakan spesifikasi yang disediakan
2. **Implementasi Komponen:** Bangun semua komponen UI mengikuti sistem desain
3. **Design Handoff:** Ekspor spesifikasi ke tim development
4. **Review dan Iterasi:** Kumpulkan feedback dan perbaiki desain

---

### Catatan Implementasi

#### Keputusan Desain Kritis
- **Psikologi Warna:** Tone biru untuk kepercayaan/keandalan teknis, orange untuk aksi/energi, hijau untuk sukses
- **Tipografi:** Font Inter untuk tampilan modern, bersih
- **Sistem Grid:** Spacing 8px untuk konsistensi
- **Integrasi 3D:** Prioritas untuk kanvas 3D dengan UI overlay minimal

#### Pertimbangan Responsif
- Pendekatan mobile-first dengan progressive enhancement
- Touch target minimum 44px
- Dioptimalkan untuk lebar 320px+

#### Prioritas Aksesibilitas
- Kompliance WCAG AA diperlukan
- Rasio kontras warna yang memadai
- Ramah screen reader
- Dukungan navigasi keyboard

---
*Versi Dokumen 1.0 | Dibuat: 19 Oktober 2026*

### Informasi Kontak
Untuk bantuan pembuatan file Figma:
- Proyek: Platform Otomotif AI (Project Pak Yogi)
- Tim: fajar1180 (Project Manager), ilhamalmunawar05-cpu (Koordinasi Desain)
- Repositori: /c/laragon/www/Project-Otomotif-Visual3D/