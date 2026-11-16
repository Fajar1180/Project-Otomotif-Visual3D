"""Workshop directory routes."""
from __future__ import annotations

import math
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel, ConfigDict
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from models import Workshop

router = APIRouter(prefix="/api/v1/workshops", tags=["workshops"])


class WorkshopOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    address: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    phone: Optional[str] = None
    specialties: Optional[List[str]] = None
    rating: Optional[float] = None
    website: Optional[str] = None


def _haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    r = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp, dl = p2 - p1, math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return round(2 * r * math.asin(math.sqrt(a)), 2)


@router.get("")
def list_workshops(
    lat: Optional[float] = None,
    lng: Optional[float] = None,
    radius_km: float = Query(25.0, gt=0),
    specialty: Optional[str] = None,
    min_rating: float = Query(0.0, ge=0, le=5),
    db: Session = Depends(get_db),
) -> dict:
    """Workshop list; sorted by distance when lat/lng given, else by rating."""
    stmt = select(Workshop).where(Workshop.rating >= min_rating)
    workshops = db.execute(stmt).scalars().all()

    # ponytail: specialties is JSON; filter in Python until a GIN index exists
    if specialty:
        workshops = [
            w for w in workshops if specialty.lower() in [str(s).lower() for s in (w.specialties or [])]
        ]

    data = []
    for w in workshops:
        item = WorkshopOut.model_validate(w).model_dump()
        if lat is not None and lng is not None and w.latitude is not None and w.longitude is not None:
            item["distance_km"] = _haversine_km(lat, lng, w.latitude, w.longitude)
            if item["distance_km"] > radius_km:
                continue
            item["maps_url"] = f"https://maps.google.com/?q={w.latitude},{w.longitude}"
        else:
            item["distance_km"] = None
            item["maps_url"] = None
        data.append(item)

    data.sort(key=lambda i: (i["distance_km"] is None, i["distance_km"] or 0, -(i["rating"] or 0)))
    return {"data": data, "meta": {"total": len(data)}}


@router.get("/{workshop_id}", response_model=WorkshopOut)
def get_workshop(workshop_id: str, db: Session = Depends(get_db)) -> Workshop:
    """Workshop detail by id."""
    workshop = db.get(Workshop, workshop_id)
    if not workshop:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Bengkel tidak ditemukan")
    return workshop
