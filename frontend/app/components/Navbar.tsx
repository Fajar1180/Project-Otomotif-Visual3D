'use client';

import Link from 'next/link';
import { useAuthStore } from '@/app/store/auth';
import { useRouter } from 'next/navigation';

export default function Navbar() {
  const { user, logout, isAuthenticated } = useAuthStore();
  const router = useRouter();

  const handleLogout = () => {
    logout();
    router.push('/login');
  };

  return (
    <nav className="bg-[var(--card)] border-b border-[var(--border)] sticky top-0 z-50">
      <div className="container-app flex items-center justify-between h-16">
        <Link href="/" className="flex items-center gap-2">
          <svg
            className="w-8 h-8"
            viewBox="0 0 32 32"
            role="img"
            aria-label="Logo Otomotif AI"
          >
            <title>Otomotif AI</title>
            {/* vehicle silhouette */}
            <path
              fill="#10B981"
              d="M2 24 h3 l1-5 h12 l1 5 h3 l-2-8 h-3 l1-4 h-3 l-2-4 h-6 l-2 4 h-3 l1 4 h-3 l-2 8 h-3 z"
            />
            <circle cx="7" cy="24" r="2" fill="#10B981" />
            <circle cx="22" cy="24" r="2" fill="#10B981" />
            {/* gear (AI) */}
            <circle cx="26" cy="6" r="4" fill="none" stroke="#10B981" strokeWidth="1.5" />
            <path
              fill="#10B981"
              d="M26 2 l-1 1 h-2 l-1 -1 l-1 1 h-2 l-1 -1 l-1 1 h-2 l-1 -1 l-1 1 h-1 l1 3 v2 l-3 1 l1 3 h2 l1 3 v2 l3 1 l-1 3 h2 l1 -3 v-2 l3 -1 l-1 -3 h2 l1 -3 v-2 l1 -3 h1 l-1 -1 z"
            />
            {/* AI circuit nodes */}
            <circle cx="24" cy="10" r="1.2" fill="#10B981" />
            <circle cx="28" cy="10" r="1.2" fill="#10B981" />
            <path fill="none" stroke="#10B981" strokeWidth="1.5" d="M25 10 L27 10" />
          </svg>
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

        <div className="flex items-center gap-3">
          {isAuthenticated ? (
            <>
              <span className="text-sm text-[var(--muted-foreground)]">
                {user?.email}
              </span>
              <button
                onClick={handleLogout}
                className="text-sm font-medium text-red-500 hover:underline"
              >
                Keluar
              </button>
            </>
          ) : (
            <>
              <Link
                href="/login"
                className="text-sm font-medium hover:text-[var(--accent)]"
              >
                Masuk
              </Link>
              <Link
                href="/register"
                className="text-sm bg-[var(--accent)] text-white px-3 py-1 rounded hover:opacity-90"
              >
                Daftar
              </Link>
            </>
          )}
        </div>
      </div>
    </nav>
  );
}
