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
