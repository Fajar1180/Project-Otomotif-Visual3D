"use client";

import { useState } from "react";
import Link from "next/link";

export default function VerifyEmailPage() {
  const [token, setToken] = useState("");
  const [verified, setVerified] = useState(false);

  // TODO: Connect when backend endpoint is ready (GET /api/v1/auth/verify-email?token=...)
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setVerified(true);
  };

  return (
    <div className="min-h-[calc(100vh-4rem)] flex items-center justify-center py-8 px-4">
      <div className="w-full max-w-md space-y-6">
        <div className="text-center">
          <h2 className="text-2xl font-bold">Verifikasi Email</h2>
          <p className="text-[var(--muted-foreground)]">
            Masukkan kode verifikasi yang dikirim ke email Anda
          </p>
        </div>

        {!verified ? (
          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-sm font-medium mb-1">Kode Verifikasi</label>
              <input
                type="text"
                required
                maxLength={6}
                className="w-full rounded border p-2 focus:outline-none focus:ring-2 focus:ring-[var(--accent)] text-center"
                value={token}
                onChange={(e) => setToken(e.target.value)}
              />
            </div>
            <button
              type="submit"
              className="w-full bg-[var(--accent)] text-white py-2 rounded hover:opacity-90"
            >
              Verifikasi
            </button>
          </form>
        ) : (
          <div className="text-center space-y-2">
            <p className="text-green-600 font-medium">Email berhasil diverifikasi</p>
            <Link
              href="/login"
              className="text-[var(--accent)] font-medium hover:underline"
            >
              Kembali ke Masuk
            </Link>
          </div>
        )}
      </div>
    </div>
  );
}
