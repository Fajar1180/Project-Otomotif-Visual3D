"use client";

import { useState } from "react";
import { useAuthStore } from "@/app/store/auth";
import Link from "next/link";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const { login, isLoading, error, clearError } = useAuthStore();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    clearError();
    try {
      await login(email, password);
    } catch {
      // error already set in store
    }
  };

  return (
    <div className="min-h-[calc(100vh-4rem)] flex items-center justify-center py-8 px-4">
      <div className="w-full max-w-md space-y-6">
        <div className="text-center">
          <h2 className="text-2xl font-bold">Masuk</h2>
          <p className="text-[var(--muted-foreground)]">Selamat datang kembali</p>
        </div>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-1">Email</label>
            <input
              type="email"
              required
              className="w-full rounded border p-2 focus:outline-none focus:ring-2 focus:ring-[var(--accent)]"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">Kata Sandi</label>
            <input
              type="password"
              required
              className="w-full rounded border p-2 focus:outline-none focus:ring-2 focus:ring-[var(--accent)]"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          {error && (
            <div className="text-sm text-red-500" role="alert">
              {error}
            </div>
          )}
          <button
            type="button"
            onClick={() => {
              setEmail("user@otomotif.ai");
              setPassword("UserOtomotif2026!");
            }}
            className="w-full border border-[var(--border)] text-sm py-2 rounded hover:bg-[var(--muted)] disabled:opacity-50"
          >
            Isi Akun Demo
          </button>
          <button
            type="submit"
            disabled={isLoading}
            className="w-full bg-[var(--accent)] text-white py-2 rounded hover:opacity-90 disabled:opacity-50"
          >
            {isLoading ? "Memproses..." : "Masuk"}
          </button>
        </form>

        <p className="text-center text-sm text-[var(--muted-foreground)]">
          Belum punya akun?{" "}
          <Link href="/register" className="text-[var(--accent)] font-medium">
            Daftar
          </Link>
        </p>
      </div>
    </div>
  );
}
