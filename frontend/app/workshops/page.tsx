'use client'

import { useEffect, useState } from 'react'
import { apiRequest } from '../lib/api'

export default function WorkshopsPage() {
  const [workshops, setWorkshops] = useState<any[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const load = async () => {
      try {
        const res = await apiRequest('/api/v1/workshops')
        if (!res.ok) throw new Error('Gagal memuat bengkel')
        const data = await res.json()
        setWorkshops(data.data || data.workshops || [])
      } catch (e) {
        setError((e as Error).message)
      } finally {
        setLoading(false)
      }
    }
    load()
  }, [])

  return (
    <div className="max-w-6xl mx-auto px-4 py-8 space-y-6">
      <div>
        <h1 className="text-3xl font-bold mb-2">Workshop Finder</h1>
        <p className="text-[var(--muted-foreground)]">
          Temukan bengkel dan bengkel resmi terdekat untuk kendaraan Anda
        </p>
      </div>

      {error && (
        <div className="rounded-lg border border-red-200 bg-red-50 p-4 text-red-800 text-sm">
          {error}
        </div>
      )}

      {loading ? (
        <p className="text-[var(--muted-foreground)]">Memuat daftar bengkel...</p>
      ) : (
        <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
          {workshops.length === 0 ? (
            <p className="col-span-full text-[var(--muted-foreground)]">
              Tidak ada bengkel tersedia.
            </p>
          ) : (
            workshops.map((w: any) => (
              <div key={w.id} className="border border-[var(--border)] rounded-lg p-4 bg-white">
                <h3 className="font-bold">{w.name}</h3>
                <p className="text-sm text-[var(--muted-foreground)]">
                  {w.address || '-'}
                </p>
                {w.phone && <p className="text-sm">{w.phone}</p>}
                {w.rating != null && (
                  <p className="text-xs font-medium text-amber-600">
                    ⭐ {w.rating}
                  </p>
                )}
                {w.specialties && w.specialties.length > 0 && (
                  <p className="text-xs text-[var(--muted-foreground)]">
                    {w.specialties.join(', ')}
                  </p>
                )}
              </div>
            ))
          )}
        </div>
      )}
    </div>
  )
}
