"""SQLAlchemy ORM models for Otomotif AI platform."""
from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, ForeignKey, Text, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector

from app.database import Base


class User(Base):
    """User account and profile."""
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    vehicles = relationship("Vehicle", back_populates="owner", cascade="all, delete-orphan")
    diagnostic_results = relationship("DiagnosticResult", back_populates="user", cascade="all, delete-orphan")


class Vehicle(Base):
    """User vehicle inventory."""
    __tablename__ = "vehicles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    make = Column(String(100), nullable=False)  # e.g., "Honda"
    model = Column(String(100), nullable=False)  # e.g., "Civic"
    year = Column(Integer, nullable=False)
    color = Column(String(100), nullable=True)
    vin = Column(String(50), unique=True, nullable=True)
    mileage = Column(Integer, nullable=True)  # in km
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    owner = relationship("User", back_populates="vehicles")
    diagnostic_results = relationship("DiagnosticResult", back_populates="vehicle", cascade="all, delete-orphan")


class DiagnosticResult(Base):
    """AI diagnosis history with vector embeddings."""
    __tablename__ = "diagnostic_results"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    vehicle_id = Column(UUID(as_uuid=True), ForeignKey("vehicles.id"), nullable=False, index=True)
    
    # Input
    symptom_text = Column(Text, nullable=False)
    
    # Output
    diagnosis = Column(Text, nullable=False)
    confidence_score = Column(Float, nullable=False)  # 0.0-1.0
    severity = Column(String(50), nullable=False)  # "low", "medium", "high", "critical"
    repair_steps = Column(JSON, nullable=True)  # Array of step objects
    
    # Vector embedding for semantic search (pgvector)
    embedding = Column(Vector(768), nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="diagnostic_results")
    vehicle = relationship("Vehicle", back_populates="diagnostic_results")
    recommendations = relationship("Recommendation", back_populates="diagnostic_result", cascade="all, delete-orphan")


class Recommendation(Base):
    """Suku cadang recommendations with Shopee affiliate links."""
    __tablename__ = "recommendations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    diagnostic_result_id = Column(UUID(as_uuid=True), ForeignKey("diagnostic_results.id"), nullable=False, index=True)
    
    part_name = Column(String(255), nullable=False)
    part_description = Column(Text, nullable=True)
    part_category = Column(String(100), nullable=False)
    estimated_cost = Column(Float, nullable=True)  # in IDR
    
    # Shopee Affiliate
    shopee_product_id = Column(String(100), nullable=True)
    shopee_link = Column(String(500), nullable=True)
    shopee_affiliate_link = Column(String(500), nullable=True)
    
    priority = Column(Integer, default=0)  # 0=low, 1=medium, 2=high
    urgency = Column(String(50), nullable=False)  # "immediate", "soon", "optional"
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    diagnostic_result = relationship("DiagnosticResult", back_populates="recommendations")


class Workshop(Base):
    """Bengkel directory for workshop finder integration."""
    __tablename__ = "workshops"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(255), nullable=False)
    address = Column(Text, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    phone = Column(String(20), nullable=True)
    
    specialties = Column(JSON, nullable=True)  # Array of service types
    rating = Column(Float, nullable=True)  # 0.0-5.0
    review_count = Column(Integer, default=0)
    
    # Google Maps / external integration
    google_place_id = Column(String(200), nullable=True)
    website = Column(String(500), nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class VectorStore(Base):
    """Cache for pgvector embeddings (diagnostic knowledge base)."""
    __tablename__ = "vector_store"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    
    # Reference to diagnostic result (optional, for traceability)
    diagnostic_result_id = Column(UUID(as_uuid=True), ForeignKey("diagnostic_results.id"), nullable=True)
    
    # Content
    text_chunk = Column(Text, nullable=False)
    source = Column(String(100), nullable=False)  # "faq", "manual", "community", etc.
    
    # Vector embedding
    embedding = Column(Vector(768), nullable=False)
    
    metadata = Column(JSON, nullable=True)  # Extra context (e.g., vehicle_make, part_category)
    
    created_at = Column(DateTime, default=datetime.utcnow)
