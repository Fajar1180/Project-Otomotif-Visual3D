"use client"

import { useState } from "react"
import { useAuthStore } from "@/app/store/auth"
import Link from "next/link"

const MAX_NAME_LENGTH = 50
const MAX_EMAIL_LENGTH = 100

export default function RegisterPage() {
  const [fullName, setFullName] = useState("")
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const { register, isLoading, error, clearError } = useAuthStore()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    clearError()

    const trimmedName = fullName.trim()
    const trimmedEmail = email.trim()

    if (!trimmedName) {
      return
    }
    if (trimmedName.length > MAX_NAME_LENGTH) {
      alert(`Nama terlalu panjang (maksimal ${MAX_NAME_LENGTH} karakter)`)
      return
    }

    if (!trimmedEmail) {
      return
    }
    if (trimmedEmail.length > MAX_EMAIL_LENGTH) {
      alert(`Email terlalu panjang (maksimal ${MAX_EMAIL_LENGTH} karakter)`)
      return
    }

    try {
      await register(trimmedName, trimmedEmail, password)
    } catch {
      // error already set in store
    }
  }

  return (
    <div className="min-h-[calc(100vh-4rem)] flex items-center justify-center py-8 px-4">
      <div className="w-full max-w-md space-y-6">
        <div className="text-center">
          <h2 className="text-2xl font-bold">Daftar</h2>
          <p className="text-[var(--muted-foreground)]">Buat akun baru</p>
        </div>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-1">Nama Lengkap</label>
            <input
              type="text"
              className="w-full rounded border p-2 focus:outline-none focus:ring-2 focus:ring-[var(--accent)]"
              value={fullName}
              onChange={(e) => setFullName(e.target.value)}
            />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">Email</label>
            <input
              type="email"
              className="w-full rounded border p-2 focus:outline-none focus:ring-2 focus:ring-[var(--accent)]"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">Kata Sandi</label>
            <input
              type="password"
              className="w-full rounded border p-2 focus:outline-none focus:ring-2 focus:ring-[var(--accent)]"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              minLength={8}
            />
          </div>
          {error && (
            <div className="text-sm text-red-500" role="alert">
              {error}
            </div>
          )}
          <button
            type="submit"
            disabled={isLoading}
            className="w-full bg-[var(--accent)] text-white py-2 rounded hover:opacity-90 disabled:opacity-50"
          >
            {isLoading ? "Memproses..." : "Daftar"}
          </button>
        </form>

        <p className="text-center text-sm text-[var(--muted-foreground)]">
          Sudah punya akun?{" "}
          <Link href="/login" className="text-[var(--accent)] font-medium">Masuk</Link>
        </p>
      </div>
    </div>
  )
}
