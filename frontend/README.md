# Otomotif AI - Frontend

Next.js frontend with TypeScript, Tailwind CSS, Zustand, and React Three Fiber.

## Setup

```bash
npm install
npm run dev
```

## Structure

- `app/` - Next.js App Router
- `app/components/` - Reusable components (Navbar, Footer)
- `app/store.ts` - Zustand state management
- `app/globals.css` - Global Tailwind styles

## Pages

- `/` - Dashboard
- `/diagnosis` - AI Diagnosis Interface
- `/configurator` - 3D Vehicle Configurator

## Configuration

- `tsconfig.json` - TypeScript configuration
- `tailwind.config.ts` - Tailwind CSS theme
- `next.config.js` - Next.js configuration
- `.env.local` - Environment variables

## TODO

- [ ] React Three Fiber 3D canvas integration
- [ ] API client utilities
- [ ] Form validation
- [ ] Error handling & loading states
- [ ] Mobile responsiveness
- [ ] Dark mode toggle
- [ ] Authentication pages
