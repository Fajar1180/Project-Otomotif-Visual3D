"""Tests for database models."""
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from uuid import uuid4

from app.database import Base
from app.models import User, Vehicle, DiagnosticResult, Recommendation, Workshop


@pytest.fixture
def test_db():
    """Create in-memory SQLite database for testing."""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    yield db
    db.close()


def test_create_user(test_db):
    """Test user creation."""
    user = User(
        id=uuid4(),
        email="test@example.com",
        password_hash="hashed_password",
        full_name="Test User",
        phone="081234567890",
    )
    test_db.add(user)
    test_db.commit()
    test_db.refresh(user)
    
    assert user.email == "test@example.com"
    assert user.full_name == "Test User"
    assert user.id is not None


def test_create_vehicle(test_db):
    """Test vehicle creation."""
    user = User(
        id=uuid4(),
        email="test@example.com",
        password_hash="hashed_password",
        full_name="Test User",
    )
    test_db.add(user)
    test_db.commit()
    
    vehicle = Vehicle(
        id=uuid4(),
        user_id=user.id,
        make="Honda",
        model="Civic",
        year=2020,
        color="Silver",
    )
    test_db.add(vehicle)
    test_db.commit()
    test_db.refresh(vehicle)
    
    assert vehicle.make == "Honda"
    assert vehicle.model == "Civic"
    assert vehicle.year == 2020


def test_create_diagnostic_result(test_db):
    """Test diagnostic result creation with relationships."""
    user = User(
        id=uuid4(),
        email="test@example.com",
        password_hash="hashed_password",
        full_name="Test User",
    )
    test_db.add(user)
    test_db.commit()
    
    vehicle = Vehicle(
        id=uuid4(),
        user_id=user.id,
        make="Honda",
        model="Civic",
        year=2020,
    )
    test_db.add(vehicle)
    test_db.commit()
    
    diagnostic = DiagnosticResult(
        id=uuid4(),
        user_id=user.id,
        vehicle_id=vehicle.id,
        symptom_text="Engine is making noise",
        diagnosis="Carbon buildup likely",
        confidence_score=0.87,
        severity="medium",
    )
    test_db.add(diagnostic)
    test_db.commit()
    test_db.refresh(diagnostic)
    
    assert diagnostic.confidence_score == 0.87
    assert diagnostic.severity == "medium"
    assert diagnostic.vehicle.make == "Honda"


def test_diagnostic_has_recommendations(test_db):
    """Test recommendations relationship."""
    user = User(
        id=uuid4(),
        email="test@example.com",
        password_hash="hashed_password",
        full_name="Test User",
    )
    test_db.add(user)
    test_db.commit()
    
    vehicle = Vehicle(
        id=uuid4(),
        user_id=user.id,
        make="Honda",
        model="Civic",
        year=2020,
    )
    test_db.add(vehicle)
    test_db.commit()
    
    diagnostic = DiagnosticResult(
        id=uuid4(),
        user_id=user.id,
        vehicle_id=vehicle.id,
        symptom_text="Engine is making noise",
        diagnosis="Carbon buildup likely",
        confidence_score=0.87,
        severity="medium",
    )
    test_db.add(diagnostic)
    test_db.commit()
    
    recommendation = Recommendation(
        id=uuid4(),
        diagnostic_result_id=diagnostic.id,
        part_name="Fuel System Cleaner",
        part_category="Additives",
        estimated_cost=75000,
        urgency="soon",
        priority=1,
    )
    test_db.add(recommendation)
    test_db.commit()
    test_db.refresh(diagnostic)
    
    assert len(diagnostic.recommendations) == 1
    assert diagnostic.recommendations[0].part_name == "Fuel System Cleaner"
