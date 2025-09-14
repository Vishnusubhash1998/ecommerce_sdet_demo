import pytest
import requests

BASE = "http://localhost:8000"

# 🔹 Smoke test (critical quick check)
@pytest.mark.smoke
def test_login_success_smoke():
    """Smoke: check login endpoint is alive and returns a token"""
    r = requests.post(f"{BASE}/login", json={
        "username": "standard_user",
        "password": "Passw0rd!"
    })
    assert r.status_code == 200
    assert r.json().get("ok") is True
    assert "token" in r.json()


# 🔹 Full API test suite (regression-level)
def test_login_fail():
    r = requests.post(f"{BASE}/login", json={"username": "x", "password": "y"})
    assert r.status_code == 401


@pytest.mark.parametrize("coupon,expected_total", [
    ("SAVE10", 81.0),   # (20*2 + 50) = 90 → 10% off
    ("FLAT5", 85.0),
    (None, 90.0)
])
def test_checkout_totals(coupon, expected_total):
    payload = {
        "items": [
            {"product_id": 1, "qty": 2},
            {"product_id": 2, "qty": 1}
        ],
        "coupon": coupon
    }
    r = requests.post(f"{BASE}/checkout", json=payload)
    assert r.status_code == 200
    j = r.json()
    assert j["subtotal"] == 90.0
    assert j["total"] == expected_total
