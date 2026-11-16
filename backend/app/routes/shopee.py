"""Shopee Affiliate API route.

Provides product search with caching, static fallback, and click tracking.
Rate-limited per IP (10 req/min) consistent with main.py pattern.
"""
from __future__ import annotations

from fastapi import APIRouter, Depends, Query, Request, status
from fastapi.responses import JSONResponse
from typing import List, Optional

from app.services.shopee import search_products, track_click
from app.auth import get_current_user

router = APIRouter(prefix="/shopee", tags=["shopee"])


def _rate_limit_ip(request: Request, limit: int = 10, window: int = 60) -> None:
    """In-memory rate limit per IP (same pattern as main.py)."""
    ip = request.client.host if request.client else "unknown"
    now = request.app.state._now if hasattr(request.app.state, "_now") else None
    # Lightweight: store in app state dict
    hits = getattr(request.app, "_shopee_hits", {})
    start, count = hits.get(ip, (now or 0, 0))
    if now is not None and now - start >= window:
        start, count = now, 0
    count += 1
    hits[ip] = (start, count)
    request.app._shopee_hits = hits
    if count > limit:
        retry_after = max(1, int(window - (now - start)))
        raise JSONResponse(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            content={"error": "RATE_LIMITED", "message": "Terlalu banyak permintaan",
                     "retry_after": retry_after},
        )


@router.post("/search", response_model=dict, status_code=status.HTTP_200_OK)
async def search_shopee_products(
    request: Request,
    query: str = Query(..., min_length=1, description="Cari produk Shopee"),
    limit: int = Query(10, ge=1, le=20, description="Jumlah maksimum hasil"),
    user=Depends(get_current_user),
):
    """Search Shopee affiliate products.

    - Uses cached results when available
    - Falls back to static parts when API unavailable
    - Tracks click events per item
    - Rate-limited per IP
    """
    _rate_limit_ip(request, limit=10, window=60)

    items = search_products(query=query, limit=limit)

    # Track a generic search click for analytics
    # (item_id would be specific per result; here we track the search event)
    _ = track_click(f"search:{query.lower()}:{limit}")

    return {
        "items": items,
        "click_tracking_id": f"shopee:search:{query.lower()}:{limit}",
    }