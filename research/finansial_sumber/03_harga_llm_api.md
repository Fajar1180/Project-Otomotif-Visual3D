# Sumber Data Harga LLM API — OpenAI & Anthropic (Oktober 2024)

## Ringkasan Harga per 1 Million Tokens (USD)

| Provider | Model | Input ($/1M tokens) | Output ($/1M tokens) | Context Window | Sumber |
|----------|-------|---------------------|----------------------|----------------|--------|
| **OpenAI** | GPT-4o | $2.50 | $10.00 | 128K | OpenAI Pricing |
| **OpenAI** | GPT-4o-mini | $0.15 | $0.60 | 128K | OpenAI Pricing |
| **OpenAI** | GPT-4 Turbo | $10.00 | $30.00 | 128K | OpenAI Pricing |
| **OpenAI** | GPT-3.5 Turbo | $0.50 | $1.50 | 16K | OpenAI Pricing |
| **Anthropic** | Claude 3.5 Sonnet | $3.00 | $15.00 | 200K | Anthropic Pricing |
| **Anthropic** | Claude 3.5 Haiku | $0.25 | $1.25 | 200K | Anthropic Pricing (2024-10) |
| **Anthropic** | Claude 3 Opus | $15.00 | $75.00 | 200K | Anthropic Pricing |

---

## Data Detail per Provider

### 1. OpenAI API Pricing
**Sumber Resmi:** https://openai.com/api/pricing/ (akses Oktober 2024)

| Model | Input | Output | Batch API (50% off) | Cache Hit | Catatan |
|-------|-------|--------|---------------------|-----------|---------|
| **GPT-4o** (2024-08-06) | $2.50 / 1M | $10.00 / 1M | $1.25 / $5.00 | $1.25 / - | Flagship multimodal |
| **GPT-4o-mini** (2024-07-18) | $0.15 / 1M | $0.60 / 1M | $0.075 / $0.30 | $0.075 / - | Cost-efficient, 82% MMLU |
| **GPT-4 Turbo** (2024-04-09) | $10.00 / 1M | $30.00 / 1M | $5.00 / $15.00 | $5.00 / - | Legacy, 128K context |
| **GPT-3.5 Turbo** (0125) | $0.50 / 1M | $1.50 / 1M | $0.25 / $0.75 | - | Fast, cheap |
| **o1-preview** | $15.00 / 1M | $60.00 / 1M | - | - | Reasoning model |
| **o1-mini** | $3.00 / 1M | $12.00 / 1M | - | - | Small reasoning |

**Embedding Models:**
| Model | Price / 1M tokens | Dimensions |
|-------|-------------------|------------|
| text-embedding-3-large | $0.13 | 3.072 |
| text-embedding-3-small | $0.02 | 1.536 |
| text-embedding-ada-002 | $0.10 | 1.536 |

**Fine-tuning (Training + Hosting):**
| Base Model | Training / 1M tokens | Hosting / jam | Inference / 1M tokens |
|------------|----------------------|---------------|----------------------|
| GPT-4o-mini | $3.00 | $1.70 | $0.30 / $1.20 |
| GPT-3.5 Turbo | $8.00 | $1.70 | $3.00 / $6.00 |

---

### 2. Anthropic (Claude) API Pricing
**Sumber Resmi:** https://www.anthropic.com/pricing (akses Oktober 2024)

| Model | Input ($/1M) | Output ($/1M) | Context | Catatan |
|-------|--------------|---------------|---------|---------|
| **Claude 3.5 Sonnet** (2024-10-22) | $3.00 | $15.00 | 200K | Best balance, coding strong |
| **Claude 3.5 Haiku** (2024-10-22) | $0.25 | $1.25 | 200K | Fast, cheap, new |
| **Claude 3 Opus** (2024-02) | $15.00 | $75.00 | 200K | Most capable, expensive |
| **Claude 3 Sonnet** (2024-02) | $3.00 | $15.00 | 200K | Legacy |
| **Claude 3 Haiku** (2024-03) | $0.25 | $1.25 | 200K | Legacy |

**Prompt Caching (50% discount on cached tokens):**
- Cache write: $3.75 / 1M (Sonnet), $0.30 / 1M (Haiku)
- Cache read: $0.30 / 1M (Sonnet), $0.03 / 1M (Haiku)

**Batch Processing (50% off):**
- Async batch API: 50% diskon input/output

---

### 3. Perbandingan Cost per Request (Estimasi)

**Asumsi Request Rata-Rata:**
- Input: 2.000 tokens (system prompt + user query + context)
- Output: 500 tokens (response)

| Model | Cost/Request (USD) | Cost/Request (Rp*) | 10.000 req/bln (Rp) |
|-------|-------------------|-------------------|---------------------|
| GPT-4o | $0.010 | Rp 156 | Rp 1.560.000 |
| GPT-4o-mini | $0.0006 | Rp 9 | Rp 90.000 |
| GPT-3.5 Turbo | $0.00175 | Rp 27 | Rp 270.000 |
| Claude 3.5 Sonnet | $0.0135 | Rp 211 | Rp 2.110.000 |
| Claude 3.5 Haiku | $0.001125 | Rp 18 | Rp 180.000 |

*\*Kurs: Rp 15.600/USD*

---

### 4. Estimasi Penggunaan untuk Proposal (MVP)

**Skenario Diagnosis Otomotif:**
- Rata-rata input: 3.000 tokens (gejala + context bengkel + schema)
- Rata-rata output: 800 tokens (diagnosis + rekomendasi + part)
- Target: 5.000 diagnosis/bulan (early adopter 20-30 bengkel, ~200 diagnosis/bengkel/bln)

| Model | Cost/Bulan (USD) | Cost/Bulan (Rp) | Catatan |
|-------|-----------------|-----------------|---------|
| **GPT-4o-mini** (recommended) | $2.90 | **Rp 45.240** | Hemat 94% vs GPT-4o, cukup untuk diagnosis terstruktur |
| **Claude 3.5 Haiku** (alternatif) | $5.55 | **Rp 86.580** | Lebih cepat, context 200K |
| GPT-4o | $47.50 | **Rp 741.000** | Overkill untuk MVP |
| Claude 3.5 Sonnet | $67.50 | **Rp 1.053.000** | Overkill untuk MVP |

**Rekomendasi Proposal:** **GPT-4o-mini** sebagai primary, **Claude 3.5 Haiku** sebagai fallback.
- Budget LLM API MVP: **Rp 100.000/bulan** (buffer 2x)

---

### 5. Volume Discount (Enterprise)
**Sumber:** OpenAI & Anthropic Sales (kontak langsung untuk >1M tokens/bln)

| Volume Bulanan | Diskon Umum | Catatan |
|----------------|-------------|---------|
| 1M – 10M tokens | 10-20% | Perlu NDA & contract |
| 10M – 100M tokens | 20-35% | Custom pricing |
| 100M+ tokens | 35-50% | Dedicated capacity |

**Catatan untuk Proposal:** MVP tidak memerlukan enterprise pricing. Gunakan pay-as-you-go. Enterprise pricing relevan saat MAU > 50.000.

---

### 6. Alternatif Self-Hosted (Untuk Perbandingan)

| Opsi | Hardware Cost | Operational Cost | Latency | Privacy |
|------|---------------|------------------|---------|---------|
| **vLLM + Llama 3.1 8B** (A10G 24GB) | $1.00/jam (AWS g5.xlarge) | $730/bln | <100ms | Full control |
| **vLLM + Llama 3.1 70B** (A100 80GB×2) | $5.87/jam (GCP a2-highgpu-2g) | $4.284/bln | ~200ms | Full control |
| **Ollama + Llama 3.1 8B** (Local RTX 4070) | Rp 30M (one-time) | Listrik ~Rp 500k/bln | <50ms | Full control |

**Kesimpulan:** Self-hosted **lebih murah** untuk volume tinggi (>50k req/bln), tapi butuh DevOps expertise. MVP gunakan API.

---

## Referensi & Tanggal Akses
| Sumber | URL | Tanggal Akses |
|--------|-----|---------------|
| OpenAI Pricing | https://openai.com/api/pricing/ | Oktober 2024 |
| Anthropic Pricing | https://www.anthropic.com/pricing | Oktober 2024 |
| Bank Indonesia Kurs | https://www.bi.go.id/id/statistik/informasi-kurs/transaksi-bi/Default.aspx | Oktober 2024 |