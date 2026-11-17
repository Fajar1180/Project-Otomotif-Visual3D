"use client"

import { useState } from "react"
import { apiRequest } from "../lib/api"

export interface ShopeeProduct {
  id: string
  name: string
  price: string
  image: string
  affiliate_link: string
}

export interface ShopeeSearchFormProps {
  onResults: (products: ShopeeProduct[]) => void
}

const MAX_QUERY_LENGTH = 100

export const useShopeeSearch = (onResults?: (products: ShopeeProduct[]) => void) => {
  const [query, setQuery] = useState("")
  const [limit, setLimit] = useState(10)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const search = async () => {
    const trimmedQuery = query.trim()

    if (!trimmedQuery) return
    if (trimmedQuery.length > MAX_QUERY_LENGTH) {
      setError(`Query terlalu panjang (maksimal ${MAX_QUERY_LENGTH} karakter)`)
      return
    }

    setLoading(true)
    setError(null)

    try {
      const res = await apiRequest("/shopee/search", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${typeof window !== "undefined" ? localStorage.getItem("token") : ""}`,
        },
        body: JSON.stringify({ query: trimmedQuery, limit }),
      })

      if (res.status === 401) {
        setError("Token tidak valid atau expired")
        return
      }

      if (!res.ok) {
        throw new Error("Gagal mengambil data Shopee")
      }

      const data = await res.json()
      setError(null)
      onResults?.(data.items || [])
    } catch (e: any) {
      setError(e.message || "Terjadi kesalahan")
    } finally {
      setLoading(false)
    }
  }

  return {
    query,
    setQuery,
    limit,
    setLimit,
    loading,
    error,
    search,
  }
}
