"use client"

import { useState } from "react"
import Link from "next/link"

const MAX_EMAIL_LENGTH = 100

export default function ForgotPasswordPage() {
  const [email, setEmail] = useState("")
  const [sent, setSent] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()

    const trimmedEmail = email.trim()

    if (!trimmedEmail) {
      return
    }
    if (trimmedEmail.length > MAX_EMAIL_LENGTH) {
      alert(`Email terlalu panjang (maksimal ${MAX_EMAIL_LENGTH} karakter)`)
      return
    }

    setSent(true)
  }

  return (
    <div className="min-h-[calc(100vh-4rem)] flex items-center justify-center py-8 px-4">
      <div className="w-full max-w-md space-y-6">
        <div className="text-center">
          <h2 className="text-2xl font-bold">Lupa Kata Sandi</h2>
          <p className="text-[var(--muted-foreground)]">
            Kami akan kirim link reset ke email Anda
          </p>
        </div>

        {!sent ? (
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
            <button
              type="submit"
              className="w-full bg-[var(--accent)] text-white py-2 rounded hover:opacity-90"
            >
              Kirim Link Reset
            </button>
          </form>
        ) : (
          <div className="text-center space-y-2">
            <p className="text-green-600 font-medium">Email reset terkirim</p>
            <p className="text-xs text-[var(--muted-foreground)]">
              Periksa inbox email {email || "Anda"}
            </p>
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
  )
}
