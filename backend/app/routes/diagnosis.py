"""Diagnosis API routes."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas import DiagnosisAnalyzeRequest, DiagnosisAnalyzeResponse
from app.services.diagnosis import DiagnosisService
from app.services.rag import RAGService
from app.services.llm import LLMServiceFactory
from config import settings


router = APIRouter(prefix="/api/v1", tags=["diagnosis"])


@router.post("/diagnosis/analyze", response_model=DiagnosisAnalyzeResponse)
async def analyze_diagnosis(
    request: DiagnosisAnalyzeRequest,
    db: AsyncSession = Depends(get_db),
) -> DiagnosisAnalyzeResponse:
    """
    Analyze vehicle symptoms and return AI diagnosis with recommendations.
    
    **Request:**
    - `symptom_text`: Description of vehicle symptoms (10-2000 chars)
    - `vehicle_id`: Optional saved vehicle UUID
    - `vehicle_make`, `vehicle_model`, `vehicle_year`: Optional for new vehicles
    
    **Response:**
    - `diagnosis_id`: UUID of stored diagnostic result
    - `diagnosis`: Technical diagnosis explanation
    - `severity`: DIY_EASY | DIY_HARD | WORKSHOP_REQUIRED
    - `confidence_score`: 0.0-1.0
    - `repair_steps`: List of step-by-step instructions
    - `recommendations`: Recommended spare parts with Shopee links
    
    **Performance:** Target <500ms (95th percentile)
    
    **Error Codes:**
    - 422: Validation error (invalid symptom_text length, vehicle year)
    - 500: LLM or database error
    """
    try:
        # Initialize services
        rag_service = RAGService()
        llm_service = LLMServiceFactory.create(
            api_key=settings.openai_api_key if hasattr(settings, 'openai_api_key') else None,
            mock=not settings.debug,  # Mock in production for cost control
        )
        diagnosis_service = DiagnosisService(rag_service, llm_service)
        
        # Analyze
        result = await diagnosis_service.analyze(db, request)
        
        # Commit to DB
        await db.commit()
        
        return result
        
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"Diagnosis failed: {str(e)}")
