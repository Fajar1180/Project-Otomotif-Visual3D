# Figma Design File Creation Instructions
## Platform Otomotif AI (Project Pak Yogi)

### Overview
This document provides comprehensive instructions for creating the Figma design for the Otomotif AI platform, based on the UI/UX Design Specification.

### Required Access
To create this Figma file, you'll need:
- A Figma account with proper permissions
- Access to the project organization/team: **pak-yogi** (or similar)
- Ability to create new Figma files in the project

### Current Limitations
In the current sandbox environment, direct Figma file creation is limited due to authentication and API access restrictions. The following approach provides the complete design specifications that can be imported into Figma.

---

### Figma Design File Creation Steps

#### Step 1: Create New Figma File
1. Log into Figma with the appropriate account
2. Navigate to the **pak-yogi** project/organization
3. Click "New file" → "Design" (or "FigJam" for prototyping)
4. File Name: **Project_Pak_Yogi_Design**

#### Step 2: Setup Design System
1. **Create Main Frame:** "Dashboard - Main View" (1920x1080px)
2. **Set up Color Styles:**
   - Primary Dark (#0A2463)
   - Primary Main (#1E4E79)
   - Primary Light (#2563AB)
   - Secondary Dark (#92400E)
   - etc.

3. **Typography Styles:** Create text styles for h1-h4, body, caption
4. **Component Styles:** Create button styles, card variants, severity badges

#### Step 3: Create Main Screens

##### 3.1 Dashboard Screen
```
Components:
- Top Navigation (fixed, 64px height)
- Sidebar navigation (collapsed/expanded)
- Dashboard cards:
  • Recent Diagnosis (status card)
  • Quick 3D Configurator (CTA card)
- Quick Action Buttons
- User Profile/Logout
```

##### 3.2 3D Configurator Screen
```
Components:
- 3D Canvas Area (70% width)
- Right Panel (30% width)
  • Component Tree (collapsible categories)
  • Preview cards (hover effects)
  • Apply buttons
- Legend panel (bottom, status indicators)
- Toolbar (zoom, reset, save)
```

##### 3.3 AI Diagnosis Screen
```
Components:
- Input Section (top)
  • Textarea with mic button
  • Sample question buttons
  • Vehicle context selector
- Result Panel (main area)
  • Severity indicator (badge)
  • AI explanation section
  • Repair steps (collapsible list)
  • Parts recommendations (cards)
  • Workshop suggestions (list/map toggle)
```

##### 3.4 Workshop Finder Screen
```
Components:
- Map View (main area)
- Filter Panel (right sidebar)
  • Location search
  • Radius selector
  • Rating filter
  • Specialty filter
- List View (toggle)
- Workshop detail panel
```

##### 3.5 Authentication Screens
```
Components:
- Login form (email/password + OAuth)
- Register form
- Forgot password
- Email verification
```

#### Step 4: Create Components

##### 4.1 Button Variants
```
.btn-primary { /* gradient style */ }
.btn-secondary { /* outline style */ }
.btn-ghost { /* text only */ }
.btn-disabled { /* disabled state */ }
```

##### 4.2 Status Cards
```
.card { /* base style */ }
.card.severity-easy { /* green border */ }
.card.severity-hard { /* orange border */ }
.card.severity-workshop { /* red border */ }
.card.hover { /* lift effect */ }
```

##### 4.3 Severity Indicators
```
.badge {
  .severity-easy { background: #ECFDF5, color: #065F46 }
  .severity-hard { background: #FFFBEB, color: #92400E }
  .severity-workshop { background: #FEF2F2, color: #991B1B }
}
```

##### 4.4 Form Elements
```
.input-group {
  .label { /* label style */ }
  .input-field { /* input style */ }
  .error-message { /* error style */ }
}
```

#### Step 5: Create Design Tokens

##### 5.1 Color Tokens
```
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
```
{
  "typography": {
    "h1": { "fontFamily": "Inter", "fontWeight": "Bold", "fontSize": "2.5rem", "lineHeight": "3.2rem" },
    "h2": { "fontFamily": "Inter", "fontWeight": "Bold", "fontSize": "2rem", "lineHeight": "2.8rem" },
    "body": { "fontFamily": "Inter", "fontWeight": "Regular", "fontSize": "1rem", "lineHeight": "1.6rem" }
  }
}
```

#### Step 6: Set Up Prototypes
```
- Create clickable hotspots on 3D configurator components
- Link screens for main user flows:
  • Dashboard → 3D Configurator → Diagnosis → Workshop
  • Login → Dashboard
  • Diagnosis → Results → Parts/Workshop
- Create transitions with appropriate easing
```

#### Step 7: Documentation and System Setup

##### 7.1 Component Documentation
For each component, document:
- Props/States
- Interaction patterns
- Accessibility notes
- Variants
- Usage guidelines

##### 7.2 Design System Documentation
```
Documentation should include:
- Color palette usage
- Typography scale
- Spacing system (8px grid)
- Shadow layers
- Border radius system
- Z-index scales
```

---

### Alternative: Manual Figma Creation

If direct tool creation isn't possible, you can:

1. **Import from Code:** Export the CSS from this specification as:
   - Component code in Figma
   - Documentation in Figma Comments
   - Design tokens as Figma variables

2. **Manual Setup:**
   - Create frames matching the specified dimensions
   - Apply colors, typography, spacing as specified
   - Build components using the provided CSS structure as reference

3. **Collaboration with Design Team:**
   - Share this specification with the design team
   - Provide clear component specs and design tokens
   - Use as base for final design iteration

---

### Export/Import Recommendations

#### Step 8: Export Design Assets
```
- Export SVG icons (all 24px variations)
- Export component states (hover, active, disabled)
- Export dark theme variants (for developer implementation)
- Export design tokens as JSON/CSS custom properties
```

#### Step 9: Developer Handoff
```
- Create figma-plugin.json with component props
- Export component specifications to developer portal
- Create interactive prototype for feedback
- Set up design review comments
```

---

### Project Progress Summary

#### Created Documents (✅)
1. **PRD (Project Requirements Document)**
2. **SRS (Software Requirements Specification)** 
3. **ERD (Entity Relationship Diagram)**
4. **API Specification**
5. **UI/UX Design Specification**

#### In Progress
- [x] Documentation deliverables
- [x] Design specifications
- [ ] Figma design file creation (requires manual setup)

#### Next Steps
1. **Manual Figma File Creation:** Due to sandbox limitations, the Figma design file needs to be created manually using the provided specifications
2. **Component Implementation:** Build all UI components following the design system
3. **Design Handoff:** Export specifications to development team
4. **Review and Iteration:** Gather feedback and refine design

---

### Implementation Notes

#### Critical Design Decisions
- **Color Psychology:** Blue tones for trust/technical reliability, orange for action/energy, green for success
- **Typography:** Inter font for modern, clean look
- **Grid System:** 8px spacing for consistency
- **3D Integration:** Priority for 3D canvas with minimal UI overlay

#### Responsive Considerations
- Mobile-first approach with progressive enhancement
- Touch targets minimum 44px
- Optimized for 320px+ width

#### Accessibility Priority
- WCAG AA compliance required
- Sufficient color contrast ratios
- Screen reader friendly
- Keyboard navigation support

---
*Document Version 1.0 | Created: 2026-10-19*

### Contact Information
For Figma file creation assistance:
- Project: Otomotif AI Platform (Project Pak Yogi)
- Team: fajar1180 (Project Manager), ilhamalmunawar05-cpu (Design Coordination)
- Repository: /c/laragon/www/Project-Otomotif-Visual3D/