from datetime import date

COUPONS = {
    "SAVE10": {"type": "percent", "value": 10, "expires": date(2099,1,1)},
    "FLAT5":  {"type": "flat", "value": 5, "expires": date(2099,1,1)},
    "OLD":    {"type": "percent", "value": 50, "expires": date(2000,1,1)},
}

def apply_coupon(subtotal: float, code: str | None) -> float:
    if not code:
        return round(subtotal, 2)
    c = COUPONS.get(code)
    if not c:
        return round(subtotal, 2)  # unknown coupon ignored for simplicity
    if c["expires"] < date.today():
        return round(subtotal, 2)
    if c["type"] == "percent":
        return round(subtotal * (1 - c["value"]/100.0), 2)
    if c["type"] == "flat":
        return round(max(0.0, subtotal - c["value"]), 2)
    return round(subtotal, 2)
