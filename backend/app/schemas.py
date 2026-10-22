"""Pydantic schemas for M2 diagnosis API."""
from typing import Optional, List
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
    step: int
    description: str


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


class DiagnosisAnalyzeResponse(BaseModel):
    """M2: Diagnosis analyze endpoint response."""
    diagnosis_id: UUID
    diagnosis: str = Field(..., description="Technical diagnosis explanation")
    severity: str = Field(..., description="Severity level: DIY_EASY, DIY_HARD, WORKSHOP_REQUIRED")
    confidence_score: float = Field(..., ge=0.0, le=1.0, description="Confidence 0.0-1.0")
    repair_steps: List[RepairStepResponse] = Field(default_factory=list, description="Step-by-step repair instructions")
    recommendations: List[RecommendationResponse] = Field(default_factory=list, description="Recommended spare parts")
