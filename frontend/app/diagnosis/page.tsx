'use client'

import { useDiagnosisStore } from '../store'
import { useState } from 'react'

export default function DiagnosisPage() {
  const { symptomText, setSymptomsText } = useDiagnosisStore()
  const [make, setMake] = useState('')
  const [model, setModel] = useState('')
  const [year, setYear] = useState('')
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState<any>(null)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)

    try {
      const response = await fetch(
        'http://localhost:8000/api/v1/diagnosis/analyze',
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            symptom_text: symptomText,
            vehicle_make: make,
            vehicle_model: model,
            vehicle_year: parseInt(year),
          }),
        }
      )
      const data = await response.json()
      setResult(data)
    } catch (error) {
      console.error('Error:', error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="max-w-2xl space-y-8">
      <div>
        <h1 className="text-3xl font-bold mb-2">AI Diagnosis</h1>
        <p className="text-[var(--muted-foreground)]">
          Describe your vehicle symptoms and get AI-powered diagnosis
        </p>
      </div>

      <form onSubmit={handleSubmit} className="space-y-6">
        <div>
          <label className="block font-medium mb-2">Describe Your Symptoms</label>
          <textarea
            value={symptomText}
            onChange={(e) => setSymptomsText(e.target.value)}
            placeholder="e.g., Engine is making knocking sound when accelerating..."
            className="w-full p-4 border border-[var(--border)] rounded-lg focus:outline-none focus:ring-2 focus:ring-[var(--accent)]"
            rows={5}
          />
        </div>

        <div className="grid grid-cols-3 gap-4">
          <div>
            <label className="block font-medium mb-2">Make</label>
            <input
              type="text"
              value={make}
              onChange={(e) => setMake(e.target.value)}
              placeholder="Honda"
              className="w-full p-2 border border-[var(--border)] rounded-lg"
            />
          </div>
          <div>
            <label className="block font-medium mb-2">Model</label>
            <input
              type="text"
              value={model}
              onChange={(e) => setModel(e.target.value)}
              placeholder="Civic"
              className="w-full p-2 border border-[var(--border)] rounded-lg"
            />
          </div>
          <div>
            <label className="block font-medium mb-2">Year</label>
            <input
              type="number"
              value={year}
              onChange={(e) => setYear(e.target.value)}
              placeholder="2020"
              className="w-full p-2 border border-[var(--border)] rounded-lg"
            />
          </div>
        </div>

        <button
          type="submit"
          disabled={loading || !symptomText}
          className="btn btn-primary w-full disabled:opacity-50"
        >
          {loading ? 'Analyzing...' : 'Get Diagnosis'}
        </button>
      </form>

      {result && (
        <div className="card border-[var(--accent)] border-2">
          <h2 className="text-xl font-bold mb-4">Diagnosis Result</h2>
          <div className="space-y-4">
            <div>
              <p className="text-sm text-[var(--muted-foreground)]">Diagnosis</p>
              <p className="font-medium">{result.diagnosis}</p>
            </div>
            <div className="grid grid-cols-2 gap-4">
              <div>
                <p className="text-sm text-[var(--muted-foreground)]">Severity</p>
                <p className="font-medium text-[var(--accent)]">{result.severity}</p>
              </div>
              <div>
                <p className="text-sm text-[var(--muted-foreground)]">Confidence</p>
                <p className="font-medium">{(result.confidence_score * 100).toFixed(0)}%</p>
              </div>
            </div>
            {result.repair_steps && (
              <div>
                <p className="text-sm text-[var(--muted-foreground)] mb-2">Repair Steps</p>
                <ul className="space-y-2">
                  {result.repair_steps.map((step: any, i: number) => (
                    <li key={i} className="flex gap-3">
                      <span className="font-bold text-[var(--accent)]">{step.step}.</span>
                      <span>{step.description}</span>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  )
}
