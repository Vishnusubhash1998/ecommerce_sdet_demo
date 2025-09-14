import pytest
from app.auth import is_strong_password

@pytest.mark.parametrize("pwd,ok", [
    ("Passw0rd!", True),
    ("weak", False),
    ("NoNumber!", False),
    ("nonumberorspecial", False),
    ("Short1!", False),
])
def test_is_strong_password(pwd, ok):
    assert is_strong_password(pwd) == ok
