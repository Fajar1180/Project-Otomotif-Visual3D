'use client'

import Link from 'next/link'

export default function Navbar() {
  return (
    <nav className="bg-[var(--card)] border-b border-[var(--border)] sticky top-0 z-50">
      <div className="container-app flex items-center justify-between h-16">
        <Link href="/" className="flex items-center gap-2">
          <div className="w-8 h-8 bg-[var(--accent)] rounded-lg" />
          <span className="font-bold text-lg">Otomotif AI</span>
        </Link>

        <div className="flex gap-8">
          <Link href="/" className="text-sm font-medium hover:text-[var(--accent)]">
            Dashboard
          </Link>
          <Link
            href="/diagnosis"
            className="text-sm font-medium hover:text-[var(--accent)]"
          >
            Diagnosis
          </Link>
          <Link
            href="/configurator"
            className="text-sm font-medium hover:text-[var(--accent)]"
          >
            3D Config
          </Link>
        </div>

        <button className="btn btn-primary">Sign In</button>
      </div>
    </nav>
  )
}
