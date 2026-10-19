# Manual Figma File Creation Guide
## Platform Otomotif AI - Project Pak Yogi

**Target:** Create complete Figma design file with design system, components, and screens  
**Account:** pak-yogi organization (atau personal account)  
**File Name:** Project_Pak_Yogi_Design  
**Date:** 19 Oktober 2026

---

## Prerequisites

### 1. Setup Figma Account
- [ ] Buat/login Figma account di https://figma.com
- [ ] Install Figma desktop app (recommended) atau gunakan web version
- [ ] Join team/organization "pak-yogi" (jika ada)

### 2. Preparation Materials
- [ ] `figma-design-specification.json` - Design tokens dan component specs
- [ ] `design-mockups/` folder - HTML mockups sebagai visual reference
- [ ] `UI_UX_Design_Specification.md` - Complete design documentation

---

## Phase 1: Create New Figma File (5 menit)

### Step 1.1: Create File
1. Open Figma
2. Click **"New design file"** 
3. Rename file: **Project_Pak_Yogi_Design**
4. Save to team "pak-yogi" (atau Drafts)

### Step 1.2: Setup Pages
Create 4 pages (left sidebar):
1. **🎨 Design System** - Colors, typography, components
2. **📱 Screens** - All main screens
3. **🔄 Prototypes** - Linked user flows
4. **📦 Assets** - Icons, images, exports

---

## Phase 2: Design System Setup (30 menit)

### Page: 🎨 Design System

### Step 2.1: Color Styles

1. **Create frame:** "Color Palette" (1200x800px)

2. **Primary Colors** - Create 3 rectangles (200x100px each):
   - Primary Dark: `#0A2463` → Right-click → Create color style → Name: "Primary/Dark"
   - Primary Main: `#1E4E79` → Create style: "Primary/Main"
   - Primary Light: `#2563AB` → Create style: "Primary/Light"

3. **Secondary Colors** - Same process:
   - Secondary Dark: `#92400E` → "Secondary/Dark"
   - Secondary Main: `#D97706` → "Secondary/Main"
   - Secondary Light: `#F59E0B` → "Secondary/Light"

4. **Status Colors**:
   - Success: `#059669` → "Status/Success" (DIY Easy)
   - Warning: `#D97706` → "Status/Warning" (DIY Hard)
   - Error: `#DC2626` → "Status/Error" (Workshop)
   - Info: `#2563AB` → "Status/Info"

5. **Neutral Colors**:
   - Dark: `#111827` → "Neutral/Dark"
   - Gray: `#6B7280` → "Neutral/Gray"
   - Light: `#F3F4F6` → "Neutral/Light"
   - White: `#FFFFFF` → "Neutral/White"

**Pro tip:** Group colors dengan slash notation (Primary/Dark) untuk organize styles

### Step 2.2: Typography Styles

1. **Create frame:** "Typography Scale" (1200x1000px)

2. **Install Font:** Inter (Google Fonts)
   - Menu → File → Font settings → Add "Inter"

3. **Create Text Styles:**

**Heading 1:**
- Create text: "Heading 1 - Main Page Headings"
- Font: Inter Bold
- Size: 32px (2rem)
- Line height: 44.8px (140%)
- Letter spacing: -0.64px (-2%)
- Right-click → Create text style → "Heading/H1"

**Heading 2:**
- Text: "Heading 2 - Section Headings"
- Inter Bold, 24px, line height 32px, -0.24px
- Style: "Heading/H2"

**Heading 3:**
- Text: "Heading 3 - Card Titles"
- Inter Semibold, 20px, line height 25.6px, 0px
- Style: "Heading/H3"

**Heading 4:**
- Text: "Heading 4 - Component Headings"
- Inter Semibold, 18px, line height 24px, 0px
- Style: "Heading/H4"

**Body:**
- Text: "Body - Regular text for content and descriptions"
- Inter Regular, 16px, line height 25.6px (160%), 0px
- Style: "Body/Regular"

**Small:**
- Text: "Small - Labels and secondary text"
- Inter Regular, 14px, line height 19.6px, 0px
- Style: "Body/Small"

**Caption:**
- Text: "Caption - Metadata and captions"
- Inter Medium, 12px, line height 16px, 0.12px
- Style: "Body/Caption"

### Step 2.3: Spacing System

1. **Create frame:** "Spacing Grid" (800x600px)
2. Create rectangles showing 8px grid:
   - 4px (xs)
   - 8px (sm) - base unit
   - 16px (md)
   - 24px (lg)
   - 32px (xl)
   - 48px (2xl)

**Pro tip:** Use Auto Layout dengan 8px spacing untuk consistency

### Step 2.4: Component Library

#### Button Components

1. **Create frame:** "Buttons" (1000x600px)

2. **Button - Primary:**
   - Rectangle: 120x48px
   - Background: Gradient linear 135° (#1E4E79 → #2563AB)
   - Border radius: 8px
   - Text: "Button Text" (Inter Semibold, 16px, white)
   - Padding: 12px vertical, 24px horizontal (Auto Layout)
   - Create Component: Cmd/Ctrl+Alt+K → Name: "Button/Primary"

3. **Add Variants:**
   - Default state (created)
   - Hover: Slightly darker gradient + shadow
   - Active: Even darker
   - Disabled: Gray + 50% opacity

4. **Button - Secondary:**
   - Same size (120x48px)
   - Background: transparent
   - Border: 2px solid Primary/Main
   - Text color: Primary/Main
   - Create Component: "Button/Secondary"
   - Add same 4 variants

5. **Button - Ghost:**
   - No background, no border
   - Just text (Primary/Main color)
   - Padding: 8px 16px
   - Component: "Button/Ghost"

#### Card Components

1. **Create frame:** "Cards" (1200x800px)

2. **Base Card:**
   - Rectangle: 380x300px
   - Background: White
   - Border radius: 12px
   - Shadow: 0px 2px 8px rgba(0,0,0,0.1)
   - Auto Layout: vertical, 24px padding
   - Create Component: "Card/Base"

3. **Card Variants:**
   - **Easy Severity:** Add left border 4px solid Success
   - **Hard Severity:** Left border Warning
   - **Workshop Severity:** Left border Error

4. **Status Card (Recent Diagnosis):**
   - Use Card/Base
   - Add: Header (icon + title), Content area, Status badges
   - Component: "Card/Status"

#### Badge Components

1. **Create frame:** "Badges" (800x400px)

2. **Severity Easy:**
   - Rectangle: auto width x 32px
   - Background: `#ECFDF5`
   - Border radius: 16px (pill shape)
   - Text: "DIY EASY" (Inter Semibold, 14px, `#065F46`)
   - Padding: 4px 12px (Auto Layout)
   - Component: "Badge/Severity-Easy"

3. **Severity Hard:**
   - Background: `#FFFBEB`
   - Text: "DIY HARD" (color `#92400E`)
   - Component: "Badge/Severity-Hard"

4. **Severity Workshop:**
   - Background: `#FEF2F2`
   - Text: "WORKSHOP REQUIRED" (color `#991B1B`)
   - Component: "Badge/Severity-Workshop"

#### Input Components

1. **Text Input:**
   - Rectangle: 360x48px
   - Background: White
   - Border: 2px solid `#E5E7EB`
   - Border radius: 8px
   - Placeholder text: Inter Regular 16px Gray
   - Component: "Input/Text"
   - Variants: Default, Focused (border Primary/Light + shadow), Error

2. **Textarea:**
   - Same style, height 150px
   - Component: "Input/Textarea"

---

## Phase 3: Screen Designs (60 menit)

### Page: 📱 Screens

### Step 3.1: Dashboard Screen

1. **Create frame:** "Dashboard" (1920x1080px)

2. **Navigation Bar** (top, 64px height):
   - Rectangle: full width x 64px
   - Gradient background: Primary/Dark → Primary/Main (135°)
   - Logo text: "🚗 OTOMOTIF AI" (white, H3)
   - Search input (300px width)
   - Auto Layout: horizontal, space-between

3. **Sub Navigation Menu:**
   - Below navbar, same background
   - Items: Dashboard, 3D Configurator, AI Diagnosis, Spare Parts, Workshops, History
   - Horizontal Auto Layout, 24px gap
   - Active state: white background 20% opacity

4. **Dashboard Header:**
   - Padding top: 32px
   - H1: "Dashboard"
   - Body/Small: "Selamat datang di Platform Otomotif AI"
   - Margin bottom: 32px

5. **Cards Grid:**
   - Auto Layout: horizontal wrap, 3 columns
   - Gap: 24px
   - Cards:
     - Recent Diagnosis (use Card/Status component)
     - Quick 3D Configurator (Card/Base + 4 steps)
     - Statistics (Card/Base + 4 metrics grid)

6. **Quick Actions:**
   - Section title: "Quick Actions" (H2)
   - 4 action cards: Diagnosis, Spare Parts, Workshop, Settings
   - Auto Layout: horizontal, 16px gap

**Reference:** Lihat `design-mockups/dashboard.html` untuk visual

### Step 3.2: 3D Configurator Screen

1. **Create frame:** "3D Configurator" (1920x1080px)

2. **Layout:** Horizontal Auto Layout, 2 sections

3. **Left: Canvas Area (70% width):**
   - Background: Gradient `#f5f5f5` → `#e8e8e8` (135°)
   - Placeholder: Large icon 🎨 (center)
   - Toolbar (bottom center):
     - Frame: Auto Layout horizontal, white background
     - Border radius: 12px
     - Shadow: 0 4px 12px rgba(0,0,0,0.15)
     - Buttons: Reset, Zoom In, Zoom Out, Rotate, Save
     - Gap: 16px, padding: 12px 24px

4. **Right: Component Panel (30% width):**
   - **Panel Header:**
     - Background: Light
     - Padding: 24px
     - Title: "Component Selector" (H3)
     - Border bottom: 1px Light

   - **Component Sections** (scrollable):
     - Section: Wheels 🛞
       - Collapsible header (Auto Layout)
       - Items: 2 wheel components
       - Each item: name, price range, Preview + Apply buttons
     - Section: Exhaust 🔥
     - Section: Body Kit 🎨
     - Section: Suspension ⚙️

   - **Legend (bottom):**
     - Background: Light
     - 3 legend items dengan colored dots
     - Padding: 24px

**Reference:** `design-mockups/3d-configurator.html`

### Step 3.3: AI Diagnosis Screen

1. **Create frame:** "AI Diagnosis" (1920x1080px)

2. **Layout:** Horizontal Auto Layout, 2 columns (1fr 2fr)

3. **Left: Input Panel (narrower):**
   - White background card
   - Padding: 24px
   - Sections (vertical Auto Layout, 20px gap):
     - **Title:** "Ceritakan Masalah Kendaraan Anda" (H3)
     - **Textarea:** Input/Textarea component
       - Placeholder: "Contoh: Motor Vario saya..."
       - Mic button (bottom right, floating)
     - **Vehicle Selector:** Dropdown input
     - **Sample Questions:** 4 clickable question cards
     - **Analyze Button:** Button/Primary full width

4. **Right: Result Panel (wider):**
   - White background card
   - Padding: 24px
   - Sections (vertical Auto Layout):
     - **Severity Badge:** Badge/Severity-Easy component
     - **Conclusion:** H2 text "Kerusakan terindikasi pada..."
     - **Confidence Score:** 
       - Label + progress bar (92%)
       - Bar: 100px x 8px, filled 92%
     - **Section: Penjelasan Teknis** (H4 + body text)
     - **Section: Langkah Perbaikan:**
       - 7 step items (numbered circles + text)
       - Auto Layout vertical, 12px gap
     - **Section: Suku Cadang:**
       - 2 part cards (icon + name + price + Shopee link)
       - Auto Layout, 16px gap

**Reference:** `design-mockups/ai-diagnosis.html`

### Step 3.4: Workshop Finder Screen (Optional)

1. **Create frame:** "Workshop Finder" (1920x1080px)
2. **Layout:** 70% map view + 30% filter panel
3. Use placeholder for map area
4. Right panel: Location search, filters (radius, rating, specialty)

### Step 3.5: Authentication Screens (Optional)

1. **Login Frame:** 1920x1080px
   - Centered card: 480x600px
   - Logo, email input, password input, login button, OAuth buttons
2. **Register Frame:** Similar layout, more fields
3. **Forgot Password Frame:** Simplified, just email input

---

## Phase 4: Prototyping (20 menit)

### Page: 🔄 Prototypes

### Step 4.1: Create Interactions

1. **Switch to Prototype mode** (top right)

2. **Main User Flow:**
   - Login → Dashboard: Click "Login" button
   - Dashboard → 3D Configurator: Click "Quick 3D Configurator" card
   - Dashboard → AI Diagnosis: Click "Diagnosis Story" action
   - AI Diagnosis Input → Result: Click "Analyze" button

3. **Component Interactions:**
   - Button hover states: On hover → Change to hover variant
   - Card hover: On hover → Lift animation (4px up)
   - Section collapse: Click header → Toggle visibility

4. **Transitions:**
   - Screen transitions: Smart Animate, 300ms, Ease Out
   - Hover effects: Instant or 100ms

### Step 4.2: Create Presentation

1. **Set starting frame:** Dashboard
2. **Test prototype:** Click Play (▶) button top right
3. **Share:** Click Share → Copy link → Send to team

---

## Phase 5: Component Documentation (15 menit)

### In Design System Page

1. **For each component:**
   - Add description text beside component
   - Document props/variants
   - Note usage guidelines

2. **Example - Button/Primary:**
   ```
   Button - Primary
   
   Usage: Main CTAs, form submits, primary actions
   States: Default, Hover, Active, Disabled
   Sizes: Default (48px height), Large (56px)
   
   Props:
   - Text (string)
   - Icon (optional)
   - Full width (boolean)
   ```

---

## Phase 6: Developer Handoff (10 menit)

### Step 6.1: Inspect Panel Setup

1. **Enable Dev Mode:** Switch mode (top right)
2. **Check measurements:** All spacing in 8px increments
3. **Verify color codes:** Match figma-design-specification.json

### Step 6.2: Export Assets

1. **Icons:**
   - Select all icons
   - Right panel → Export → SVG, 24px
   - Export to: `exports/icons/`

2. **Components:**
   - Export component states as PNG
   - 2x scale for retina

3. **Design Tokens:**
   - Use plugin: "Design Tokens" atau "Style Dictionary"
   - Export JSON dengan all colors, typography, spacing

### Step 6.3: Documentation

1. **Add README in Figma:**
   - Create frame: "README - Developer Guide"
   - Document:
     - File structure
     - Component naming conventions
     - How to use design tokens
     - Links to GitHub repo

2. **Comments:**
   - Add comments for complex interactions
   - Tag developers dengan @mentions

---

## Phase 7: Final Review (10 menit)

### Checklist

**Design System:**
- [ ] 11 color styles created (Primary x3, Secondary x3, Status x4, Neutral x1)
- [ ] 7 text styles created (H1-H4, Body, Small, Caption)
- [ ] Spacing grid documented (8px base)
- [ ] All components created dengan variants

**Screens:**
- [ ] Dashboard (1920x1080) complete
- [ ] 3D Configurator complete
- [ ] AI Diagnosis complete
- [ ] Workshop Finder (optional) complete
- [ ] Auth screens (optional) complete

**Prototyping:**
- [ ] Main user flows linked
- [ ] Component interactions working
- [ ] Transitions smooth (300ms)
- [ ] Starting frame set

**Developer Handoff:**
- [ ] Dev Mode enabled
- [ ] Measurements verified (8px grid)
- [ ] Export assets prepared
- [ ] Documentation added

---

## Export & Share

### Final Steps

1. **Organize Layers:**
   - Rename all frames clearly
   - Group related components
   - Lock background elements

2. **Clean Up:**
   - Delete unused components
   - Merge duplicate styles
   - Update component descriptions

3. **Share Link:**
   - Click "Share" (top right)
   - Set permissions: "Anyone with link can view"
   - Copy link
   - Share to team: fajar1180, ilhamalmunawar05-cpu

4. **GitHub Integration:**
   - Add Figma link to GitHub README.md
   - Update issue #14 dengan Figma file link
   - Mark issue as "Done"

---

## Troubleshooting

### Common Issues

**Font tidak tersedia:**
- Install Inter font dari Google Fonts
- Upload custom font files di Figma settings

**Color tidak match:**
- Double check HEX codes di `figma-design-specification.json`
- Use color picker untuk precision

**Auto Layout tidak bekerja:**
- Ensure parent frame has Auto Layout enabled
- Check direction (horizontal/vertical)
- Verify padding/gap values

**Component variants hilang:**
- Re-create component sebagai main component
- Add variants via right panel: Component → Variants

**Export gagal:**
- Check file size limits
- Export in smaller batches
- Use SVG untuk icons, PNG untuk raster

---

## Resources

### Files Reference
- `figma-design-specification.json` - Complete design tokens
- `design-mockups/dashboard.html` - Dashboard visual reference
- `design-mockups/3d-configurator.html` - Configurator reference
- `design-mockups/ai-diagnosis.html` - Diagnosis reference
- `UI_UX_Design_Specification.md` - Full design documentation

### Links
- Figma Help: https://help.figma.com
- Inter Font: https://fonts.google.com/specimen/Inter
- Design Tokens Plugin: Figma Community
- Auto Layout Guide: https://help.figma.com/hc/en-us/articles/360040451373

### Team Contacts
- Project Manager: fajar1180 (GitHub)
- Designer: ilhamalmunawar05-cpu (GitHub)
- Repository: https://github.com/Fajar1180/Project-Otomotif-Visual3D

---

## Estimated Time

- **Phase 1:** Setup (5 min)
- **Phase 2:** Design System (30 min)
- **Phase 3:** Screens (60 min)
- **Phase 4:** Prototyping (20 min)
- **Phase 5:** Documentation (15 min)
- **Phase 6:** Handoff (10 min)
- **Phase 7:** Review (10 min)

**Total:** ~2.5 hours untuk complete Figma file

---

**STATUS: READY FOR IMPLEMENTATION** ✅  
**Last Updated:** 19 Oktober 2026  
**Version:** 1.0

*Follow this guide step-by-step untuk create production-ready Figma design file*