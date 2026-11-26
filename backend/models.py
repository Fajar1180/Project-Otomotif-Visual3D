"""Database models for Otomotif AI platform aligned with ERD schema (7 tables).

Single declarative Base in this module. Import Base from here in app/database.py.
"""
from __future__ import annotations

from datetime import datetime
from uuid import uuid4

from sqlalchemy import (
    Column, String, Integer, Float, Text, JSON, DateTime, 
    Boolean, UniqueConstraint, ForeignKey, func,
    Enum as SAEnum,
)
from sqlalchemy.orm import declarative_base, relationship
import enum

# Single Base
Base = declarative_base()


class SeverityLevel(str, enum.Enum):
    """Severity classification for diagnoses."""
    DIY_EASY = "DIY_EASY"
    DIY_HARD = "DIY_HARD"
    WORKSHOP_REQUIRED = "WORKSHOP_REQUIRED"


class Vehicle(Base):
    """Vehicle model (brand, model, year range)."""
    __tablename__ = "vehicles"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    brand = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    year_start = Column(Integer, nullable=False)
    year_end = Column(Integer, nullable=True)
    category = Column(String(30), nullable=True)
    created_at = Column(DateTime, default=func.now())

    # Relationships
    diagnostic_results = relationship("DiagnosticResult", back_populates="vehicle")

    __table_args__ = (UniqueConstraint("brand", "model", "year_start", name="uq_vehicle_year"),)


class Symptom(Base):
    """Symptom catalog (knocking, overheating, etc.)."""
    __tablename__ = "symptoms"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    symptom_code = Column(String(50), unique=True, nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(50), nullable=False)  # Engine, Transmission, etc.
    embedding = Column(JSON, nullable=True)  # ponytail: JSON not pgvector, swap when pgvector is installed
    created_at = Column(DateTime, default=func.now())


class Diagnosis(Base):
    """Diagnosis record (what's wrong, severity, repair steps)."""
    __tablename__ = "diagnoses"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    title = Column(String(255), nullable=False)
    technical_explanation = Column(Text, nullable=False)
    severity_level = Column(SAEnum(SeverityLevel), nullable=False)
    repair_steps = Column(JSON, nullable=True)  # List[{step: int, description: str}]
    created_at = Column(DateTime, default=func.now())

    # Relationships
    spare_part_maps = relationship("DiagnosisPartMap", back_populates="diagnosis")


class SparePart(Base):
    """Spare part catalog (filters, belts, bearings, etc.)."""
    __tablename__ = "spare_parts"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    part_name = Column(String(255), nullable=False)
    part_number = Column(String(100), unique=True, nullable=False)
    category = Column(String(100), nullable=False)
    brand = Column(String(100), nullable=True)
    price_min = Column(Float, nullable=True)
    price_max = Column(Float, nullable=True)
    default_shopee_url = Column(String(500), nullable=True)
    shopee_item_id = Column(String(50), nullable=True)
    shopee_shop_id = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=func.now())

    # Relationships
    diagnosis_maps = relationship("DiagnosisPartMap", back_populates="spare_part")


class DiagnosisPartMap(Base):
    """Junction table: Diagnosis → SparePart (many-to-many)."""
    __tablename__ = "diagnosis_part_maps"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    diagnosis_id = Column(String(36), ForeignKey("diagnoses.id"), nullable=False)
    part_id = Column(String(36), ForeignKey("spare_parts.id"), nullable=False)
    is_primary = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())

    # Relationships
    diagnosis = relationship("Diagnosis", back_populates="spare_part_maps")
    spare_part = relationship("SparePart", back_populates="diagnosis_maps")

    __table_args__ = (UniqueConstraint("diagnosis_id", "part_id", name="uq_diagnosis_part"),)


class VectorStore(Base):
    """Vector embedding storage for RAG (text chunks + embeddings)."""
    __tablename__ = "vector_store"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    text_chunk = Column(Text, nullable=False)
    source = Column(String(100), nullable=False)  # "faq", "manual", "forum", etc.
    embedding = Column(JSON, nullable=True)  # 768-dim vector as JSON array
    extra_metadata = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=func.now())


class Workshop(Base):
    """Trusted workshop catalog (for WORKSHOP_REQUIRED diagnoses)."""
    __tablename__ = "workshops"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    name = Column(String(100), nullable=False)
    address = Column(Text, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    phone = Column(String(20), nullable=True)
    specialties = Column(JSON, nullable=True)  # ["Engine", "Electrical", ...]
    rating = Column(Float, default=0.0)  # 0-5 star rating
    review_count = Column(Integer, default=0)
    website = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=func.now())


class SymptomDiagnosisMap(Base):
    """Junction table: Symptom -> Diagnosis with a confidence weight."""
    __tablename__ = "symptom_diagnosis_map"

    symptom_id = Column(String(36), ForeignKey("symptoms.id"), primary_key=True)
    diagnosis_id = Column(String(36), ForeignKey("diagnoses.id"), primary_key=True)
    confidence_weight = Column(Float, nullable=False, default=0.5)


class User(Base):
    """Registered user (JWT auth)."""
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(150), nullable=True)
    role = Column(String(20), nullable=False, default="user")  # "user" | "admin"
    created_at = Column(DateTime, default=func.now())

    refresh_tokens = relationship("RefreshToken", back_populates="user", cascade="all, delete-orphan")


class RefreshToken(Base):
    """Refresh token for rotating access tokens."""
    __tablename__ = "refresh_tokens"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    token = Column(String(255), unique=True, nullable=False, index=True)
    expires_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=func.now())

    user = relationship("User", back_populates="refresh_tokens")


class DiagnosticResult(Base):
    """Stored diagnosis result for a user's vehicle (audit trail)."""
    __tablename__ = "diagnostic_results"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    vehicle_id = Column(String(36), ForeignKey("vehicles.id"), nullable=True)
    symptom_text = Column(Text, nullable=False)
    diagnosis = Column(Text, nullable=False)
    severity = Column(SAEnum(SeverityLevel), nullable=False)
    confidence_score = Column(Float, nullable=True)  # 0.0-1.0
    repair_steps = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=func.now())

    # Relationships
    vehicle = relationship("Vehicle", back_populates="diagnostic_results")
