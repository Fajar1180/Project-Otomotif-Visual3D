"use client";

import { useState } from "react";
import { useShopeeSearch, ShopeeProduct } from "./ShopeeSearch";

export const ShopeeSearchPage = () => {
  const { query, setQuery, loading, error, search } = useShopeeSearch((items) => setResults(items));
  const [results, setResults] = useState<ShopeeProduct[]>([]);

  return (
    <div className="min-h-screen p-4 bg-gray-50">
      <h1 className="text-2xl font-bold mb-6">Cari Produk Shopee</h1>

      <div className="bg-white p-6 rounded-lg shadow mb-8">
        <form
          onSubmit={e => {
            e.preventDefault();
            search();
          }}
        >
          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium mb-2">Kata kunci</label>
              <input
                value={query}
                onChange={e => setQuery(e.target.value)}
                placeholder="Masukkan produk yang dicari..."
                required
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-2">Batas hasil</label>
              <select
                value={10}
                onChange={() => {/* limit diatur di hook */}
                }
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
              >
                <option value={5}>5</option>
                <option value={10}>10</option>
                <option value={15}>15</option>
                <option value={20}>20</option>
              </select>
            </div>
          </div>
          <button
            type="submit"
            disabled={loading}
            className="w-full py-3 px-6 bg-primary text-white rounded-lg font-medium hover:bg-primary/90 transition-colors disabled:opacity-50"
          >
            {loading ? "Sedang mencari..." : "Cari Produk"}
          </button>
        </form>
      </div>

      {error && (
        <div className="mb-6 p-4 bg-red-100 rounded-lg text-red-800">
          {error}
        </div>
      )}

      {results.length > 0 && (
        <div className="mb-6">
          <h2 className="text-lg font-bold mb-4">Hasil pencarian</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {results.map((product) => (
              <div key={product.id} className="bg-white p-4 rounded-lg shadow border">
                <h3 className="font-bold">{product.name}</h3>
                <p className="text-[var(--muted-foreground)]">{product.price}</p>
                <a
                  href={product.affiliate_link}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-[var(--accent)] font-medium hover:underline text-sm"
                >
                  Buka di Shopee →
                </a>
              </div>
            ))}
          </div>
        </div>
      )}

      <p className="text-sm text-gray-600 mt-8">
        Masukkan kata kunci produk untuk mencari di Shopee affiliate.
      </p>
    </div>
  );
};