"""Vehicle catalog routes."""
from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.database import get_db
from models import Vehicle

router = APIRouter(prefix="/api/v1/vehicles", tags=["vehicles"])


class VehicleCreate(BaseModel):
    brand: str = Field(..., min_length=1, max_length=100)
    model: str = Field(..., min_length=1, max_length=100)
    year_start: int = Field(..., ge=1900, le=2100)
    year_end: Optional[int] = Field(None, ge=1900, le=2100)
    category: Optional[str] = Field(None, max_length=30)


class VehicleOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    brand: str
    model: str
    year_start: int
    year_end: Optional[int] = None
    category: Optional[str] = None


@router.get("")
def list_vehicles(
    brand: Optional[str] = None,
    category: Optional[str] = None,
    year: Optional[int] = None,
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
) -> dict:
    """Paginated vehicle list with optional brand/category/year filters."""
    stmt = select(Vehicle)
    if brand:
        stmt = stmt.where(Vehicle.brand.ilike(brand))
    if category:
        stmt = stmt.where(Vehicle.category == category)
    if year:
        stmt = stmt.where(Vehicle.year_start <= year).where(
            (Vehicle.year_end.is_(None)) | (Vehicle.year_end >= year)
        )

    total = db.execute(select(func.count()).select_from(stmt.subquery())).scalar_one()
    rows = (
        db.execute(stmt.order_by(Vehicle.brand, Vehicle.model).offset((page - 1) * limit).limit(limit))
        .scalars()
        .all()
    )
    return {
        "data": [VehicleOut.model_validate(r).model_dump() for r in rows],
        "meta": {
            "total": total,
            "page": page,
            "limit": limit,
            "total_pages": (total + limit - 1) // limit,
        },
    }


@router.get("/{vehicle_id}", response_model=VehicleOut)
def get_vehicle(vehicle_id: str, db: Session = Depends(get_db)) -> Vehicle:
    """Vehicle detail by id."""
    vehicle = db.get(Vehicle, vehicle_id)
    if not vehicle:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Kendaraan tidak ditemukan")
    return vehicle


@router.post("", response_model=VehicleOut, status_code=status.HTTP_201_CREATED)
def create_vehicle(payload: VehicleCreate, db: Session = Depends(get_db)) -> Vehicle:
    """Create a vehicle catalog entry."""
    vehicle = Vehicle(**payload.model_dump())
    db.add(vehicle)
    db.commit()
    db.refresh(vehicle)
    return vehicle
