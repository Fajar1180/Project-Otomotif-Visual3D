"""Tests for database models."""
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from models import Vehicle, Symptom, Diagnosis, SparePart, DiagnosisPartMap, VectorStore, Workshop, DiagnosticResult


@pytest.fixture
def test_db():
    """Create in-memory SQLite database for testing."""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    yield db
    db.close()


def test_vehicle_creation(test_db):
    """Test vehicle model creation."""
    vehicle = Vehicle(
        brand="Honda",
        model="Civic",
        year_start=2020,
        year_end=2023,
    )
    test_db.add(vehicle)
    test_db.commit()
    test_db.refresh(vehicle)

    assert vehicle.brand == "Honda"
    assert vehicle.model == "Civic"
    assert vehicle.year_start == 2020
    assert vehicle.id is not None


def test_symptom_creation(test_db):
    """Test symptom model creation."""
    symptom = Symptom(
        symptom_code="ENG_KNOCK",
        description="Engine knocking sound",
        category="Engine",
    )
    test_db.add(symptom)
    test_db.commit()
    test_db.refresh(symptom)

    assert symptom.symptom_code == "ENG_KNOCK"
    assert symptom.category == "Engine"


def test_diagnosis_creation(test_db):
    """Test diagnosis model creation."""
    from models import SeverityLevel
    
    diagnosis = Diagnosis(
        title="Carbon Buildup",
        technical_explanation="Accumulation of carbon deposits",
        severity_level=SeverityLevel.DIY_HARD,
        repair_steps=[{"step": 1, "description": "Clean fuel injectors"}],
    )
    test_db.add(diagnosis)
    test_db.commit()
    test_db.refresh(diagnosis)

    assert diagnosis.title == "Carbon Buildup"
    assert diagnosis.severity_level == SeverityLevel.DIY_HARD
