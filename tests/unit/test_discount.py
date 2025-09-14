import pytest
from app.pricing import apply_coupon

@pytest.mark.parametrize("subtotal,code,expected", [
    (100.0, "SAVE10", 90.0),
    (50.0,  "FLAT5",  45.0),
    (80.0,  "OLD",    80.0),   # expired ignored
    (20.0,  None,     20.0),
    (20.0,  "UNKNOWN",20.0),
])
def test_apply_coupon(subtotal, code, expected):
    assert apply_coupon(subtotal, code) == expected
