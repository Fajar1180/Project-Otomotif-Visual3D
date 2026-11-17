'use client'

import { useState } from 'react'
import { useConfiguratorStore } from '../store'
import { Vehicle3DViewer } from '@/app/components/Vehicle3DViewer'
import { BASE_URL } from '@/app/lib/api'

export default function Configurator3D() {
  const { selectedParts, togglePart, clearParts } = useConfiguratorStore()
  const [taskId, setTaskId] = useState<string | null>(null)
  const [generateLoading, setGenerateLoading] = useState(false)

  const categories = [
    { id: 'wheels', label: 'Wheels', parts: ['Stock', '17" Alloy', '19" Performance'] },
    { id: 'exhaust', label: 'Exhaust', parts: ['Stock', 'Catback', 'Full System'] },
    { id: 'suspension', label: 'Suspension', parts: ['Stock', 'Sport', 'Lowered'] },
    { id: 'body', label: 'Body Kit', parts: ['Stock', 'Sport', 'Aggressive'] },
  ]

  const handleGenerate = async () => {
    setGenerateLoading(true)
    try {
      const files = ['front', 'back', 'left', 'right'].map((name) => {
        const buf = new ArrayBuffer(16)
        return new File([buf], `${name}.jpg`, { type: 'image/jpeg' })
      })
      const form = new FormData()
      form.append('vehicle_brand', 'Generic')
      form.append('vehicle_model', 'Concept')
      files.forEach((f) => form.append('images', f))

      const res = await fetch(`${BASE_URL}/api/v1/3d/generate`, {
        method: 'POST',
        body: form,
      })
      if (!res.ok) throw new Error('Generate gagal')
      const data = await res.json()
      setTaskId(data.task_id)
    } catch (e) {
      console.error(e)
      alert('Gagal generate 3D. Pastikan backend berjalan di http://localhost:8000')
    } finally {
      setGenerateLoading(false)
    }
  }

  return (
    <div className="max-w-6xl space-y-8">
      <div>
        <h1 className="text-3xl font-bold mb-2">3D Configurator</h1>
        <p className="text-[var(--muted-foreground)]">
          Visualize and customize your vehicle in 3D.
        </p>
      </div>

      <div className="card p-4">
        <div className="flex flex-col sm:flex-row gap-4 items-end">
          <div className="flex-1 min-w-[200px]">
            <label className="block text-xs font-medium mb-1 text-[var(--muted-foreground)]">
              Task ID (kosongkan untuk generate baru)
            </label>
            <input
              value={taskId ?? ''}
              onChange={(e) => setTaskId(e.target.value || null)}
              className="w-full p-2 border border-[var(--border)] rounded-lg text-sm"
              placeholder="task_xxxx"
            />
          </div>
          <button
            onClick={handleGenerate}
            disabled={generateLoading}
            className="btn btn-primary disabled:opacity-50"
          >
            {generateLoading ? 'Memproses...' : 'Generate 3D Model'}
          </button>
        </div>
      </div>

      <div className="grid grid-cols-4 gap-6">
        <div className="col-span-1 space-y-6">
          <div>
            <h3 className="font-bold mb-4">Components</h3>
            <div className="space-y-4">
              {categories.map((cat) => (
                <div key={cat.id} className="card">
                  <p className="font-medium text-sm mb-3 text-[var(--muted-foreground)]">
                    {cat.label}
                  </p>
                  <div className="space-y-2">
                    {cat.parts.map((part, i) => (
                      <button
                        key={i}
                        onClick={() => togglePart(cat.id, part)}
                        className={`w-full p-2 text-sm rounded transition-colors ${
                          selectedParts[cat.id] === part
                            ? 'bg-[var(--accent)] text-white'
                            : 'bg-gray-100 hover:bg-gray-200'
                        }`}
                      >
                        {part}
                      </button>
                    ))}
                  </div>
                </div>
              ))}
            </div>
            <button onClick={clearParts} className="btn btn-secondary w-full mt-4">
              Reset All
            </button>
          </div>
        </div>

        <div className="col-span-3 card p-4">
          <h3 className="font-bold mb-4">3D Preview</h3>
          {taskId ? (
            <Vehicle3DViewer taskId={taskId} />
          ) : (
            <div className="flex flex-col items-center justify-center h-96 text-[var(--muted-foreground)]">
              <div className="text-4xl mb-2">🚗</div>
              <p className="text-sm">Generate model 3D untuk memulai preview</p>
            </div>
          )}
        </div>
      </div>

      {Object.keys(selectedParts).length > 0 && (
        <div className="card border-[var(--accent)] border-2">
          <h3 className="font-bold mb-4">Your Configuration</h3>
          <div className="grid grid-cols-2 gap-4">
            {Object.entries(selectedParts).map(([cat, part]) => (
              <div key={cat} className="flex justify-between">
                <span className="text-sm text-[var(--muted-foreground)]">{cat}</span>
                <span className="font-medium">{part}</span>
              </div>
            ))}
          </div>
          <button className="btn btn-primary w-full mt-4">Save Configuration</button>
        </div>
      )}
    </div>
  )
}
