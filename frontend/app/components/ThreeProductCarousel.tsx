'use client'

import { useState, useEffect } from 'react'
import { Canvas } from '@react-three/fiber'
import { OrbitControls, PerspectiveCamera } from '@react-three/drei'
import { Color } from 'three'

export const ThreeProductCarousel = () => {
  const [products, setProducts] = useState<any[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Fetch products from backend
    const fetchProducts = async () => {
      try {
        const res = await fetch('/api/shopee/search', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ query: '', limit: 8 })
        })
        if (!res.ok) throw new Error('Failed to fetch products')
        const data = await res.json()
        setProducts(data.items || [])
      } catch (e) {
        console.error('Error fetching products:', e)
        // Fallback: create demo products
        setProducts([
          { id: '1', name: 'Oil Filter', price: '50.000₫', image: '/placeholder.svg?height=200&width=200' },
          { id: '2', name: 'Brake Pad', price: '200.000₫', image: '/placeholder.svg?height=200&width=200' },
          { id: '3', name: 'Spark Plug', price: '35.000₫', image: '/placeholder.svg?height=200&width=200' },
        ])
      } finally {
        setLoading(false)
      }
    }

    fetchProducts()
  }, [])

  if (loading) {
    return (
      <div className="h-64 bg-gray-200 flex items-center justify-center text-sm text-[var(--muted-foreground)]">
        Loading products...
      </div>
    )
  }

  return (
    <div className="relative h-64 w-full">
      <div className="absolute inset-0 flex items-center justify-center">
        <Canvas>
          <PerspectiveCamera fov={75} position={[0, 5, 10]} far={50}>
            <OrbitControls enableZoom={true} enablePan={false} minPolarAngle={0.5} maxPolarAngle={Math.PI - 0.5} />
          <ambientLight intensity={0.5} />
          <directionalLight position={[5, 10, 7]} intensity={1.5} />
          <pointLight position={[-5, 5, 5]} intensity={0.5} color="#ff6b6b" />
          
          {/* Product boxes in a circular arrangement */}
          {products.map((product, index) => {
            const angle = (index / products.length) * Math.PI * 2 - Math.PI / 2
            const radius = 3
            const x = Math.cos(angle) * radius
            const z = Math.sin(angle) * radius
            
            return (
              <mesh key={product.id} position={[x, 0, z]} rotation={[0, 0, angle]}>
                <boxGeometry args={[1.2, 1.2, 1.2]} />
                <meshStandardMaterial
                  color={new Color(product.color || '#6366f1')}
                  roughness={0.5}
                  metalness={0.2}
                />
              </mesh>
            )
          })}
          </PerspectiveCamera>
        </Canvas>
      </div>
    </div>
  )
}