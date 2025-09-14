# app/db.py
def get_product(product_id: int):
    """Dummy DB lookup for product info"""
    products = {
        1: {"name": "Shoes", "price": 20.0},
        2: {"name": "Bag", "price": 50.0}
    }
    return products.get(product_id, None)
