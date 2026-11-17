"""Diagnosis API routes."""
from __future__ import annotations

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.database import get_db
from models import DiagnosticResult
from app.schemas import DiagnosisAnalyzeRequest, DiagnosisAnalyzeResponse
from app.services.diagnosis import DiagnosisService
from app.services.rag import RAGService
from app.services.llm import LLMServiceFactory
from config import settings


router = APIRouter(prefix="/api/v1", tags=["diagnosis"])


@router.get("/diagnosis/history")
def diagnosis_history(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    severity: Optional[str] = None,
    db: Session = Depends(get_db),
) -> dict:
    """Stored diagnostic-result history (audit trail), newest first."""
    stmt = select(DiagnosticResult)
    if severity:
        stmt = stmt.where(DiagnosticResult.severity == severity)
    total = db.execute(select(func.count()).select_from(stmt.subquery())).scalar_one()
    rows = (
        db.execute(
            stmt.order_by(DiagnosticResult.created_at.desc())
            .offset((page - 1) * limit)
            .limit(limit)
        )
        .scalars()
        .all()
    )

    def _row(r) -> dict:
        sev = r.severity
        return {
            "diagnosis_id": str(r.id),
            "vehicle_id": r.vehicle_id,
            "conclusion": r.diagnosis,
            "severity_level": sev.value if hasattr(sev, "value") else sev,
            "confidence_score": r.confidence_score,
            "created_at": r.created_at.isoformat() if r.created_at else None,
        }

    return {"data": [_row(r) for r in rows], "meta": {"total": total, "page": page, "limit": limit}}


@router.post("/diagnosis/analyze", response_model=DiagnosisAnalyzeResponse)
async def analyze_diagnosis(
    request: DiagnosisAnalyzeRequest,
    db: Session = Depends(get_db),
) -> DiagnosisAnalyzeResponse:
    """
    Analyze vehicle symptoms and return AI diagnosis with recommendations.

    **Request:**
    - `symptom_text`: Description of vehicle symptoms (10-2000 chars)
    - `vehicle_id`: Optional saved vehicle UUID
    - `vehicle_make`, `vehicle_model`, `vehicle_year`: Optional for new vehicles

    **Response:**
    - `diagnosis_id`: UUID of stored diagnostic result
    - `conclusion`: Technical diagnosis explanation
    - `severity_level`: DIY_EASY | DIY_HARD | WORKSHOP_REQUIRED
    - `confidence_score`: 0.0-1.0
    - `technical_explanation`: Detailed technical explanation
    - `repair_steps`: List of step-by-step instructions
    - `recommended_parts`: Recommended spare parts with Shopee links
    - `recommended_workshops`: Recommended workshops

    **Performance:** Target <500ms (95th percentile)

    **Error Codes:**
    - 422: Validation error (invalid symptom_text length, vehicle year)
    - 500: LLM or database error
    """
    try:
        rag_service = RAGService()
        llm_service = LLMServiceFactory.create(
            api_key=settings.openai_api_key if hasattr(settings, "openai_api_key") else None,
            mock=True,
        )
        diagnosis_service = DiagnosisService(rag_service, llm_service)

        result = await diagnosis_service.analyze(db, request)
        db.commit()
        return result
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        # Log error to server log, do not expose details to client
        import logging
        logging.getLogger(__name__).error(f"Diagnosis error: {str(e)}")
        raise HTTPException(status_code=500, detail="Diagnosis failed. Silakan coba lagi nanti.")
