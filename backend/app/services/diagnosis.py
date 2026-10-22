"""Diagnosis orchestration service."""
from typing import Optional
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models import DiagnosticResult, Recommendation
from app.schemas import DiagnosisAnalyzeRequest, DiagnosisAnalyzeResponse, RepairStepResponse, RecommendationResponse
from app.services.rag import RAGService
from app.services.llm import LLMService


class DiagnosisService:
    """Orchestrate diagnosis pipeline: validate → RAG search → LLM → store result → fetch recommendations."""

    def __init__(self, rag_service: RAGService, llm_service: LLMService):
        """
        Initialize diagnosis service.
        
        Args:
            rag_service: RAG service for context retrieval
            llm_service: LLM service for diagnosis generation
        """
        self.rag = rag_service
        self.llm = llm_service

    async def analyze(
        self,
        db: AsyncSession,
        request: DiagnosisAnalyzeRequest,
    ) -> DiagnosisAnalyzeResponse:
        """
        Analyze symptom and generate diagnosis with recommendations.
        
        Args:
            db: Async database session
            request: DiagnosisAnalyzeRequest with symptom and vehicle info
            
        Returns:
            DiagnosisAnalyzeResponse with diagnosis, severity, repair steps, recommendations
        """
        # Step 1: Build vehicle context string
        vehicle_context = self._build_vehicle_context(request)
        
        # Step 2: RAG search for similar symptoms
        similar_symptoms = await self.rag.search_similar_symptoms(
            db,
            request.symptom_text,
            top_k=5,
        )
        
        symptom_ids = [UUID(s["symptom_id"]) for s in similar_symptoms]
        
        # Step 3: Retrieve diagnosis context
        rag_context = await self.rag.retrieve_diagnosis_context(db, symptom_ids, top_k=3)
        
        # Step 4: Call LLM for diagnosis
        llm_result = await self.llm.diagnose(
            symptom_text=request.symptom_text,
            vehicle_context=vehicle_context,
            rag_context=rag_context,
        )
        
        # Step 5: Store diagnosis result in DB
        diagnostic_result = DiagnosticResult(
            symptom_text=request.symptom_text,
            diagnosis=llm_result["diagnosis"],
            confidence_score=llm_result["confidence"],
            severity=llm_result["severity"],
            repair_steps=llm_result["repair_steps"],
        )
        
        db.add(diagnostic_result)
        await db.flush()
        
        # Step 6: Fetch and build recommendations
        recommendations = await self._fetch_recommendations(
            db,
            diagnostic_result.id,
            rag_context.get("spare_parts", [])[:5],
        )
        
        # Step 7: Build response
        repair_steps = [
            RepairStepResponse(step=s["step"], description=s["description"])
            for s in llm_result.get("repair_steps", [])
        ]
        
        return DiagnosisAnalyzeResponse(
            diagnosis_id=diagnostic_result.id,
            diagnosis=llm_result["diagnosis"],
            severity=llm_result["severity"],
            confidence_score=llm_result["confidence"],
            repair_steps=repair_steps,
            recommendations=recommendations,
        )

    def _build_vehicle_context(self, request: DiagnosisAnalyzeRequest) -> str:
        """Build human-readable vehicle context string."""
        if request.vehicle_id:
            # In production: fetch vehicle from DB
            return f"ID: {request.vehicle_id}"
        
        parts = []
        if request.vehicle_make:
            parts.append(request.vehicle_make)
        if request.vehicle_model:
            parts.append(request.vehicle_model)
        if request.vehicle_year:
            parts.append(f"({request.vehicle_year})")
        
        return " ".join(parts) or "Kendaraan tidak ditentukan"

    async def _fetch_recommendations(
        self,
        db: AsyncSession,
        diagnostic_result_id: UUID,
        spare_parts: list,
    ) -> list:
        """
        Fetch and build recommendation responses.
        
        Args:
            db: Async database session
            diagnostic_result_id: ID of diagnostic result
            spare_parts: List of spare part dicts from RAG context
            
        Returns:
            List of RecommendationResponse objects
        """
        recommendations = []
        
        for idx, part in enumerate(spare_parts[:5], 1):
            # In production: fetch actual Recommendation record from DB
            # For now: build from RAG context
            rec = RecommendationResponse(
                id=UUID(int=idx),  # Mock ID
                part_name=part.get("part_name", "Unknown Part"),
                part_category=part.get("category", "Accessories"),
                part_description=None,
                estimated_cost=float(part.get("price_range", "0").split("-")[0]),
                urgency="soon" if idx == 1 else "optional",
                priority=idx,
                shopee_affiliate_link=part.get("shopee_url"),
            )
            recommendations.append(rec)
        
        return recommendations


async def get_diagnosis_service(
    db: AsyncSession,
    rag_service: RAGService,
    llm_service: LLMService,
) -> DiagnosisService:
    """Dependency injection for diagnosis service."""
    return DiagnosisService(rag_service, llm_service)
