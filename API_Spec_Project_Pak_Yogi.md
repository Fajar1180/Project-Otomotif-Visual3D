# API Specification (OpenAPI 3.0)
## Platform Otomotif AI (Project Pak Yogi)

### Base Information
- **Base URL:** `https://api.otomotif-ai.com/api/v1`
- **Authentication:** Bearer Token (JWT)
- **Content-Type:** `application/json`
- **Rate Limit:** 100 requests/hour/IP

---

### Authentication Endpoints

#### POST /auth/register
Register a new user account.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securePassword123",
  "full_name": "John Doe",
  "vehicle_id": "uuid-optional"
}
```

**Response (201):**
```json
{
  "user": {
    "id": "uuid",
    "email": "user@example.com",
    "full_name": "John Doe",
    "vehicle_id": "uuid-optional",
    "created_at": "2026-10-19T10:00:00Z"
  },
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer",
  "expires_in": 86400
}
```

#### POST /auth/login
Authenticate user and return tokens.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

**Response (200):** Same structure as register.

#### POST /auth/refresh
Refresh access token using refresh token.

**Request Body:**
```json
{
  "refresh_token": "eyJhbGciOiJIUzI1NiIs..."
}
```

**Response (200):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer",
  "expires_in": 86400
}
```

---

### Vehicle Endpoints

#### GET /vehicles
List all available vehicle models.

**Query Parameters:**
- `brand` (optional): Filter by brand (e.g., "Honda", "Yamaha")
- `category` (optional): Filter by category (matic, sport, cub, car)
- `year` (optional): Filter by year
- `page` (default: 1), `limit` (default: 20)

**Response (200):**
```json
{
  "data": [
    {
      "id": "uuid",
      "brand": "Honda",
      "model": "Vario 150",
      "year_start": 2015,
      "year_end": 2023,
      "category": "matic"
    }
  ],
  "meta": {
    "total": 150,
    "page": 1,
    "limit": 20,
    "total_pages": 8
  }
}
```

#### GET /vehicles/{id}
Get vehicle details by ID.

**Response (200):**
```json
{
  "id": "uuid",
  "brand": "Honda",
  "model": "Vario 150",
  "year_start": 2015,
  "year_end": 2023,
  "category": "matic"
}
```

---

### Diagnosis Endpoints

#### POST /diagnosis/analyze
Analyze user's vehicle issue description and return diagnosis.

**Headers:** `Authorization: Bearer <access_token>`

**Request Body:**
```json
{
  "user_story": "Motor Vario saya kalau pagi susah banget di-stater, klakson agak sember...",
  "vehicle_id": "uuid-vario-150"
}
```

**Response (200):**
```json
{
  "diagnosis_id": "uuid-diag-123",
  "conclusion": "Kerusakan terindikasi pada sistem kelistrikan (Aki tekor).",
  "severity_level": "DIY_EASY",
  "confidence_score": 0.92,
  "technical_explanation": "Gejala starter berat pagi hari dan klakson lemah mengindikasikan tegangan aki turun...",
  "repair_steps": [
    "Buka cover depan motor",
    "Lepas kutub negatif (-) terlebih dahulu",
    "Lepas kutub positif (+)",
    "Ganti aki dengan spesifikasi yang sama",
    "Pasang kutub positif (+) lalu negatif (-)",
    "Tutup cover dan test starter"
  ],
  "recommended_parts": [
    {
      "part_id": "uuid-part-1",
      "part_name": "Aki Kering GS Astra GTZ6V",
      "brand": "GS Battery",
      "price_estimate": "Rp 230.000 - Rp 270.000",
      "shopee_affiliate_link": "https://shp.ee/xyz123",
      "is_primary": true
    }
  ],
  "recommended_workshops": []
}
```

**Response (200) - WORKSHOP_REQUIRED:**
```json
{
  "diagnosis_id": "uuid-diag-456",
  "conclusion": "Kerusakan mesin (kompresi rendah, mungkin piston/ring aus).",
  "severity_level": "WORKSHOP_REQUIRED",
  "confidence_score": 0.88,
  "technical_explanation": "...",
  "repair_steps": [
    "Perlu peralatan khusus (kompresi tester, torque wrench)",
    "Disarankan ke bengkel profesional"
  ],
  "recommended_parts": [
    {
      "part_id": "uuid-part-2",
      "part_name": "Set Piston & Ring Honda Vario 150",
      "brand": "OEM",
      "price_estimate": "Rp 450.000 - Rp 600.000",
      "shopee_affiliate_link": "https://shp.ee/abc456",
      "is_primary": true
    }
  ],
  "recommended_workshops": [
    {
      "workshop_id": "uuid-ws-1",
      "name": "Bengkel Pak Yogi Jaya",
      "address": "Jl. Raya No. 123, Bandung",
      "distance_km": 2.3,
      "rating": 4.8,
      "specialties": ["matic", "sport"],
      "phone": "022-1234567",
      "maps_url": "https://maps.google.com/?q=-6.9175,107.6191"
    }
  ]
}
```

#### GET /diagnosis/history
Get user's diagnosis history.

**Headers:** `Authorization: Bearer <access_token>`

**Query Parameters:** `page`, `limit`, `severity`

**Response (200):**
```json
{
  "data": [
    {
      "diagnosis_id": "uuid-diag-123",
      "vehicle_id": "uuid-vario-150",
      "conclusion": "Kerusakan terindikasi pada sistem kelistrikan (Aki tekor).",
      "severity_level": "DIY_EASY",
      "created_at": "2026-10-19T10:30:00Z"
    }
  ],
  "meta": { "total": 5, "page": 1, "limit": 10 }
}
```

---

### 3D Configurator Endpoints

#### POST /3d/generate
Upload vehicle photos to generate base 3D mesh.

**Headers:** `Authorization: Bearer <access_token>`
**Content-Type:** `multipart/form-data`

**Form Data:**
- `images[]` (4 files, required): Front, back, left, right photos
- `vehicle_brand` (string, required): e.g., "Honda"
- `vehicle_model` (string, required): e.g., "Vario 150"

**Response (202):**
```json
{
  "task_id": "celery-task-999",
  "status": "processing",
  "message": "3D construction is running in background",
  "estimated_time_seconds": 120
}
```

#### GET /3d/status/{task_id}
Check 3D generation status.

**Headers:** `Authorization: Bearer <access_token>`

**Response (200):**
```json
{
  "task_id": "celery-task-999",
  "status": "completed",
  "mesh_url": "https://cdn.otomotif-ai.com/meshes/uuid-vario-150.glb",
  "texture_url": "https://cdn.otomotif-ai.com/textures/uuid-vario-150.png",
  "metadata": {
    "vertices": 45000,
    "faces": 90000,
    "texture_resolution": "1024x1024"
  }
}
```

#### POST /3d/modify
Apply component modification to existing mesh.

**Headers:** `Authorization: Bearer <access_token>`
**Content-Type:** `application/json`

**Request Body:**
```json
{
  "base_mesh_id": "uuid-vario-150",
  "modifications": [
    {
      "component_type": "wheels",
      "part_id": "uuid-part-wheels-1",
      "parameters": {
        "size": 17,
        "offset": 5
      }
    }
  ]
}
```

**Response (200):**
```json
{
  "modified_mesh_url": "https://cdn.otomotif-ai.com/meshes/uuid-vario-150-mod.glb",
  "modification_id": "uuid-mod-789",
  "affiliate_links": [
    {
      "part_id": "uuid-part-wheels-1",
      "shopee_affiliate_link": "https://shp.ee/wheel123"
    }
  ]
}
```

---

### Workshop Endpoints

#### GET /workshops
Find nearby workshops.

**Headers:** `Authorization: Bearer <access_token>` (optional for public access)

**Query Parameters:**
- `lat` (required): User latitude
- `lng` (required): User longitude
- `radius_km` (default: 25): Search radius
- `specialty` (optional): Filter by vehicle category
- `min_rating` (default: 4.0): Minimum rating

**Response (200):**
```json
{
  "data": [
    {
      "id": "uuid-ws-1",
      "name": "Bengkel Pak Yogi Jaya",
      "address": "Jl. Raya No. 123, Bandung",
      "latitude": -6.9175,
      "longitude": 107.6191,
      "distance_km": 2.3,
      "rating": 4.8,
      "specialties": ["matic", "sport"],
      "phone": "022-1234567",
      "maps_url": "https://maps.google.com/?q=-6.9175,107.6191"
    }
  ],
  "meta": { "total": 15 }
}
```

---

### Error Responses

All endpoints may return these error formats:

**400 Bad Request:**
```json
{
  "error": "VALIDATION_ERROR",
  "message": "Invalid request payload",
  "details": [
    { "field": "email", "message": "Invalid email format" }
  ]
}
```

**401 Unauthorized:**
```json
{
  "error": "UNAUTHORIZED",
  "message": "Invalid or expired token"
}
```

**404 Not Found:**
```json
{
  "error": "NOT_FOUND",
  "message": "Resource not found"
}
```

**429 Too Many Requests:**
```json
{
  "error": "RATE_LIMITED",
  "message": "Rate limit exceeded. Try again in 60 seconds.",
  "retry_after": 60
}
```

**500 Internal Server Error:**
```json
{
  "error": "INTERNAL_ERROR",
  "message": "An unexpected error occurred",
  "request_id": "req-uuid-for-debugging"
}
```

---
*Document Version 1.0 | Created: 2026-10-19*