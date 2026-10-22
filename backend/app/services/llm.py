"""LLM (Language Model) integration service for diagnosis generation."""
from typing import Optional, Dict, Any
import json
import logging

from tenacity import retry, stop_after_attempt, wait_exponential
from openai import AsyncOpenAI

logger = logging.getLogger(__name__)


class LLMService:
    """OpenAI/Claude LLM service for diagnosis generation."""

    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo", mock: bool = False):
        """
        Initialize LLM service.
        
        Args:
            api_key: OpenAI API key
            model: Model name (gpt-3.5-turbo, gpt-4, etc.)
            mock: Use mock responses (for testing)
        """
        self.model = model
        self.mock = mock
        self.client = AsyncOpenAI(api_key=api_key) if api_key and not mock else None

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    async def diagnose(
        self,
        symptom_text: str,
        vehicle_context: str,
        rag_context: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Generate diagnosis using LLM with RAG context.
        
        Args:
            symptom_text: User's symptom description
            vehicle_context: Vehicle info (make, model, year)
            rag_context: Retrieved context from VectorStore
            
        Returns:
            Dict with diagnosis, severity, confidence, repair_steps
        """
        if self.mock:
            return self._mock_diagnosis(symptom_text, vehicle_context)

        # Build prompt with RAG context
        prompt = self._build_prompt(symptom_text, vehicle_context, rag_context)
        
        try:
            response = await self._call_openai(prompt)
            return self._parse_response(response)
        except Exception as e:
            logger.error(f"LLM error: {e}")
            # Fallback to mock if API fails
            return self._mock_diagnosis(symptom_text, vehicle_context)

    def _build_prompt(
        self,
        symptom_text: str,
        vehicle_context: str,
        rag_context: Dict[str, Any],
    ) -> str:
        """Build structured prompt for LLM."""
        diagnoses_context = "\n".join([
            f"- {d['title']}: {d['explanation'][:100]}"
            for d in rag_context.get("diagnoses", [])[:3]
        ])
        
        parts_context = "\n".join([
            f"- {p['part_name']} ({p['category']}): {p['price_range']}"
            for p in rag_context.get("spare_parts", [])[:5]
        ])

        prompt = f"""Anda adalah mekanik ahli mobil dan motor Indonesia. Analisis gejala berikut dan berikan diagnosis.

Gejala Pengguna:
{symptom_text}

Informasi Kendaraan:
{vehicle_context}

Konteks Diagnosis Serupa (dari knowledge base):
{diagnoses_context or "Tidak ada konteks serupa."}

Suku Cadang Relevan:
{parts_context or "Tidak ada suku cadang yang disarankan."}

Berikan diagnosis HANYA dalam format JSON berikut (tanpa teks tambahan):
{{
  "diagnosis": "Penjelasan teknis diagnosa (2-3 kalimat)",
  "severity": "DIY_EASY|DIY_HARD|WORKSHOP_REQUIRED",
  "confidence": 0.85,
  "repair_steps": [
    {{"step": 1, "description": "Langkah perbaikan pertama"}},
    {{"step": 2, "description": "Langkah perbaikan kedua"}}
  ]
}}

Hanya JSON, tidak ada penjelasan tambahan."""
        return prompt

    async def _call_openai(self, prompt: str) -> str:
        """Call OpenAI API asynchronously."""
        if not self.client:
            raise ValueError("OpenAI client not initialized")
        
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Anda adalah mekanik otomotif profesional Indonesia."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,
            max_tokens=500,
        )
        content = response.choices[0].message.content
        if content is None:
            raise ValueError("OpenAI returned empty response")
        return content

    def _parse_response(self, response_text: str) -> Dict[str, Any]:
        """Parse LLM JSON response."""
        try:
            # Extract JSON from response
            start = response_text.find('{')
            end = response_text.rfind('}') + 1
            json_str = response_text[start:end] if start != -1 else response_text
            
            parsed = json.loads(json_str)
            
            # Validate required fields
            required = ["diagnosis", "severity", "confidence", "repair_steps"]
            for field in required:
                if field not in parsed:
                    raise ValueError(f"Missing field: {field}")
            
            # Validate severity enum
            if parsed["severity"] not in ["DIY_EASY", "DIY_HARD", "WORKSHOP_REQUIRED"]:
                parsed["severity"] = "WORKSHOP_REQUIRED"  # Failsafe
            
            return parsed
        except json.JSONDecodeError:
            logger.warning("Failed to parse LLM response as JSON, using mock")
            return self._mock_diagnosis("", "")

    def _mock_diagnosis(self, symptom_text: str, vehicle_context: str) -> Dict[str, Any]:
        """Return mock diagnosis for testing/fallback."""
        return {
            "diagnosis": "Kemungkinan carbon buildup di ruang bakar atau kualitas bahan bakar rendah. Mesin butuh fuel system cleaning dan pemeriksaan injector.",
            "severity": "DIY_HARD",
            "confidence": 0.82,
            "repair_steps": [
                {"step": 1, "description": "Gunakan fuel octane booster (Premium Fuel) untuk pembersihan otomatis"},
                {"step": 2, "description": "Bawa ke bengkel untuk fuel system flush jika masalah berlanjut"},
                {"step": 3, "description": "Ganti fuel filter dan air filter (preventive maintenance)"},
                {"step": 4, "description": "Test drive untuk verifikasi perbaikan"},
            ],
        }


class LLMServiceFactory:
    """Factory for creating LLM service instances."""

    @staticmethod
    def create(api_key: Optional[str] = None, mock: bool = False) -> LLMService:
        """Create LLM service."""
        return LLMService(
            api_key=api_key or "",
            model="gpt-3.5-turbo",
            mock=mock,
        )
