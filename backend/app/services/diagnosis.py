"""Diagnosis orchestration service."""
from typing import Optional
from uuid import UUID

from sqlalchemy.orm import Session
from sqlalchemy import select

from models import DiagnosticResult
from app.schemas import DiagnosisAnalyzeRequest, DiagnosisAnalyzeResponse, RepairStepResponse, PartRecommendation, WorkshopRecommendation
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
        db: Session,
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
        similar_symptoms = self.rag.search_similar_symptoms(
            db,
            request.symptom_text,
            top_k=5,
        )
        
        symptom_ids = [UUID(s["symptom_id"]) for s in similar_symptoms]
        
        # Step 3: Retrieve diagnosis context
        rag_context = self.rag.retrieve_diagnosis_context(db, symptom_ids, top_k=3)
        
        # Step 4: Call LLM for diagnosis
        llm_result = await self.llm.diagnose(
            symptom_text=request.symptom_text,
            vehicle_context=vehicle_context,
            rag_context=rag_context,
        )

        # Step 5: Store diagnosis result in DB
        # LLM returns keys: diagnosis, severity, confidence, repair_steps
        conclusion = llm_result.get("conclusion") or llm_result.get("diagnosis") or ""
        technical_explanation = llm_result.get("technical_explanation") or conclusion
        severity_level = llm_result.get("severity_level") or llm_result.get("severity") or "WORKSHOP_REQUIRED"
        confidence_score = llm_result.get("confidence_score", llm_result.get("confidence", 0.5))
        repair_steps = self._normalize_repair_steps(llm_result.get("repair_steps"))

        diagnostic_result = DiagnosticResult(
            symptom_text=request.symptom_text,
            diagnosis=conclusion,
            severity=severity_level,
            confidence_score=confidence_score,
            repair_steps=[s.model_dump() for s in repair_steps],
        )

        db.add(diagnostic_result)
        db.flush()

        # Step 6: Fetch and build recommendations
        recommended_parts = self._fetch_parts_recommendations(
            rag_context.get("spare_parts", [])[:5],
        )
        recommended_workshops = self._fetch_workshops_recommendations(
            rag_context.get("workshops", []),
        )

        # Step 7: Build response
        return DiagnosisAnalyzeResponse(
            diagnosis_id=diagnostic_result.id,
            conclusion=conclusion,
            severity_level=severity_level,
            confidence_score=confidence_score,
            technical_explanation=technical_explanation,
            repair_steps=repair_steps,
            recommended_parts=recommended_parts,
            recommended_workshops=recommended_workshops,
        )

    @staticmethod
    def _normalize_repair_steps(raw_steps) -> list:
        """Coerce LLM repair_steps into [{step:int, description:str}].

        ponytail: handles dicts and bare strings only; add nested/step-object
        variants if a real LLM starts emitting them.
        """
        normalized = []
        for idx, item in enumerate(raw_steps or [], 1):
            if isinstance(item, dict):
                description = item.get("description") or item.get("text") or ""
                step = item.get("step", idx)
                try:
                    step = int(step)
                except (TypeError, ValueError):
                    step = idx
            else:
                description, step = str(item), idx
            if description:
                normalized.append(RepairStepResponse(step=step, description=description))
        return normalized

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

    def _fetch_parts_recommendations(self, spare_parts: list) -> list:
        """Build PartRecommendation list from RAG spare parts context."""
        recommendations = []
        for idx, part in enumerate(spare_parts[:5], 1):
            recommendations.append(
                PartRecommendation(
                    part_id=UUID(int=idx),
                    part_name=part.get("part_name", "Unknown Part"),
                    brand=part.get("brand", "Generic"),
                    price_estimate=str(part.get("price_estimate", part.get("price_range", "0"))),
                    shopee_affiliate_link=part.get("shopee_affiliate_link", part.get("shopee_url", "")),
                    is_primary=(idx == 1),
                )
            )
        return recommendations

    def _fetch_workshops_recommendations(self, workshops: list) -> list:
        """Build WorkshopRecommendation list from RAG workshop context."""
        recommendations = []
        for idx, w in enumerate(workshops[:3], 1):
            recommendations.append(
                WorkshopRecommendation(
                    workshop_id=UUID(int=idx),
                    name=w.get("name", f"Bengkel {idx}"),
                    address=w.get("address", "-"),
                    distance_km=float(w.get("distance_km", 0)),
                    rating=float(w.get("rating", 0)),
                    phone=w.get("phone", "-"),
                    maps_url=w.get("maps_url", ""),
                )
            )
        return recommendations


def get_diagnosis_service(
    db: Session,
    rag_service: RAGService,
    llm_service: LLMService,
) -> DiagnosisService:
    """Dependency injection for diagnosis service."""
    return DiagnosisService(rag_service, llm_service)
