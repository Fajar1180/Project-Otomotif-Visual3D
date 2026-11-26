'use client'

import { useEffect, useState, Suspense } from 'react'
import { Canvas, useLoader } from '@react-three/fiber'
import { OrbitControls } from '@react-three/drei'
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js'
import Link from 'next/link'
import { apiRequest } from '../lib/api'

// URL validation for 3D model loading - only allow local paths or trusted origins
const ALLOWED_MESH_PATTERN = /^\/(.*)$/i
const TRUSTED_MESH_ORIGINS = ['https://app.otomotif-ai.com', 'https://www.otomotif-ai.com']

function validateMeshUrl(url: string): string | null {
  // Reject dangerous schemes
  if (/^javascript:/i.test(url) || /^data:/i.test(url)) {
    console.error('Rejected dangerous URL scheme:', url)
    return null
  }
  // Allow local paths starting with /
  if (ALLOWED_MESH_PATTERN.test(url)) {
    return url
  }
  // Allow trusted origins (checked at runtime in useEffect)
  if (TRUSTED_MESH_ORIGINS.some(origin => url.startsWith(origin))) {
    return url
  }
  console.error('Rejected untrusted mesh URL:', url)
  return null
}

interface Vehicle3DViewerProps {
  taskId: string
}

interface AffiliatePart {
  part_id: string
  shopee_affiliate_link: string
}

function ModelCanvas({ meshUrl, color }: { meshUrl: string; color: string }) {
  const gltf = useLoader(GLTFLoader, meshUrl)

  useEffect(() => {
    if (!gltf) return
    gltf.scene.traverse((child: any) => {
      if (child.isMesh && child.material) {
        child.material.color.set(color)
      }
    })
  }, [color, gltf])

  return (
    <Canvas shadows className="h-80 w-full">
      <ambientLight intensity={0.5} />
      <directionalLight position={[5, 10, 7]} intensity={1} castShadow />
      <OrbitControls enableZoom enablePan={false} />
      <Suspense fallback={null}>
        <primitive object={gltf.scene} />
      </Suspense>
    </Canvas>
  )
}

export function Vehicle3DViewer({ taskId }: Vehicle3DViewerProps) {
  const [meshUrl, setMeshUrl] = useState<string | null>(null)
  const [status, setStatus] = useState<'idle' | 'loading' | 'completed' | 'error'>('idle')
  const [color, setColor] = useState('#3b82f6')
  const [selectedPart, setSelectedPart] = useState('body')
  const [affiliateParts, setAffiliateParts] = useState<AffiliatePart[]>([])

  // Poll 3D status endpoint until COMPLETED
  useEffect(() => {
    if (!taskId) return
    let active = true
    async function poll() {
      setStatus('loading')
      try {
        const res = await apiRequest(`/api/v1/3d/status/${encodeURIComponent(taskId)}`)
        if (!res.ok) throw new Error('Gagal memuat status')
        const data = await res.json()
        if (!active) return
        if (data.status === 'COMPLETED' && data.mesh_url) {
          const validatedUrl = validateMeshUrl(data.mesh_url)
          if (validatedUrl) {
            setMeshUrl(validatedUrl)
            setStatus('completed')
          }
        } else if (data.status === 'FAILED') {
          setStatus('error')
        } else {
          setTimeout(poll, 2000)
        }
      } catch {
        if (active) setStatus('error')
      }
    }
    poll()
    return () => { active = false }
  }, [taskId])

  const handlePartChange = async (part: string) => {
    setSelectedPart(part)
    if (!meshUrl) return
    try {
      const res = await apiRequest(`/api/v1/3d/modify`, {
        method: 'POST',
        body: JSON.stringify({
          base_mesh_id: meshUrl,
          modifications: [
            { component_type: 'part', part_id: part, parameters: {} }
          ],
        }),
      })
      if (!res.ok) throw new Error('Modify gagal')
      const data = await res.json()
      setAffiliateParts(data.affiliate_links || [])
    } catch (e) {
      console.error(e)
    }
  }

  if (status === 'error') {
    return (
      <div className="card p-4 text-red-500 text-sm">
        Gagal memuat model 3D. Pastikan task ID valid dan backend berjalan.
      </div>
    )
  }
  if (status !== 'completed' || !meshUrl) {
    return (
      <div className="card flex flex-col items-center justify-center h-96 text-[var(--muted-foreground)]">
        <div className="text-4xl mb-2">🚗</div>
        <p className="text-sm">Menunggu model 3D selesai diproses...</p>
        <p className="text-xs mt-2">Task ID: {taskId}</p>
      </div>
    )
  }

  return (
    <div className="card p-4 relative">
      <div className="absolute top-3 right-3 flex flex-col gap-1.5">
        <span className="bg-[var(--card)] px-2 py-1 rounded border border-[var(--border)] text-xs">
          Status: {status}
        </span>
        <div className="flex gap-1">
          <button
            onClick={() => handlePartChange('body')}
            className={`px-2 py-1 rounded text-xs border ${selectedPart === 'body' ? 'bg-[var(--accent)] text-white border-[var(--accent)]' : 'bg-gray-100 border-gray-200'}`}
          >
            Body
          </button>
          <button
            onClick={() => handlePartChange('wheels')}
            className={`px-2 py-1 rounded text-xs border ${selectedPart === 'wheels' ? 'bg-[var(--accent)] text-white border-[var(--accent)]' : 'bg-gray-100 border-gray-200'}`}
          >
            Wheels
          </button>
        </div>
      </div>

      {meshUrl ? <ModelCanvas meshUrl={meshUrl} color={color} /> : null}
      <div className="mt-3 flex items-center gap-2">
        <label className="text-xs text-[var(--muted-foreground)]">Warna:</label>
        <input
          type="color"
          value={color}
          onChange={(e) => setColor(e.target.value)}
          className="w-8 h-8 rounded cursor-pointer border-0 bg-transparent"
        />
      </div>
      {affiliateParts.length > 0 && (
        <div className="mt-4 p-3 bg-blue-50 rounded border border-blue-100">
          <h4 className="text-sm font-bold mb-2">Rekomendasi Part (Shopee Affiliate)</h4>
          <div className="space-y-2">
            {affiliateParts.map((p) => (
              <div key={p.part_id} className="flex justify-between items-center text-sm">
                <span className="truncate max-w-[120px]">{p.part_id}</span>
                <Link
                  href={p.shopee_affiliate_link}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-[var(--accent)] text-xs hover:underline"
                >
                  Buka di Shopee →
                </Link>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}
