'use client'

export default function Footer() {
  return (
    <footer className="bg-[var(--card)] border-t border-[var(--border)] mt-16">
      <div className="container-app py-8">
        <div className="grid grid-cols-4 gap-8 mb-8">
          <div>
            <h3 className="font-bold mb-4">Product</h3>
            <ul className="space-y-2 text-sm text-[var(--muted-foreground)]">
              <li><a href="#" className="hover:text-[var(--foreground)]">AI Diagnosis</a></li>
              <li><a href="#" className="hover:text-[var(--foreground)]">3D Configurator</a></li>
              <li><a href="#" className="hover:text-[var(--foreground)]">Workshop Finder</a></li>
            </ul>
          </div>
          <div>
            <h3 className="font-bold mb-4">Company</h3>
            <ul className="space-y-2 text-sm text-[var(--muted-foreground)]">
              <li><a href="#" className="hover:text-[var(--foreground)]">About</a></li>
              <li><a href="#" className="hover:text-[var(--foreground)]">Blog</a></li>
              <li><a href="#" className="hover:text-[var(--foreground)]">Contact</a></li>
            </ul>
          </div>
          <div>
            <h3 className="font-bold mb-4">Resources</h3>
            <ul className="space-y-2 text-sm text-[var(--muted-foreground)]">
              <li><a href="#" className="hover:text-[var(--foreground)]">Docs</a></li>
              <li><a href="#" className="hover:text-[var(--foreground)]">API</a></li>
              <li><a href="#" className="hover:text-[var(--foreground)]">FAQ</a></li>
            </ul>
          </div>
          <div>
            <h3 className="font-bold mb-4">Legal</h3>
            <ul className="space-y-2 text-sm text-[var(--muted-foreground)]">
              <li><a href="#" className="hover:text-[var(--foreground)]">Privacy</a></li>
              <li><a href="#" className="hover:text-[var(--foreground)]">Terms</a></li>
              <li><a href="#" className="hover:text-[var(--foreground)]">License</a></li>
            </ul>
          </div>
        </div>
        <div className="border-t border-[var(--border)] pt-8 flex items-center justify-between text-sm text-[var(--muted-foreground)]">
          <p>&copy; 2026 Otomotif AI. All rights reserved.</p>
          <div className="flex gap-4">
            <a href="#" className="hover:text-[var(--foreground)]">Twitter</a>
            <a href="#" className="hover:text-[var(--foreground)]">GitHub</a>
            <a href="#" className="hover:text-[var(--foreground)]">LinkedIn</a>
          </div>
        </div>
      </div>
    </footer>
  )
}
