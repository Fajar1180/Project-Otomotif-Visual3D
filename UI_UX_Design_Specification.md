# Spesifikasi Desain UI/UX
## Platform Otomotif AI (Project Pak Yogi)

### 1. Ikhtisar Desain
**Target Pengguna:**
- Penggemar DIY motor
- Pemilik kendaraan mencari solusi perbaikan mandiri
- Mekanik mencari referensi diagnosis
- Pemilik bengkel mencari akuisisi pelanggan

**Tujuan Utama:**
1. Menyediakan diagnosis kendaraan intuitif dan interaktif
2. Memungkinkan visualisasi dan modifikasi komponen 3D dengan mudah
3. Menyediakan instruksi perbaikan actionable dengan integrasi suku cadang
4. Menghubungkan pengguna dengan layanan bengkel lokal saat dibutuhkan

---

### 2. Sistem Desain

#### 2.1 Palette Warna
```css
/* Warna Primary */
- primary-dark: #0A2463 (navy blue)
- primary-main: #1E4E79 (deep blue)
- primary-light: #2563AB (bright blue)

/* Warna Secondary */
- secondary-dark: #92400E (brown)
- secondary-main: #D97706 (orange)
- secondary-light: #F59E0B (amber)

/* Warna Status */
- success: #059669 (green)
- warning: #D97706 (orange)
- error: #DC2626 (red)
- info: #2563AB (blue)

/* Neutral */
- dark: #111827 (near black)
- dark-2: #1F2937 (dark gray)
- gray: #6B7280 (gray)
- light: #F3F4F6 (light gray)
- white: #FFFFFF
```

#### 2.2 Tipografi
```css
/* Heading */
- h1: Inter Bold, 2.5rem (desktop), 2rem (mobile), 32px-40px line-height
- h2: Inter Bold, 2rem (desktop), 1.75rem (mobile), 28px-36px
- h3: Inter SemiBold, 1.5rem, 24-32px
- h4: Inter SemiBold, 1.25rem, 20-28px

/* Body Text */
- body-large: Inter Regular, 1.125rem, 18-22px
- body: Inter Regular, 1rem, 16-20px
- body-small: Inter Regular, 0.875rem, 14-18px

/* Special */
- code: Fira Code, monospace
```

#### 2.3 Ikonografi
- Ikon outline 24px untuk interaksi
- Ikon filled 20px untuk indikator status
- Ikon custom 3D-styled untuk komponen kendaraan
- Set Material Design Icons untuk konsistensi

---

### 3. Struktur Layout

#### 3.1 Navigasi Utama
```
┌─────────────────────────────────────────────────────┐
│ Logo [OTOMOTIF AI] │ Search [Kendaraan/File] │     │
│                                                   │
│ [Dashboard] │ [3D Configurator] │ [AI Diagnosis] │
│ [Suku Cadang] │ [Bengkel] │ [Riwayat] │
└─────────────────────────────────────────────────────┘
```

- Navigasi atas fixed dengan brand dan search
- Navigasi sekunder dengan 6 section utama
- Tema gelap dengan efek gradient
- Shadow untuk kedalaman

#### 3.2 Layout Dashboard
```
┌─────────────────────────────────────────────────────┐
│              Dashboard                               │
│                                                   │
│ [Recent Diagnosis] │ [Quick 3D Config] │         │
│  ┌─────┐  ┌──────────┐                           │
│  │ •  │  │  Generate │  (proses 4-langkah)       │
│  │ 1  │  │  3D Mesh  │                           │
│  │2&3 │  └──────────┘                           │
│  │DIY  │                                          │
│  └─────┘                                          │
│                                                   │
│ Quick Actions:                                     │
│ • Diagnosis Story               • Suku Cadang      │
│ • Pencari Bengkel             • Pengaturan Profil │
└─────────────────────────────────────────────────────┘
```

#### 3.3 Layout 3D Configurator
```
┌─────────────────────────────────────────────────────┐
│              3D Vehicle Configurator                │
│                                                   │
│                  ┌───────────────┐                 │
│                  │   Canvas      │                 │
│                  │   (Main      │                 │
│                  │   Viewport)  │                 │
│                  │              │                 │
│   ┌─────────────┴─────────────┐ │                 │
│   │ Panel Right            │ │                 │
│   │                        │ │                 │
│   │ ┌─────────────────────┐ │ │                 │
│   │ │ Component Tree      │ │ │                 │
│   │ │                    │ │ │                 │
│   │ │ • Category 1       │ │ │                 │
│   │ │   ├── Subcategory 1 │ │ │                 │
│   │ │   │ • Item A       │ │ │                 │
│   │ │   │   ├── Preview  │ │ │                 │
│   │ │   │   └── Apply    │ │ │                 │
│   │ │   └── ...          │ │ │                 │
│   │ │ • Category 2       │ │ │                 │
│   │ │                    │ │ │                 │
│   │ │                      │ │                 │
│   │ └─────────────────────┘ │                 │
│                                                   │
│   ┌─────────────────────┐ │                 │
│   │ Legend              │ │                 │
│   │ • Connected       │ │                 │
│   │ • Butuh Skill     │ │                 │
│   │ • Affiliate       │ │                 │
│   └─────────────────────┘ │                 │
└─────────────────────────────────────────────────────┘
```

#### 3.4 Layout AI Diagnosis
```
┌─────────────────────────────────────────────────────┐
│                AI Diagnosis Interface               │
│                                                   │
│ ┌─────────────────────┐ ┌───────────────────────┐ │
│ │ Input Area          │ │ Result Panel          │ │
│ │                     │ │                       │ │
│ │ Textbox dengan mic  │ │ ┌─────────────────────┐ │ │
│ │ icon                │ │ │ Severity:           │ │ │
│ │ • Story Input       │ │ │                      │ │ │
│ │ • Sample Questions  │ │ │ 💚 DIY EASY          │ │ │
│ │ • Vehicle Context   │ │ │ 🌠 DIY HARD          │ │ │
│ │                     │ │ │ 🔧 WORKSHOP REQUIRED │ │ │
│ │ ┌─────────────────┐ │ │ ┌─────────────────────┐ │ │
│ │ │ AI Avatar       │ │ │ │ Technical           │ │ │
│ │ │ (Chat Interface)│ │ │ │ Explanation         │ │ │
│ │ └─────────────────┘ │ │ │                    │ │ │
│ │                     │ │ │ ┌─────────────────┐ │ │ │
│ │                     │ │ │ │ Repair Steps    │ │ │ │
│ │                     │ │ │ │                  │ │ │ │
│ │                     │ │ │ │ • Step 1          │ │ │ │
│ │                     │ │ │ │ • Step 2          │ │ │ │
│ │                     │ │ │ │                  │ │ │ │
│ │                     │ │ │ │ ┌───────────────┐ │ │ │
│ │                     │ │ │ │ Parts List     │ │ │ │
│ │                     │ │ │ │ • Primary      │ │ │ │
│ │                     │ │ │ │ • Secondary    │ │ │ │
│ │                     │ │ │ └───────────────┘ │ │ │
│ └─────────────────────┘ │ └───────────────────────┘ │
│                                                   │
│                              ┌─────────────────────┐ │
│                              │ Footer/Affiliate    │ │
│                              │ Integration         │ │
│                              └─────────────────────┘ │
└─────────────────────────────────────────────────────┘
```

---

### 4. Perpustakaan Komponen

#### 4.1 Tombol
```css
/* Primary Action */
.btn-primary {
  background: linear-gradient(135deg, #1E4E79, #2563AB);
  color: white;
  padding: 12px 24px;
  border-radius: 8px;
  border: none;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(30, 78, 121, 0.4);
}

/* Secondary Action */
.btn-secondary {
  background: transparent;
  color: #1E4E79;
  border: 2px solid #1E4E79;
  padding: 10px 22px;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
}

/* Ghost */
.btn-ghost {
  background: transparent;
  color: #6B7280;
  padding: 8px 16px;
  border-radius: 6px;
  border: none;
  cursor: pointer;
}
```

#### 4.2 Kartu
```css
.card {
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  padding: 20px;
  transition: all 0.3s ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 24px rgba(0,0,0,0.15);
}

card.severity-easy {
  border-left: 4px solid #10B981;
}

card.severity-hard {
  border-left: 4px solid #F59E0B;
}

card.severity-workshop {
  border-left: 4px solid #EF4444;
}
```

#### 4.3 Form & Input
```css
.input-group {
  margin-bottom: 20px;
}

.input-label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
  color: #1F2937;
}

.input-field {
  width: 100%;
  padding: 12px 16px;
  border: 2px solid #E5E7EB;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.3s ease;
}

.input-field:focus {
  outline: none;
  border-color: #2563AB;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.textarea {
  min-height: 120px;
  resize: vertical;
}
```

---

### 5. Elemen Interaktif

#### 5.1 Interaksi Kanvas 3D
- **Hover States:** Highlight bagian yang bisa diinteraksi
- **Drag & Drop:** Penyusunan komponen di konfigurator
- **Mouse Wheel:** Zoom in/out pada model 3D
- **Touch Gestures:** Pinch to zoom, swipe to rotate (mobile)

#### 5.2 Loading States
```css
.spinner {
  border: 3px solid rgba(0,0,0,0.1);
  border-radius: 50%;
  border-top-color: #2563AB;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

#### 5.3 Notifikasi
```css
.notification {
  position: fixed;
  top: 20px;
  right: 20px;
  padding: 16px 24px;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  z-index: 1000;
  animation: slideIn 0.3s ease;
}

.notification.success {
  background: #ECFDF5;
  color: #065F46;
  border-left: 4px solid #10B981;
}

@keyframes slideIn {
  from { transform: translateX(100%); }
  to { transform: translateX(0); }
}
```

---

### 6. Sistem Warna untuk Tingkat Keparahan Diagnosis

| Tingkat Keparahan | Warna | Light Shade | Teks pada Background |
|----------|-------|-------------|-------------------|
| DIY Easy | #10B981 | #ECFDF5 | #065F46 |
| DIY Hard | #F59E0B | #FFFBEB | #92400E |
| Workshop | #EF4444 | #FEF2F2 | #991B1B |

---

### 7. Desain Responsif

#### Mobile (< 768px)
```
- Navigasi: Collapsible hamburger menu
- 3D Canvas: Full-width, pengaturan kualitas reduced
- Panel Width: 280px max (drawer)
- Font Size: Body 0.875rem, Headings scale down
```

#### Tablet (768px - 1024px)
```
- Navigasi: Full width dengan ikon
- 3D Canvas: Fixed height, side panel
- Panel Width: 320px
- Font Size: Body 1rem
```

#### Desktop (> 1024px)
```
- Navigasi: Fixed top dengan sidebar sekunder
- 3D Canvas: Area kiri/utama dengan panel kanan
- Panel Width: 360px
- Font Size: Body 1.125rem
```

---

### 8. Tipografi & Aksesibilitas

#### 8.1 Hierarki Teks
```
Level 1 (H1)  : 2.5rem / 32px - Judul halaman
Level 2 (H2)  : 2rem / 28px - Judul section
Level 3 (H3)  : 1.5rem / 24px - Judul subsection
Level 4 (H4)  : 1.25rem / 20px - Judul komponen
Level 5 (H5)  : 1.125rem / 18px - Judul kartu
Body Large   : 1.125rem / 18px - Teks primer
Body          : 1rem / 16px - Teks sekunder
Body Small    : 0.875rem / 14px - Caption, label
```

#### 8.2 Rasio Kontras
- Semua teks harus memenuhi standar WCAG AA (4.5:1 untuk teks normal, 3:1 untuk teks besar)
- Gunakan kombinasi warna yang lolos tes aksesibilitas
- Sertakan indikator fokus untuk navigasi keyboard
- Sediakan teks alternatif untuk semua gambar

---

### 9. Animasi & Motion

#### 9.1 Fungsi Easing
- **Ease Out:** Untuk ekspansi elemen, pembukaan dialog
- **Ease In:** Untuk kollaps elemen
- **Linear:** Untuk loading spinner

#### 9.2 Durasi
- **Cepat:** 150ms - Interaksi cepat
- **Normal:** 300ms - Animasi standar
- **Lambat:** 500ms - Transisi kompleks

---

### 10. State Komponen

#### 10.1 Komponen Interaktif
```
Default State:
  Background: white
  Border: #E5E7EB
  Color: #374151

Hover State:
  Background: #F9FAFB
  Border: #D1D5DB
  Color: #1E4E79

Active/Pressed:
  Background: #E5E7EB
  Border: #1E4E79
  Color: #0A2463

Disabled:
  Background: #F3F4F6
  Border: #E5E7EB
  Color: #9CA3AF
  Cursor: not-allowed
```

#### 10.2 State Kartu Diagnosis
```
Default: Kartu putih bersih dengan border warna severity di kiri
Hover: Efek lift, peningkatan shadow
Selected: Background highlighted, border accent
Loading: Skeleton placeholders dengan efek shimmer
```

---

### 11. Dukungan i18n

#### 11.1 Struktur Bahasa
```json
{
  "en": {
    "diagnosis": "Diagnosis",
    "severity": "Severity",
    "repair": "Repair",
    "parts": "Parts",
    "workshops": "Workshops",
    "configure": "Configure",
    "analyze": "Analyze",
    "save": "Save",
    "cancel": "Cancel"
  },
  "id": {
    "diagnosis": "Diagnosis",
    "severity": "Keparahan",
    "repair": "Perbaikan",
    "parts": "Suku Cadang",
    "workshops": "Bengkel",
    "configure": "Konfigurasi",
    "analyze": "Analisis",
    "save": "Simpan",
    "cancel": "Batal"
  }
}
```

---

### 12. Struktur Local Storage
```javascript
{
  "user": {
    "profile": { "name": "", "vehicle": "", "preferences": {} }
  },
  "cache": {
    "diagnoses": [],
    "configurations": [],
    "workshop_searches": []
  },
  "offline": {
    "last_sync": null,
    "pending_actions": []
  }
}
```

---
*Versi Dokumen 1.0 | Dibuat: 19 Oktober 2026*
