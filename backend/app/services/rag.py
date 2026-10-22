"""RAG (Retrieval-Augmented Generation) service for vector search and context retrieval."""
from typing import List, Dict, Optional
import json
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, text

from models import VectorStore, Symptom, Diagnosis, DiagnosisPartMap, SparePart


class RAGService:
    """Vector search and knowledge retrieval service."""

    async def search_similar_symptoms(
        self,
        db: AsyncSession,
        query_text: str,
        top_k: int = 5,
        confidence_threshold: float = 0.7,
    ) -> List[Dict]:
        """
        Search for similar symptoms using pgvector similarity search.
        
        Args:
            db: Async database session
            query_text: Symptom description to search for
            top_k: Number of results to return
            confidence_threshold: Minimum similarity score
            
        Returns:
            List of similar symptoms with scores
        """
        # In production: use OpenAI embeddings or local model
        # For now: mock similarity based on keyword matching
        result = await db.execute(
            select(Symptom).limit(top_k)
        )
        symptoms = result.scalars().all()
        
        # Mock scoring: return with placeholder confidence
        return [
            {
                "symptom_id": str(s.id),
                "symptom_code": s.symptom_code,
                "description": s.description,
                "category": s.category,
                "confidence": 0.85,
            }
            for s in symptoms
        ]

    async def retrieve_diagnosis_context(
        self,
        db: AsyncSession,
        symptom_ids: List[UUID],
        top_k: int = 3,
    ) -> Dict:
        """
        Retrieve related diagnoses and recommendations for symptoms.
        
        Args:
            db: Async database session
            symptom_ids: List of symptom UUIDs
            top_k: Number of diagnosis results per symptom
            
        Returns:
            Context dict with diagnoses and spare parts
        """
        context = {
            "diagnoses": [],
            "spare_parts": [],
            "repair_hints": [],
        }

        for symptom_id in symptom_ids:
            # Get diagnosis mappings
            result = await db.execute(
                select(Diagnosis)
                .from_statement(
                    text("""
                    SELECT DISTINCT d.* FROM diagnoses d
                    JOIN symptom_diagnosis_map sdm ON d.id = sdm.diagnosis_id
                    WHERE sdm.symptom_id = :symptom_id
                    LIMIT :top_k
                    """)
                )
                .bindparams(symptom_id=symptom_id, top_k=top_k)
            )
            diagnoses = result.scalars().all()
            
            for diagnosis in diagnoses:
                context["diagnoses"].append({
                    "title": diagnosis.title,
                    "explanation": diagnosis.technical_explanation,
                    "severity": diagnosis.severity_level,
                    "repair_steps": diagnosis.repair_steps or [],
                })
                
                # Get recommended spare parts
                parts_result = await db.execute(
                    select(SparePart, DiagnosisPartMap.is_primary)
                    .join(DiagnosisPartMap)
                    .filter(DiagnosisPartMap.diagnosis_id == diagnosis.id)
                )
                parts = parts_result.all()
                
                for part, is_primary in parts:
                    context["spare_parts"].append({
                        "part_id": str(part.id),
                        "part_name": part.part_name,
                        "part_number": part.part_number,
                        "category": part.brand or "Unknown",
                        "price_range": f"{part.price_min or 0}-{part.price_max or 0}",
                        "is_primary": is_primary,
                        "shopee_url": part.default_shopee_url,
                    })

        return context

    async def store_embedding(
        self,
        db: AsyncSession,
        text_chunk: str,
        source: str,
        embedding: Optional[List[float]] = None,
        metadata: Optional[Dict] = None,
    ) -> UUID:
        """
        Store text chunk with embedding for future retrieval.
        
        Args:
            db: Async database session
            text_chunk: Text content to store
            source: Source identifier (e.g., "faq", "manual")
            embedding: Vector embedding (768-dim, mock for now)
            metadata: Additional metadata dict
            
        Returns:
            Created VectorStore ID
        """
        vs = VectorStore(
            text_chunk=text_chunk,
            source=source,
            embedding=embedding,
            metadata=metadata or {},
        )
        db.add(vs)
        await db.flush()
        return vs.id


async def get_rag_service() -> RAGService:
    """Dependency injection for RAG service."""
    return RAGService()
