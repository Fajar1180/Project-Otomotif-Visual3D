# UI/UX Design Specification
## Platform Otomotif AI (Project Pak Yogi)

### 1. Design Overview
**Target Users:**
- DIY motorcycle enthusiasts
- Vehicle owners seeking self-repair solutions
- Mechanics looking for diagnostic reference
- Workshop owners seeking customer acquisition

**Primary Goals:**
1. Provide intuitive, interactive vehicle diagnosis
2. Enable easy 3D component visualization and modification
3. Deliver actionable repair instructions with spare parts integration
4. Connect users with local workshop services when needed

---

### 2. Design System

#### 2.1 Color Palette
```css
/* Primary Colors */
- primary-dark: #0A2463 (navy blue)
- primary-main: #1E4E79 (deep blue)
- primary-light: #2563AB (bright blue)

/* Secondary Colors */
- secondary-dark: #92400E (brown)
- secondary-main: #D97706 (orange)
- secondary-light: #F59E0B (amber)

/* Status Colors */
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

#### 2.2 Typography
```css
/* Headings */
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

#### 2.3 Iconography
- 24px outline icons for interactions
- 20px filled icons for status indicators
- Custom 3D-styled icons for vehicle components
- Material Design Icons set for consistency

---

### 3. Layout Structure

#### 3.1 Main Navigation
```
┌─────────────────────────────────────────────────────┐
│ Logo [OTOMOTIF AI] │ Search [Vehicle/File] │     │
│                                                   │
│ [Dashboard] │ [3D Configurator] │ [AI Diagnosis] │
│ [Spare Parts] │ [Workshops] │ [History] │
└─────────────────────────────────────────────────────┘
```

- Fixed top navigation with brand and search
- Secondary navigation with 6 main sections
- Dark theme with gradient effect
- Shadow for depth

#### 3.2 Dashboard Layout
```
┌─────────────────────────────────────────────────────┐
│              Dashboard                               │
│                                                   │
│ [Recent Diagnosis] │ [Quick 3D Config] │         │
│  ┌─────┐  ┌──────────┐                           │
│  │ •  │  │  Generate │  (4-step process)        │
│  │ 1  │  │  3D Mesh  │                           │
│  │2&3 │  └──────────┘                           │
│  │DIY  │                                          │
│  └─────┘                                          │
│                                                   │
│ Quick Actions:                                     │
│ • Diagnosis Story               • Spare Parts      │
│ • Workshop Locator             • Profile Settings │
└─────────────────────────────────────────────────────┘
```

#### 3.3 3D Configurator Layout
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
│   │ │                    │ │                 │
│   │ │                      │ │                 │
│   │ └─────────────────────┘ │                 │
│                                                   │
│   ┌─────────────────────┐ │                 │
│   │ Legend              │ │                 │
│   │ • Connected       │ │                 │
│   │ • Requires Skill │ │                 │
│   │ • Affiliate      │ │                 │
│   └─────────────────────┘ │                 │
└─────────────────────────────────────────────────────┘
```

#### 3.4 AI Diagnosis Layout
```
┌─────────────────────────────────────────────────────┐
│                AI Diagnosis Interface               │
│                                                   │
│ ┌─────────────────────┐ ┌───────────────────────┐ │
│ │ Input Area          │ │ Result Panel          │ │
│ │                     │ │                       │ │
│ │ Textbox with mic    │ │ ┌─────────────────────┐ │ │
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

### 4. Component Library

#### 4.1 Buttons
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

#### 4.2 Cards
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

#### 4.3 Forms & Inputs
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

### 5. Interactive Elements

#### 5.1 3D Canvas Interactions
- **Hover States:** Highlight interactable parts
- **Drag & Drop:** Component rearrangement in configurator
- **Mouse Wheel:** Zoom in/out on 3D model
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

#### 5.3 Notifications
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

### 6. Color System for Diagnosis Severity

| Severity | Color | Light Shade | Text on Background |
|----------|-------|-------------|-------------------|
| DIY Easy | #10B981 | #ECFDF5 | #065F46 |
| DIY Hard | #F59E0B | #FFFBEB | #92400E |
| Workshop | #EF4444 | #FEF2F2 | #991B1B |

---

### 7. Responsive Design

#### Mobile (< 768px)
```
- Navigation: Collapsible hamburger menu
- 3D Canvas: Full-width, reduced quality settings
- Panel Width: 280px max (drawer)
- Font Size: Body 0.875rem, Headings scale down
```

#### Tablet (768px - 1024px)
```
- Navigation: Full width with icons
- 3D Canvas: Fixed height, side panel
- Panel Width: 320px
- Font Size: Body 1rem
```

#### Desktop (> 1024px)
```
- Navigation: Fixed top with secondary sidebar
- 3D Canvas: Left/main area with right panel
- Panel Width: 360px
- Font Size: Body 1.125rem
```

---

### 8. Typography & Accessibility

#### 8.1 Text Hierarchy
```
Level 1 (H1)  : 2.5rem / 32px - Page titles
Level 2 (H2)  : 2rem / 28px - Section titles
Level 3 (H3)  : 1.5rem / 24px - Subsection titles
Level 4 (H4)  : 1.25rem / 20px - Component titles
Level 5 (H5)  : 1.125rem / 18px - Card titles
Body Large   : 1.125rem / 18px - Primary text
Body          : 1rem / 16px - Secondary text
Body Small    : 0.875rem / 14px - Captions, labels
```

#### 8.2 Contrast Ratios
- All text must meet WCAG AA standard (4.5:1 for normal text, 3:1 for large text)
- Use color combinations that pass accessibility tests
- Include focus indicators for keyboard navigation
- Provide alternative text for all images

---

### 9. Animation & Motion

#### 9.1 Easing Functions
- **Ease Out:** For element expansion, dialog opening
- **Ease In:** For element collapsing
- **Linear:** For loading spinners

#### 9.2 Duration
- **Fast:** 150ms - Quick interactions
- **Normal:** 300ms - Standard animations
- **Slow:** 500ms - Complex transitions

---

### 10. Component States

#### 10.1 Interactive Components
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

#### 10.2 Diagnosis Card States
```
Default: Clean white card with severity color left border
Hover: Lift effect, shadow enhancement
Selected: Highlighted background, border accent
Loading: Skeleton placeholders with shimmer effect
```

---

### 11. i18n Support

#### 11.1 Language Structure
```
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

### 12. Local Storage Structure
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
*Document Version 1.0 | Created: 2026-10-19*
