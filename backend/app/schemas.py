"""Pydantic schemas for API contracts and validation."""
from datetime import datetime
from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


# User schemas
class UserCreate(BaseModel):
    """User registration request."""
    email: EmailStr
    password: str = Field(..., min_length=8)
    full_name: str = Field(..., min_length=2, max_length=255)
    phone: Optional[str] = None


class UserResponse(BaseModel):
    """User response (no password)."""
    id: UUID
    email: str
    full_name: str
    phone: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Vehicle schemas
class VehicleCreate(BaseModel):
    """Create vehicle request."""
    make: str = Field(..., min_length=1, max_length=100)
    model: str = Field(..., min_length=1, max_length=100)
    year: int = Field(..., ge=1900, le=2100)
    color: Optional[str] = None
    vin: Optional[str] = None
    mileage: Optional[int] = None
    notes: Optional[str] = None


class VehicleResponse(BaseModel):
    """Vehicle response."""
    id: UUID
    user_id: UUID
    make: str
    model: str
    year: int
    color: Optional[str]
    vin: Optional[str]
    mileage: Optional[int]
    notes: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Diagnostic result schemas
class DiagnosticCreate(BaseModel):
    """AI diagnosis request."""
    vehicle_id: UUID
    symptom_text: str = Field(..., min_length=10, max_length=2000)


class DiagnosticResponse(BaseModel):
    """AI diagnosis response."""
    id: UUID
    vehicle_id: UUID
    symptom_text: str
    diagnosis: str
    confidence_score: float
    severity: str
    repair_steps: Optional[List[dict]]
    created_at: datetime

    class Config:
        from_attributes = True


# Recommendation schemas
class RecommendationResponse(BaseModel):
    """Recommendation for parts/services."""
    id: UUID
    part_name: str
    part_category: str
    part_description: Optional[str]
    estimated_cost: Optional[float]
    urgency: str
    priority: int
    shopee_affiliate_link: Optional[str]

    class Config:
        from_attributes = True


class DiagnosticDetailResponse(DiagnosticResponse):
    """Diagnostic result with recommendations."""
    recommendations: List[RecommendationResponse]

    class Config:
        from_attributes = True


# Workshop schemas
class WorkshopResponse(BaseModel):
    """Workshop finder response."""
    id: UUID
    name: str
    address: str
    latitude: float
    longitude: float
    phone: Optional[str]
    specialties: Optional[List[str]]
    rating: Optional[float]
    review_count: int
    website: Optional[str]

    class Config:
        from_attributes = True


# Error response
class ErrorResponse(BaseModel):
    """Standard error response."""
    detail: str
    error_code: Optional[str] = None
