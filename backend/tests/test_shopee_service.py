"""Unit tests for Shopee affiliate service (UTM, static fallback, click tracking)."""
from app.services.shopee import (
    STATIC_PARTS,
    generate_affiliate_link,
    search_products,
    track_click,
)


def test_generate_affiliate_link_has_utm_params():
    link = generate_affiliate_link("static-1", source="web", campaign="summer")
    assert "utm_source=web" in link
    assert "utm_medium=affiliate" in link
    assert "utm_campaign=summer" in link


def test_generate_affiliate_link_uses_defaults():
    link = generate_affiliate_link("static-2")
    assert "utm_source=web" in link
    assert "utm_campaign=affiliate" in link


def test_generate_affiliate_link_unknown_item_raises():
    try:
        generate_affiliate_link("tidak-ada")
    except ValueError as exc:
        assert "Tidak dapat menemukan link afiliasi" in str(exc)
    else:
        raise AssertionError("Expected ValueError for unknown item_id")


def test_track_click_increments():
    track_click("static-1")
    track_click("static-1")
    assert track_click("static-1") == 3


def test_static_parts_have_required_fields():
    for part in STATIC_PARTS:
        for key in ("item_id", "name", "shopee_url"):
            assert key in part and part[key]


def test_search_products_returns_static_fallback(monkeypatch):
    import app.services.shopee as svc

    monkeypatch.setattr(svc, "_call_shopee_api", lambda *a, **k: None)
    items = search_products("oli mesin", limit=2)
    assert len(items) == 2
    assert all("item_id" in i for i in items)
