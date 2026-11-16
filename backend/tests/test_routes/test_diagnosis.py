"""Integration tests for diagnosis endpoint."""
import pytest
from uuid import uuid4
from httpx import ASGITransport, AsyncClient

from app.main import app
from models import Vehicle, Symptom, Diagnosis, SparePart


@pytest.mark.asyncio
async def test_analyze_diagnosis_happy_path(test_db_async):
    """Test successful diagnosis analysis."""
    # Seed test data
    symptom = Symptom(
        id=str(uuid4()),
        symptom_code="ENG_KNOCK",
        description="Engine knocking sound at high RPM",
        category="Engine",
    )
    test_db_async.add(symptom)
    test_db_async.flush()

    diagnosis = Diagnosis(
        id=str(uuid4()),
        title="Carbon Buildup",
        technical_explanation="Accumulation of carbon deposits in combustion chamber",
        severity_level="DIY_HARD",
        repair_steps=[
            {"step": 1, "description": "Use fuel system cleaner"},
            {"step": 2, "description": "Visit workshop for injection cleaning"},
        ],
    )
    test_db_async.add(diagnosis)
    test_db_async.commit()

    # Make request
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post(
            "/api/v1/diagnosis/analyze",
            json={
                "symptom_text": "Engine is making knocking sound when accelerating at high RPM",
                "vehicle_make": "Honda",
                "vehicle_model": "Civic",
                "vehicle_year": 2020,
            },
        )

    assert response.status_code == 200
    data = response.json()
    assert "diagnosis_id" in data
    assert data["conclusion"]
    assert data["severity_level"] in ["DIY_EASY", "DIY_HARD", "WORKSHOP_REQUIRED"]
    assert 0.0 <= data["confidence_score"] <= 1.0
    assert data["technical_explanation"]
    assert isinstance(data["repair_steps"], list)
    assert isinstance(data["recommended_parts"], list)
    assert isinstance(data["recommended_workshops"], list)
    # legacy fields must be gone
    for legacy in ("diagnosis", "severity", "recommendations"):
        assert legacy not in data


@pytest.mark.asyncio
async def test_analyze_diagnosis_validation_error():
    """Test validation error for short symptom."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post(
            "/api/v1/diagnosis/analyze",
            json={
                "symptom_text": "Short",  # Too short
                "vehicle_make": "Honda",
            },
        )

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_analyze_diagnosis_year_validation():
    """Test validation error for invalid vehicle year."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post(
            "/api/v1/diagnosis/analyze",
            json={
                "symptom_text": "Engine is making weird sounds and losing power quickly",
                "vehicle_year": 1800,  # Invalid year
            },
        )

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_analyze_diagnosis_with_vehicle_id(test_db_async):
    """Test diagnosis with saved vehicle ID."""
    from models import Vehicle
    
    vehicle = Vehicle(
        id=str(uuid4()),
        brand="Toyota",
        model="Avanza",
        year_start=2019,
    )
    test_db_async.add(vehicle)
    test_db_async.commit()

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post(
            "/api/v1/diagnosis/analyze",
            json={
                "symptom_text": "Oil consumption is very high, engine losing power",
                "vehicle_id": str(vehicle.id),
            },
        )

    assert response.status_code == 200
    data = response.json()
    assert "diagnosis_id" in data


@pytest.mark.asyncio
async def test_diagnosis_response_structure():
    """Test response structure matches schema."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.post(
            "/api/v1/diagnosis/analyze",
            json={
                "symptom_text": "Engine is making knocking sound and consuming oil rapidly",
                "vehicle_make": "Honda",
                "vehicle_model": "Civic",
                "vehicle_year": 2018,
            },
        )

    assert response.status_code == 200
    data = response.json()

    # Verify response structure
    required_fields = [
        "diagnosis_id",
        "conclusion",
        "severity_level",
        "confidence_score",
        "technical_explanation",
        "repair_steps",
        "recommended_parts",
        "recommended_workshops",
    ]
    for field in required_fields:
        assert field in data, f"Missing required field: {field}"

    assert data["severity_level"] in ["DIY_EASY", "DIY_HARD", "WORKSHOP_REQUIRED"]
    assert 0.0 <= data["confidence_score"] <= 1.0

    # Verify repair steps structure: [{step:int, description:str}]
    assert data["repair_steps"], "expected at least one repair step"
    for step in data["repair_steps"]:
        assert isinstance(step["step"], int)
        assert isinstance(step["description"], str)

    # Verify recommended parts structure
    for part in data["recommended_parts"]:
        for field in ("part_id", "part_name", "brand", "price_estimate", "shopee_affiliate_link", "is_primary"):
            assert field in part

    # Verify recommended workshops structure (may be empty)
    for ws in data["recommended_workshops"]:
        for field in ("workshop_id", "name", "address", "distance_km", "rating", "phone", "maps_url"):
            assert field in ws
