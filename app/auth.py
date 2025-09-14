import re

def is_strong_password(pwd: str) -> bool:
    if len(pwd) < 8:
        return False
    if not re.search(r"[A-Z]", pwd):
        return False
    if not re.search(r"[a-z]", pwd):
        return False
    if not re.search(r"\d", pwd):
        return False
    if not re.search(r"[^\w\s]", pwd):  # special char
        return False
    return True

def login(username: str, password: str) -> dict:
    # Very simple mock
    if username == "standard_user" and password == "Passw0rd!":
        return {"token": "fake-jwt-token"}
    return {"error": "invalid_credentials"}
