"""Integration tests for diagnosis endpoint."""
import pytest
from uuid import uuid4
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.main import app
from models import Vehicle, Symptom, Diagnosis, SparePart


@pytest.mark.asyncio
async def test_analyze_diagnosis_happy_path(test_db_async: AsyncSession):
    """Test successful diagnosis analysis."""
    # Seed test data
    symptom = Symptom(
        id=str(uuid4()),
        symptom_code="ENG_KNOCK",
        description="Engine knocking sound at high RPM",
        category="Engine",
    )
    test_db_async.add(symptom)
    await test_db_async.flush()

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
    await test_db_async.commit()

    # Make request
    async with AsyncClient(app=app, base_url="http://test") as client:
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
    assert "diagnosis" in data
    assert data["severity"] in ["DIY_EASY", "DIY_HARD", "WORKSHOP_REQUIRED"]
    assert 0.0 <= data["confidence_score"] <= 1.0
    assert isinstance(data["repair_steps"], list)
    assert isinstance(data["recommendations"], list)


@pytest.mark.asyncio
async def test_analyze_diagnosis_validation_error():
    """Test validation error for short symptom."""
    async with AsyncClient(app=app, base_url="http://test") as client:
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
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/api/v1/diagnosis/analyze",
            json={
                "symptom_text": "Engine is making weird sounds and losing power quickly",
                "vehicle_year": 1800,  # Invalid year
            },
        )

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_analyze_diagnosis_with_vehicle_id(test_db_async: AsyncSession):
    """Test diagnosis with saved vehicle ID."""
    from models import Vehicle
    
    vehicle = Vehicle(
        id=str(uuid4()),
        brand="Toyota",
        model="Avanza",
        year_start=2019,
    )
    test_db.add(vehicle)
    await test_db.commit()

    async with AsyncClient(app=app, base_url="http://test") as client:
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
    async with AsyncClient(app=app, base_url="http://test") as client:
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
        "diagnosis",
        "severity",
        "confidence_score",
        "repair_steps",
        "recommendations",
    ]
    for field in required_fields:
        assert field in data, f"Missing required field: {field}"

    # Verify repair steps structure
    for step in data["repair_steps"]:
        assert "step" in step
        assert "description" in step
        assert isinstance(step["step"], int)
        assert isinstance(step["description"], str)

    # Verify recommendations structure
    for rec in data["recommendations"]:
        assert "part_name" in rec
        assert "part_category" in rec
        assert "estimated_cost" in rec
        assert "priority" in rec
        assert "urgency" in rec
