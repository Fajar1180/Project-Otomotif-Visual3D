"""Database models for Otomotif AI platform aligned with ERD schema (7 tables)."""
from datetime import datetime
from uuid import uuid4


from sqlalchemy import (
    Column,
    String,
    Integer,
    Float,
    Text,
    JSON,
    DateTime,
    Enum,
    Boolean,
    ARRAY,
    Numeric,
    UniqueConstraint,
    ForeignKey,
    func,
)
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.dialects.postgresql import UUID, JSONB, NUMERIC


Base = declarative_base()


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    brand = Column(String(50), nullable=False)
    model = Column(String(100), nullable=False)
    year_start = Column(Integer, nullable=False)
    year_end = Column(Integer, nullable=True)
    category = Column(String(30), nullable=True)

    # Relationships
    symptom_maps = relationship("SymptomDiagnosisMap", back_populates="vehicle")
    workshop_maps = relationship("VehicleWorkshop", back_populates="vehicle")


class Symptom(Base):
    __tablename__ = "symptoms"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    symptom_code = Column(String(20), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    category = Column(String(50), nullable=True)
    embedding = Column(NUMERIC(1536), nullable=True)  # 1536-dim vector for similarity search

    # Relationships
    vehicle_symptoms = relationship("VehicleSymptom", back_populates="symptom")
    diagnosis_maps = relationship("SymptomDiagnosisMap", back_populates="symptom")


class Diagnosis(Base):
    __tablename__ = "diagnoses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String(150), nullable=False)
    technical_explanation = Column(Text, nullable=False)
    severity_level = Column(Enum("DIY_EASY", "DIY_HARD", "WORKSHOP_REQUIRED", name="severity_level"), nullable=False)
    repair_steps = Column(JSON, nullable=True)  # Array of step objects

    # Relationships
    symptom_maps = relationship("SymptomDiagnosisMap", back_populates="diagnosis")
    part_maps = relationship("DiagnosisPartMap", back_populates="diagnosis")
    vehicle_symptoms = relationship("VehicleSymptom", back_populates="diagnosis")
    diagnosis_parts = relationship("DiagnosisPartMap", back_populates="diagnosis")


class SparePart(Base):
    __tablename__ = "spare_parts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    part_name = Column(String(150), nullable=False)
    part_number = Column(String(50), nullable=False)
    brand = Column(String(50), nullable=True)
    price_min = Column(Numeric(12, 2), nullable=True)
    price_max = Column(Numeric(12, 2), nullable=True)
    shopee_item_id = Column(String(50), nullable=True)
    shopee_shop_id = Column(String(50), nullable=True)
    default_shopee_url = Column(Text, nullable=True)

    # Relationships
    diagnosis_parts = relationship("DiagnosisPartMap", back_populates="spare_part")


class Workshop(Base):
    __tablename__ = "workshops"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(100), nullable=False)
    address = Column(Text, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    phone = Column(String(20), nullable=True)
    specialties = Column(ARRAY(String), nullable=True)  # e.g., ['engine', 'transmission']
    rating = Column(Float, nullable=True)
    review_count = Column(Integer, default=0)

    # Relationships
    vehicle_workshop = relationship("VehicleWorkshop", back_populates="workshop")


class SymptomDiagnosisMap(Base):
    __tablename__ = "symptom_diagnosis_map"

    symptom_id = Column(UUID(as_uuid=True), ForeignKey("symptoms.id", ondelete="CASCADE"), primary_key=True)
    diagnosis_id = Column(UUID(as_uuid=True), ForeignKey("diagnoses.id", ondelete="CASCADE"), primary_key=True)
    confidence_weight = Column(Float, nullable=False)

    # Relationships
    symptom = relationship("Symptom", back_populates="diagnosis_maps")
    diagnosis = relationship("Diagnosis", back_populates="symptom_maps")
    vehicle = relationship("Vehicle", back_populates="symptom_diagnosis_maps")


class DiagnosisPartMap(Base):
    __tablename__ = "diagnosis_part_map"

    diagnosis_id = Column(UUID(as_uuid=True), ForeignKey("diagnoses.id", ondelete="CASCADE"), primary_key=True)
    spare_part_id = Column(UUID(as_uuid=True), ForeignKey("spare_parts.id", ondelete="CASCADE"), primary_key=True)
    is_primary = Column(Boolean, default=False)

    # Relationships
    diagnosis = relationship("Diagnosis", back_populates="part_map")
    spare_part = relationship("SparePart", back_populates="diagnosis_parts")


class VehicleSymptom(Base):
    __tablename__ = "vehicle_symptom"

    vehicle_id = Column(UUID(as_uuid=True), ForeignKey("vehicles.id", ondelete="CASCADE"), primary_key=True)
    symptom_id = Column(UUID(as_uuid=True), ForeignKey("symptoms.id", ondelete="CASCADE"), primary_key=True)


class VehicleWorkshop(Base):
    __tablename__ = "vehicle_workshop"

    vehicle_id = Column(UUID(as_uuid=True), ForeignKey("vehicles.id", ondelete="CASCADE"), primary_key=True)
    workshop_id = Column(UUID(as_uuid=True), ForeignKey("workshops.id", ondelete="CASCADE"), primary_key=True)


def __repr__(self):
    return f"<{self.__class__.__name__}(id={self.id})>"