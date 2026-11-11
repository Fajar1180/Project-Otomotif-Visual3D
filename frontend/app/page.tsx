'use client'

export default function Dashboard() {
  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-4xl font-bold mb-2">Welcome to Otomotif AI</h1>
        <p className="text-[var(--muted-foreground)]">
          AI-powered vehicle diagnostics, 3D customization, and workshop finder
        </p>
      </div>

      <div className="grid grid-cols-3 gap-6">
        <div className="card">
          <div className="w-12 h-12 bg-blue-100 rounded-lg mb-4" />
          <h3 className="font-bold mb-2">AI Diagnosis</h3>
          <p className="text-sm text-[var(--muted-foreground)] mb-4">
            Get instant AI-powered diagnosis for your vehicle issues
          </p>
          <a
            href="/diagnosis"
            className="text-[var(--accent)] font-medium hover:underline"
          >
            Start Diagnosis →
          </a>
        </div>

        <div className="card">
          <div className="w-12 h-12 bg-green-100 rounded-lg mb-4" />
          <h3 className="font-bold mb-2">3D Configurator</h3>
          <p className="text-sm text-[var(--muted-foreground)] mb-4">
            Visualize and customize your vehicle in 3D
          </p>
          <a
            href="/configurator"
            className="text-[var(--accent)] font-medium hover:underline"
          >
            Configure Now →
          </a>
        </div>

        <div className="card">
          <div className="w-12 h-12 bg-purple-100 rounded-lg mb-4" />
          <h3 className="font-bold mb-2">Workshop Finder</h3>
          <p className="text-sm text-[var(--muted-foreground)] mb-4">
            Find nearby workshops and repair services
          </p>
          <a
            href="#"
            className="text-[var(--accent)] font-medium hover:underline"
          >
            Find Workshops →
          </a>
        </div>
      </div>

      <div className="card bg-gradient-to-r from-blue-50 to-green-50 border-0">
        <h3 className="font-bold mb-4">Recent Activity</h3>
        <div className="space-y-2 text-sm text-[var(--muted-foreground)]">
          <p>• No recent activity yet</p>
          <p>• Start your first diagnosis to begin</p>
        </div>
      </div>
    </div>
  )
}
