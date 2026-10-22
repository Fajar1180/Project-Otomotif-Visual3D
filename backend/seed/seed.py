"""Seed script to populate test data."""
import uuid
from datetime import datetime
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine, Base
from app.models import User, Vehicle, DiagnosticResult, Recommendation, Workshop, VectorStore
from config import settings


def seed_users(db: Session):
    """Create test users."""
    users = [
        User(
            id=uuid.uuid4(),
            email="user1@example.com",
            password_hash="$2b$12$...",  # Placeholder hash
            full_name="Ahmad Rizki",
            phone="081234567890",
        ),
        User(
            id=uuid.uuid4(),
            email="user2@example.com",
            password_hash="$2b$12$...",
            full_name="Siti Nurhaliza",
            phone="081298765432",
        ),
    ]
    db.add_all(users)
    db.commit()
    return users


def seed_vehicles(db: Session, users: list):
    """Create test vehicles."""
    vehicles = [
        Vehicle(
            id=uuid.uuid4(),
            user_id=users[0].id,
            make="Honda",
            model="Civic",
            year=2020,
            color="Silver",
            vin="JHMGK5440LM109186",
            mileage=45000,
            notes="Regular maintenance done",
        ),
        Vehicle(
            id=uuid.uuid4(),
            user_id=users[0].id,
            make="Toyota",
            model="Avanza",
            year=2019,
            color="White",
            vin="TMBL28N1192088088",
            mileage=62000,
            notes="Need oil change soon",
        ),
        Vehicle(
            id=uuid.uuid4(),
            user_id=users[1].id,
            make="Daihatsu",
            model="Xenia",
            year=2021,
            color="Black",
            vin="DAIA21N1206088888",
            mileage=28000,
            notes="Warranty still valid",
        ),
    ]
    db.add_all(vehicles)
    db.commit()
    return vehicles


def seed_diagnostics(db: Session, users: list, vehicles: list):
    """Create test diagnostic results."""
    diagnostics = [
        DiagnosticResult(
            id=uuid.uuid4(),
            user_id=users[0].id,
            vehicle_id=vehicles[0].id,
            symptom_text="Mesin berbunyi aneh saat RPM tinggi, terasa seperti knocking",
            diagnosis="Kemungkinan carbon buildup di ruang bakar atau kualitas bahan bakar rendah. Rekomendasi: gunakan Premium Fuel dan lakukan flush injector.",
            confidence_score=0.87,
            severity="medium",
            repair_steps=[
                {"step": 1, "description": "Gunakan fuel octane booster"},
                {"step": 2, "description": "Bawa ke bengkel untuk flush injector"},
                {"step": 3, "description": "Ganti filter udara jika perlu"},
            ],
            embedding=None,  # Will be populated by RAG system
        ),
        DiagnosticResult(
            id=uuid.uuid4(),
            user_id=users[0].id,
            vehicle_id=vehicles[1].id,
            symptom_text="Oli berkurang cepat, ada bau gosong saat berkendara",
            diagnosis="Kemungkinan oli bocor di gasket atau piston ring sudah aus. Konsumsi oli tinggi menunjukkan internal wear.",
            confidence_score=0.92,
            severity="high",
            repair_steps=[
                {"step": 1, "description": "Periksa level oli setiap hari"},
                {"step": 2, "description": "Bawa ke bengkel untuk oil change"},
                {"step": 3, "description": "Lakukan compression test untuk piston ring"},
            ],
        ),
    ]
    db.add_all(diagnostics)
    db.commit()
    return diagnostics


def seed_recommendations(db: Session, diagnostics: list):
    """Create test recommendations."""
    recommendations = [
        Recommendation(
            id=uuid.uuid4(),
            diagnostic_result_id=diagnostics[0].id,
            part_name="Fuel System Cleaner",
            part_category="Fuel Additives",
            part_description="Premium octane booster untuk pembersihan ruang bakar",
            estimated_cost=75000,  # IDR
            shopee_product_id="123456789",
            shopee_link="https://shopee.co.id/...",
            priority=1,
            urgency="soon",
        ),
        Recommendation(
            id=uuid.uuid4(),
            diagnostic_result_id=diagnostics[1].id,
            part_name="Synthetic Motor Oil 5W-30",
            part_category="Engine Oil",
            part_description="Oli sintetis berkualitas tinggi untuk mesin modern",
            estimated_cost=185000,
            shopee_product_id="987654321",
            shopee_link="https://shopee.co.id/...",
            priority=2,
            urgency="immediate",
        ),
    ]
    db.add_all(recommendations)
    db.commit()
    return recommendations


def seed_workshops(db: Session):
    """Create test workshop directory."""
    workshops = [
        Workshop(
            id=uuid.uuid4(),
            name="Bengkel Jaya Motor",
            address="Jl. Merdeka No. 123, Jakarta Selatan",
            latitude=-6.2548,
            longitude=106.7889,
            phone="021-1234567",
            specialties=["General Maintenance", "Electrical", "Engine"],
            rating=4.8,
            review_count=156,
            website="https://bengkeljaya.example.com",
        ),
        Workshop(
            id=uuid.uuid4(),
            name="Servis Mobil Terpercaya",
            address="Jl. Sudirman No. 456, Bandung",
            latitude=-6.9147,
            longitude=107.6051,
            phone="022-9876543",
            specialties=["Brake Service", "Suspension", "Transmission"],
            rating=4.6,
            review_count=89,
            website="https://servis-terpercaya.example.com",
        ),
    ]
    db.add_all(workshops)
    db.commit()
    return workshops


def seed_vector_store(db: Session):
    """Create sample vector store entries (knowledge base)."""
    vectors = [
        VectorStore(
            id=uuid.uuid4(),
            text_chunk="Suara knocking pada mesin saat RPM tinggi biasanya disebabkan oleh carbon buildup atau kualitas bahan bakar yang rendah.",
            source="faq",
            embedding=None,  # 768-dim vector (would be computed by embedding model)
            metadata={"vehicle_make": "Honda", "issue_type": "engine_knock"},
        ),
        VectorStore(
            id=uuid.uuid4(),
            text_chunk="Konsumsi oli yang tinggi dapat menunjukkan piston ring yang sudah aus atau gasket yang bocor.",
            source="manual",
            embedding=None,
            metadata={"vehicle_make": "Toyota", "issue_type": "oil_consumption"},
        ),
    ]
    db.add_all(vectors)
    db.commit()


def main():
    """Run all seed functions."""
    # Create tables
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:
        print("🌱 Seeding database...")
        
        users = seed_users(db)
        print(f"✓ Created {len(users)} users")
        
        vehicles = seed_vehicles(db, users)
        print(f"✓ Created {len(vehicles)} vehicles")
        
        diagnostics = seed_diagnostics(db, users, vehicles)
        print(f"✓ Created {len(diagnostics)} diagnostic results")
        
        recommendations = seed_recommendations(db, diagnostics)
        print(f"✓ Created {len(recommendations)} recommendations")
        
        workshops = seed_workshops(db)
        print(f"✓ Created {len(workshops)} workshops")
        
        seed_vector_store(db)
        print("✓ Seeded vector store")
        
        print("\n✅ Database seeding complete!")
    except Exception as e:
        db.rollback()
        print(f"❌ Error during seeding: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
