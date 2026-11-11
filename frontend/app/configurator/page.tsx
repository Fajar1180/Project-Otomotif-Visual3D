'use client'

import { useConfiguratorStore } from '../store'

export default function Configurator3D() {
  const { selectedParts, togglePart, clearParts } = useConfiguratorStore()

  const categories = [
    { id: 'wheels', label: 'Wheels', parts: ['Stock', '17" Alloy', '19" Performance'] },
    { id: 'exhaust', label: 'Exhaust', parts: ['Stock', 'Catback', 'Full System'] },
    { id: 'suspension', label: 'Suspension', parts: ['Stock', 'Sport', 'Lowered'] },
    { id: 'body', label: 'Body Kit', parts: ['Stock', 'Sport', 'Aggressive'] },
  ]

  return (
    <div className="max-w-6xl space-y-8">
      <div>
        <h1 className="text-3xl font-bold mb-2">3D Configurator</h1>
        <p className="text-[var(--muted-foreground)]">
          Visualize and customize your vehicle in 3D. Canvas loading coming soon.
        </p>
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

        <div className="col-span-3 card bg-gradient-to-br from-gray-100 to-gray-200 flex items-center justify-center min-h-96">
          <div className="text-center">
            <div className="text-6xl mb-4">🚗</div>
            <p className="font-bold text-lg mb-2">3D Canvas</p>
            <p className="text-[var(--muted-foreground)]">
              Three.js visualization coming soon
            </p>
            <p className="text-sm text-[var(--muted-foreground)] mt-4">
              Selected Parts: {Object.keys(selectedParts).length}
            </p>
          </div>
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
