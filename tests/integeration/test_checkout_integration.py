from app.pricing import apply_coupon
from app.db import get_product

def test_checkout_math_integration():
    # emulate cart calc + coupon
    p1 = get_product(1)  # $20
    p2 = get_product(2)  # $50
    subtotal = p1["price"]*2 + p2["price"]*1  # 20*2 + 50 = 90
    total = apply_coupon(subtotal, "SAVE10")  # 10% off
    assert subtotal == 90.0
    assert total == 81.0
