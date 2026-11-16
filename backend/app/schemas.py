"""Pydantic schemas for M2 diagnosis API."""
from typing import Literal, Optional, List
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class DiagnosisAnalyzeRequest(BaseModel):
    """M2: Diagnosis analyze endpoint request (with optional vehicle context)."""
    symptom_text: str = Field(..., min_length=10, max_length=2000, description="Description of vehicle symptoms")
    vehicle_id: Optional[UUID] = Field(None, description="Saved vehicle ID (optional for new users)")
    vehicle_make: Optional[str] = Field(None, min_length=1, max_length=100, description="Vehicle brand if no saved vehicle")
    vehicle_model: Optional[str] = Field(None, min_length=1, max_length=100, description="Vehicle model")
    vehicle_year: Optional[int] = Field(None, ge=1900, le=2100, description="Vehicle year")


class RepairStepResponse(BaseModel):
    """Individual repair step."""
    step: int = Field(..., ge=1, description="1-based step number")
    description: str = Field(..., description="What to do in this step")


class RecommendationResponse(BaseModel):
    """Recommendation for parts/services."""
    model_config = ConfigDict(from_attributes=True)
    
    id: UUID
    part_name: str
    part_category: str
    part_description: Optional[str] = None
    estimated_cost: Optional[float] = None
    urgency: str
    priority: int
    shopee_affiliate_link: Optional[str] = None


class PartRecommendation(BaseModel):
    """Recommendation for a spare part with Shopee affiliate link."""
    part_id: UUID = Field(default_factory=UUID, description="Unique part identifier")
    part_name: str = Field(..., description="Name of the spare part")
    brand: str = Field(..., description="Brand/manufacturer")
    price_estimate: str = Field(..., description="Estimated price in IDR")
    shopee_affiliate_link: str = Field(..., description="Shopee affiliate URL")
    is_primary: bool = Field(default=False, description="Whether this is the primary recommendation")


class WorkshopRecommendation(BaseModel):
    """Recommendation for a workshop."""
    workshop_id: UUID = Field(default_factory=UUID, description="Unique workshop identifier")
    name: str = Field(..., description="Workshop name")
    address: str = Field(..., description="Street address")
    distance_km: float = Field(..., ge=0, description="Distance from user in km")
    rating: float = Field(..., ge=0, le=5, description="Average rating 0-5")
    phone: str = Field(..., description="Contact phone number")
    maps_url: str = Field(..., description="Google Maps URL")


class DiagnosisAnalyzeResponse(BaseModel):
    """M3: Diagnosis analyze endpoint response (conform to API spec v1)."""
    diagnosis_id: UUID
    conclusion: str = Field(..., description="Technical diagnosis explanation (final conclusion)")
    severity_level: Literal["DIY_EASY", "DIY_HARD", "WORKSHOP_REQUIRED"] = Field(
        ..., description="Severity level: DIY_EASY, DIY_HARD, WORKSHOP_REQUIRED"
    )
    confidence_score: float = Field(..., ge=0.0, le=1.0, description="Confidence 0.0-1.0")
    technical_explanation: str = Field(..., description="Detailed technical explanation")
    repair_steps: List[RepairStepResponse] = Field(default_factory=list, description="Step-by-step repair instructions")
    recommended_parts: List[PartRecommendation] = Field(default_factory=list, description="Recommended spare parts with Shopee links")
    recommended_workshops: List[WorkshopRecommendation] = Field(default_factory=list, description="Recommended workshops (may be empty if server not configured)")
