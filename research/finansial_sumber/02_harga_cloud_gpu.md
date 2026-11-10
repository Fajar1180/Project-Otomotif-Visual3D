# Sumber Data Harga Cloud GPU Instance — 2024

## Ringkasan Harga per Jam (USD) — AWS, GCP, DigitalOcean

| Provider | Instance Type | GPU | vCPU | RAM | Harga/Jam (USD) | Harga/Bulan* (USD) | Sumber |
|----------|---------------|-----|------|-----|-----------------|-------------------|--------|
| **AWS** | g5.xlarge | 1× A10G (24GB) | 4 | 16 GB | $1.006 | ~$734 | AWS EC2 Pricing |
| **AWS** | g5.2xlarge | 1× A10G (24GB) | 8 | 32 GB | $1.212 | ~$885 | AWS EC2 Pricing |
| **AWS** | g5.4xlarge | 1× A10G (24GB) | 16 | 64 GB | $1.624 | ~$1.185 | AWS EC2 Pricing |
| **AWS** | g6.xlarge | 1× H100 (80GB) | 4 | 32 GB | $2.500+ | ~$1.825+ | AWS EC2 Pricing (2024) |
| **AWS** | p3.2xlarge | 1× V100 (16GB) | 8 | 61 GB | $3.06 | ~$2.233 | AWS EC2 Pricing |
| **AWS** | p4d.24xlarge | 8× A100 (40GB) | 96 | 1.152 GB | $32.77 | ~$23.922 | AWS EC2 Pricing |
| **GCP** | n1-standard-4 + T4 | 1× T4 (16GB) | 4 | 15 GB | $0.35 + GPU | ~$255 + GPU | GCP Compute Engine |
| **GCP** | a2-highgpu-1g | 1× A100 (40GB) | 12 | 85 GB | $2.934 | ~$2.142 | GCP Compute Engine |
| **GCP** | a2-highgpu-2g | 2× A100 (80GB) | 24 | 170 GB | $5.868 | ~$4.284 | GCP Compute Engine |
| **DigitalOcean** | Basic GPU Droplet | 1× H100 (80GB) | 8 | 64 GB | $1.89 | ~$1.380 | DO Pricing 2024 |
| **DigitalOcean** | Professional GPU | 1× H100 (80GB) | 16 | 128 GB | $3.78 | ~$2.759 | DO Pricing 2024 |

*\*Bulan = 730 jam (24/7). Harga on-demand, tidak termasuk disk, network, tax.*

---

## Data Detail per Provider

### 1. AWS EC2 GPU Instances (US-East-1, On-Demand)
**Sumber:** https://aws.amazon.com/ec2/pricing/on-demand/ (akses Oktober 2024)

| Instance | GPU | vCPU | Memori | On-Demand $/jam | 1-Year Reserved* | 3-Year Reserved* |
|----------|-----|------|--------|-----------------|------------------|------------------|
| g5.xlarge | 1× NVIDIA A10G (24GB) | 4 | 16 GiB | $1.006 | $0.57 (-43%) | $0.38 (-62%) |
| g5.2xlarge | 1× NVIDIA A10G (24GB) | 8 | 32 GiB | $1.212 | $0.69 (-43%) | $0.46 (-62%) |
| g5.4xlarge | 1× NVIDIA A10G (24GB) | 16 | 64 GiB | $1.624 | $0.92 (-43%) | $0.61 (-62%) |
| g5.8xlarge | 1× NVIDIA A10G (24GB) | 32 | 128 GiB | $2.456 | $1.40 (-43%) | $0.93 (-62%) |
| g5.16xlarge | 1× NVIDIA A10G (24GB) | 64 | 256 GiB | $4.912 | $2.80 (-43%) | $1.86 (-62%) |
| g6.xlarge | 1× NVIDIA H100 (80GB) | 4 | 32 GiB | ~$2.50+ | - | - |
| p3.2xlarge | 1× NVIDIA V100 (16GB) | 8 | 61 GiB | $3.06 | $1.74 (-43%) | $1.16 (-62%) |
| p4d.24xlarge | 8× NVIDIA A100 (40GB) | 96 | 1.152 GiB | $32.77 | $18.65 (-43%) | $12.43 (-62%) |

*Reserved Instance: All Upfront payment.

**Catatan untuk Indonesia (ap-southeast-1 Jakarta / ap-southeast-3 Jakarta):**
- Harga Jakarta ~10-15% lebih mahal dari US-East-1
- g5.xlarge di Jakarta: ~$1.15/jam (~$840/bln)

---

### 2. Google Cloud Platform (GCP) GPU (us-central1, On-Demand)
**Sumber:** https://cloud.google.com/compute/gpus-pricing (akses Oktober 2024)

| GPU Type | Harga GPU/Jam | vCPU Minimum | Contoh Instance | Total $/jam (estimasi) |
|----------|---------------|--------------|-----------------|------------------------|
| NVIDIA T4 (16GB) | $0.095 | 2 vCPU | n1-standard-4 | $0.35 (instance) + $0.095 (GPU) = **$0.445** |
| NVIDIA T4 (16GB) | $0.095 | 4 vCPU | n1-standard-8 | $0.70 + $0.095 = **$0.795** |
| NVIDIA A100 (40GB) | $1.467 | 12 vCPU | a2-highgpu-1g | **$2.934** (termasuk instance) |
| NVIDIA A100 (80GB) | $2.367 | 24 vCPU | a2-highgpu-2g | **$5.868** |
| NVIDIA H100 (80GB) | $3.500+ | - | a3-highgpu-8g | **$28.00+** |

**Committed Use Discount (CUD):**
- 1 Tahun: -20% hingga -35%
- 3 Tahun: -40% hingga -55%

---

### 3. DigitalOcean GPU Droplets (NYC1/SFO3, On-Demand)
**Sumber:** https://www.digitalocean.com/pricing/gpu-droplets (akses Oktober 2024)

| Plan | GPU | vCPU | RAM | SSD | $/jam | $/bulan (730 jam) |
|------|-----|------|-----|-----|-------|-------------------|
| Basic GPU | 1× H100 (80GB) | 8 | 64 GB | 200 GB | $1.89 | $1.380 |
| Professional GPU | 1× H100 (80GB) | 16 | 128 GB | 400 GB | $3.78 | $2.759 |
| Enterprise GPU | 8× H100 (640GB) | 128 | 1 TB | 3.2 TB | $29.12 | $21.258 |

**Catatan:** DigitalOcean tidak memiliki region Jakarta (terdekat SGP1 Singapore). Latency ~40ms dari Indonesia.

---

### 4. RunPod / Lambda Labs / Vast.ai (Spot/Marketplace)
**Sumber:** https://www.runpod.io/pricing, https://lambdalabs.com/service/gpu-cloud, https://vast.ai/ (akses Oktober 2024)

| Provider | GPU | $/jam (Spot/Interruptible) | $/jam (On-Demand) | Catatan |
|----------|-----|----------------------------|-------------------|---------|
| RunPod | RTX 4090 (24GB) | $0.34 | $0.69 | Community cloud, no SLA |
| RunPod | RTX 3090 (24GB) | $0.25 | $0.49 | - |
| RunPod | A100 (40GB) | $0.79 | $1.64 | Secure cloud |
| RunPod | A100 (80GB) | $1.19 | $2.39 | Secure cloud |
| RunPod | H100 (80GB) | $2.69 | $4.89 | Secure cloud |
| Lambda Labs | RTX 4090 | - | $0.50 | Reserved instances available |
| Lambda Labs | A100 (40GB) | - | $1.10 | - |
| Lambda Labs | H100 (80GB) | - | $2.49 | - |
| Vast.ai | RTX 4090 | $0.15-0.30 | $0.40-0.60 | Bid-based, unreliable |

**Penting:** Provider ini **tidak memiliki SLA enterprise**, tidak cocok untuk production yang butuh uptime 99.9%. Cocok untuk training/inference batch non-kritis.

---

## Rekomendasi untuk Proposal

### Skema Cloud GPU yang Direkomendasikan

| Kebutuhan | Provider & Instance | Estimasi Bulanan (USD) | Estimasi Bulanan (Rp*) | Alasan |
|-----------|---------------------|------------------------|------------------------|--------|
| **Development + Inference Ringan** | DigitalOcean Basic GPU (H100) | $1.380 | **Rp 21.500.000** | Harga flat, billing per jam, region SG dekat Indo |
| **Production Inference (LLM 7B-13B)** | AWS g5.xlarge (A10G) Jakarta | $840 | **Rp 13.100.000** | SLA 99.9%, region Jakarta, A10G cocok LLM 7B-13B |
| **Production Inference (LLM 70B)** | AWS g5.4xlarge (A10G) Jakarta | $1.350 | **Rp 21.000.000** | VRAM 24GB cukup untuk 70B quantized (4-bit) |
| **Training / Fine-tuning** | RunPod A100 80GB (Spot) | $870 | **Rp 13.500.000** | Hemat 60% vs on-demand, toleran interrupt |

*\*Kurs: 1 USD = Rp 15.600 (kurs Bank Indonesia Oktober 2024 rata-rata).*

### Total Estimasi Cloud GPU 6 Bulan (Production Scenario)

| Skenario | Bulan 1-2 (Dev) | Bulan 3-6 (Prod) | Total 6 Bln (USD) | Total 6 Bln (Rp) |
|----------|-----------------|------------------|-------------------|------------------|
| **Minimal (DO Basic GPU 24/7)** | $2.760 | $5.520 | $8.280 | **Rp 129.000.000** |
| **Standar (AWS g5.xlarge Jakarta 24/7)** | $1.680 | $3.360 | $5.040 | **Rp 78.600.000** |
| **Hybrid (DO Dev + AWS Prod)** | $2.760 | $3.360 | $6.120 | **Rp 95.500.000** |

---

## Referensi Kurs USD/IDR
- **Bank Indonesia Kurs Tengah (Oktober 2024):** ~Rp 15.500 – 15.700 per USD
- **Sumber:** https://www.bi.go.id/id/statistik/informasi-kurs/transaksi-bi/Default.aspx
- **Digunakan untuk proposal:** **Rp 15.600 / USD** (rata-rata)