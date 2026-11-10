# Sumber Data Harga Managed Database — PostgreSQL & Redis (Oktober 2024)

## Ringkasan Harga Bulanan (USD)

| Provider | Service | Spec | Harga/Bulan (USD) | Harga/Bulan (Rp*) | Free Tier | Sumber |
|----------|---------|------|-------------------|-------------------|-----------|--------|
| **Supabase** | PostgreSQL (Pro) | 8 GB RAM, 100 GB SSD, 2 vCPU | $25 | Rp 390.000 | 500 MB, 1 GB RAM | Supabase Pricing |
| **Supabase** | PostgreSQL (Team) | 16 GB RAM, 200 GB SSD, 4 vCPU | $599 | Rp 9.344.400 | - | Supabase Pricing |
| **Neon** | PostgreSQL (Scale) | 4 GB RAM, 50 GB Storage | $19 | Rp 296.400 | 0.5 GB, 10 GB storage | Neon Pricing |
| **Neon** | PostgreSQL (Business) | 16 GB RAM, 500 GB Storage | $189 | Rp 2.948.400 | - | Neon Pricing |
| **AWS RDS** | db.t3.medium (Multi-AZ) | 2 vCPU, 4 GB RAM, 100 GB | $78 | Rp 1.216.800 | 750 jam db.t3.micro | AWS RDS Pricing |
| **AWS RDS** | db.r6g.large (Multi-AZ) | 2 vCPU, 16 GB RAM, 100 GB | $195 | Rp 3.042.000 | - | AWS RDS Pricing |
| **Google Cloud SQL** | db-custom-2-8192 (HA) | 2 vCPU, 8 GB RAM, 100 GB | $85 | Rp 1.326.000 | - | GCP SQL Pricing |
| **DigitalOcean** | Managed PostgreSQL | 2 GB RAM, 1 vCPU, 30 GB SSD | $15 | Rp 234.000 | - | DO Database Pricing |
| **DigitalOcean** | Managed PostgreSQL | 4 GB RAM, 2 vCPU, 60 GB SSD | $30 | Rp 468.000 | - | DO Database Pricing |

*\*Kurs: Rp 15.600/USD*

---

## Data Detail per Provider

### 1. Supabase (PostgreSQL + Auth + Realtime + Storage)
**Sumber:** https://supabase.com/pricing (akses Oktober 2024)

| Plan | Database | Auth | Realtime | Storage | Bandwidth | Harga/Bulan |
|------|----------|------|----------|---------|-----------|-------------|
| **Free** | 500 MB, 1 GB RAM, 1 vCPU | 50K MAU | 200 concurrent | 1 GB | 2 GB | $0 |
| **Pro** | 8 GB RAM, 100 GB SSD, 2 vCPU | 100K MAU | 500 concurrent | 100 GB | 500 GB | **$25** |
| **Team** | 16 GB RAM, 200 GB SSD, 4 vCPU | 500K MAU | 2K concurrent | 500 GB | 2 TB | **$599** |
| **Enterprise** | Custom | Custom | Custom | Custom | Custom | Custom |

**Fitur Termasuk Pro:**
- Point-in-time recovery (7 hari)
- Daily backups (retained 30 hari)
- Read replicas (1 included)
- pgvector extension (AI/embedding)
- PostGIS extension (spatial)
- Logs & metrics 30 hari
- Email support (4 jam response)

**Tambahan:**
- Database size >100 GB: $0.10/GB/bln
- Bandwidth >500 GB: $0.10/GB
- Extra read replica: $10/bln
- PITR retention >7 hari: $0.03/GB/bln

---

### 2. Neon (Serverless PostgreSQL)
**Sumber:** https://neon.tech/pricing (akses Oktober 2024)

| Plan | Compute | Storage | Branch | PITR | Harga/Bulan |
|------|---------|---------|--------|------|-------------|
| **Free** | 0.5 GB RAM, 0.25 vCPU | 10 GB | 10 | 1 hari | $0 |
| **Scale** | 4 GB RAM, 2 vCPU (auto-scale) | 50 GB | 50 | 7 hari | **$19** |
| **Business** | 16 GB RAM, 8 vCPU (auto-scale) | 500 GB | Unlimited | 30 hari | **$189** |
| **Enterprise** | Custom | Custom | Custom | Custom | Custom |

**Keunggulan Neon:**
- Auto-scale to zero (tidak ada biaya saat idle)
- Branching database (git-like untuk preview deploy)
- Pay per second compute
- Serverless — cocok untuk workload intermittent

**Kekurangan:**
- Cold start ~500ms-2s saat scale from zero
- Connection pooling via PgBouncer (built-in)
- Region: US-East, EU-West, AP-Southeast (Singapore) — tidak ada Jakarta

---

### 3. AWS RDS for PostgreSQL (ap-southeast-3 Jakarta)
**Sumber:** https://aws.amazon.com/rds/postgresql/pricing/ (akses Oktober 2024, region Jakarta)

| Instance Class | vCPU | RAM | On-Demand $/jam | 1-Yr Reserved $/jam | Multi-AZ On-Demand $/jam |
|----------------|------|-----|-----------------|---------------------|--------------------------|
| db.t3.micro | 2 | 1 GiB | $0.021 | $0.012 | $0.042 |
| db.t3.small | 2 | 2 GiB | $0.042 | $0.024 | $0.084 |
| db.t3.medium | 2 | 4 GiB | $0.084 | $0.048 | **$0.168** |
| db.t3.large | 2 | 8 GiB | $0.168 | $0.096 | $0.336 |
| db.r6g.large | 2 | 16 GiB | $0.210 | $0.120 | **$0.420** |
| db.r6g.xlarge | 4 | 32 GiB | $0.420 | $0.240 | $0.840 |

**Storage (GP3 SSD):** $0.115 / GB / bln
**Backup Storage:** $0.023 / GB / bln (free tier = DB size)
**Data Transfer:** $0.09 / GB (keluar ke internet)

**Contoh Estimasi Bulanan (730 jam, Multi-AZ, 100 GB GP3):**
| Instance | Compute | Storage (100 GB) | Backup (100 GB) | Total/bln (USD) | Total/bln (Rp) |
|----------|---------|------------------|-----------------|-----------------|----------------|
| db.t3.medium | $122.64 | $11.50 | $2.30 | **$136.44** | **Rp 2.128.464** |
| db.r6g.large | $306.60 | $11.50 | $2.30 | **$320.40** | **Rp 4.998.240** |

---

### 4. Google Cloud SQL for PostgreSQL (asia-southeast1 Singapore)
**Sumber:** https://cloud.google.com/sql/pricing (akses Oktober 2024)

| Machine Type | vCPU | RAM | On-Demand $/jam | 1-Yr CUD $/jam | HA (2x) $/jam |
|--------------|------|-----|-----------------|----------------|---------------|
| db-custom-1-3840 | 1 | 3.75 GB | $0.049 | $0.031 | $0.098 |
| db-custom-2-8192 | 2 | 8 GB | $0.104 | $0.066 | **$0.208** |
| db-custom-4-16384 | 4 | 16 GB | $0.208 | $0.132 | $0.416 |

**Storage (SSD):** $0.170 / GB / bln
**Backup:** $0.08 / GB / bln
**Network Egress:** $0.12 / GB (ke internet)

**Contoh Bulanan (HA, 100 GB SSD):**
- db-custom-2-8192: $151.84 + $17 + $8 = **$176.84/bln** → **Rp 2.758.704**

---

### 5. DigitalOcean Managed Databases (SGP1 Singapore)
**Sumber:** https://www.digitalocean.com/pricing/managed-databases (akses Oktober 2024)

| Plan | vCPU | RAM | SSD | Standby Node | Harga/Bulan | Harga/Bulan (Rp) |
|------|------|-----|-----|--------------|-------------|------------------|
| **Basic** | 1 | 1 GB | 10 GB | No | $15 | Rp 234.000 |
| **Standard** | 1 | 2 GB | 30 GB | No | $30 | Rp 468.000 |
| **Standard** | 2 | 4 GB | 60 GB | No | $60 | Rp 936.000 |
| **Standard** | 2 | 8 GB | 120 GB | **Yes (HA)** | $120 | Rp 1.872.000 |
| **Performance** | 4 | 16 GB | 240 GB | **Yes (HA)** | $240 | Rp 3.744.000 |
| **Performance** | 8 | 32 GB | 480 GB | **Yes (HA)** | $480 | Rp 7.488.000 |

**Fitur Termasuk:**
- Automated daily backups (7 hari retention, gratis)
- Point-in-time recovery
- Read replicas (tambahan $15/bln per replica)
- Private networking
- SSL enforcement
- Metrics & alerting

---

### 6. Redis Managed Services

| Provider | Plan | Spec | Harga/Bulan (USD) | Harga/Bulan (Rp) | Sumber |
|----------|------|------|-------------------|------------------|--------|
| **Redis Cloud (Redis Inc.)** | Free | 30 MB, 1 DB | $0 | Rp 0 | Redis Cloud Pricing |
| **Redis Cloud** | Essentials | 1 GB, 1 DB, 30K ops/s | $14 | Rp 218.400 | Redis Cloud Pricing |
| **Redis Cloud** | Pro | 3 GB, 5 DB, 100K ops/s | $49 | Rp 764.400 | Redis Cloud Pricing |
| **AWS ElastiCache** | cache.t3.micro | 0.55 GB, 1 vCPU | $18.40 | Rp 287.040 | AWS ElastiCache Pricing |
| **AWS ElastiCache** | cache.t3.small | 1.3 GB, 2 vCPU | $36.80 | Rp 574.080 | AWS ElastiCache Pricing |
| **AWS ElastiCache** | cache.r6g.large | 13.07 GB, 2 vCPU | $186.00 | Rp 2.901.600 | AWS ElastiCache Pricing |
| **GCP Memorystore** | Basic Tier | 1 GB, HA | $45 | Rp 702.000 | GCP Memorystore Pricing |
| **GCP Memorystore** | Standard Tier | 5 GB, HA | $225 | Rp 3.510.000 | GCP Memorystore Pricing |
| **DigitalOcean** | Managed Redis | 1 GB, 1 vCPU, HA | $15 | Rp 234.000 | DO Redis Pricing |
| **DigitalOcean** | Managed Redis | 4 GB, 2 vCPU, HA | $60 | Rp 936.000 | DO Redis Pricing |

---

## Rekomendasi untuk Proposal (MVP → Production)

### MVP (Bulan 1-3): Supabase Free Tier + DigitalOcean Redis
| Komponen | Provider | Plan | Cost/Bulan |
|----------|----------|------|------------|
| PostgreSQL | Supabase | **Free** (500 MB, 1 GB RAM) | **$0** |
| Redis | DigitalOcean | **Basic 1 GB HA** | **$15** (Rp 234.000) |
| **Total** | | | **Rp 234.000/bln** |

### Early Production (Bulan 4-6): Supabase Pro + DO Redis Standard
| Komponen | Provider | Plan | Cost/Bulan |
|----------|----------|------|------------|
| PostgreSQL | Supabase | **Pro** (8 GB RAM, 100 GB) | **$25** (Rp 390.000) |
| Redis | DigitalOcean | **Standard 4 GB HA** | **$60** (Rp 936.000) |
| **Total** | | | **Rp 1.326.000/bln** |

### Scale (Bulan 7+): Neon Business + Redis Cloud Pro
| Komponen | Provider | Plan | Cost/Bulan |
|----------|----------|------|------------|
| PostgreSQL | Neon | **Business** (16 GB, 500 GB) | **$189** (Rp 2.948.400) |
| Redis | Redis Cloud | **Pro** (3 GB, 100K ops/s) | **$49** (Rp 764.400) |
| **Total** | | | **Rp 3.712.800/bln** |

---

## Catatan Penting untuk Proposal

1. **Region:** Supabase & Neon region terdekat = **Singapore** (latency ~30-50ms dari Indonesia). AWS RDS & GCP SQL punya **Jakarta** (latency <10ms) tapi lebih mahal.
2. **PostGIS:** Supabase & Neon & AWS RDS & GCP SQL **semua support PostGIS** untuk spatial query bengkel nearby.
3. **pgvector:** Supabase & Neon & AWS RDS (PG 16+) & GCP SQL support pgvector untuk embedding search.
4. **Backup & PITR:** Semua managed service include automated backup. Supabase Pro = 7 hari PITR, Neon Scale = 7 hari, AWS RDS = 35 hari.
5. **Connection Pooling:** Supabase (PgBouncer built-in), Neon (PgBouncer built-in), AWS RDS (RDS Proxy $0.015/jam), DigitalOcean (built-in).

---

## Referensi & Tanggal Akses
| Sumber | URL | Tanggal Akses |
|--------|-----|---------------|
| Supabase Pricing | https://supabase.com/pricing | Oktober 2024 |
| Neon Pricing | https://neon.tech/pricing | Oktober 2024 |
| AWS RDS Pricing | https://aws.amazon.com/rds/postgresql/pricing/ | Oktober 2024 |
| GCP Cloud SQL Pricing | https://cloud.google.com/sql/pricing | Oktober 2024 |
| DigitalOcean Databases | https://www.digitalocean.com/pricing/managed-databases | Oktober 2024 |
| Redis Cloud Pricing | https://redis.io/cloud/pricing/ | Oktober 2024 |
| AWS ElastiCache Pricing | https://aws.amazon.com/elasticache/pricing/ | Oktober 2024 |
| GCP Memorystore Pricing | https://cloud.google.com/memorystore/pricing | Oktober 2024 |
| Bank Indonesia Kurs | https://www.bi.go.id/id/statistik/informasi-kurs/transaksi-bi/Default.aspx | Oktober 2024 |