from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .auth import login, is_strong_password
from .pricing import apply_coupon
from .db import get_product

app = FastAPI(title="Ecommerce API")

class LoginReq(BaseModel):
    username: str
    password: str

class AddToCartReq(BaseModel):
    product_id: int
    qty: int

class CheckoutReq(BaseModel):
    items: list[AddToCartReq]
    coupon: str | None = None

@app.post("/login")
def api_login(payload: LoginReq):
    res = login(payload.username, payload.password)
    if "token" in res:
        return {"ok": True, "token": res["token"]}
    raise HTTPException(status_code=401, detail="invalid_credentials")

@app.get("/password/strength")
def api_pwd_strength(pwd: str):
    return {"strong": is_strong_password(pwd)}

@app.post("/checkout")
def api_checkout(payload: CheckoutReq):
    subtotal = 0.0
    for item in payload.items:
        p = get_product(item.product_id)
        if not p:
            raise HTTPException(status_code=404, detail="product_not_found")
        subtotal += p["price"] * item.qty
    total = apply_coupon(subtotal, payload.coupon)
    return {"subtotal": round(subtotal,2), "total": total, "coupon": payload.coupon}
