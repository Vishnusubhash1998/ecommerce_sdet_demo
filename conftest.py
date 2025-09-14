# conftest.py
import subprocess, sys, time, socket, os
import pytest

def wait_for_port(host, port, timeout=20):
    start = time.time()
    while time.time() - start < timeout:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            try:
                s.connect((host, port))
                return True
            except OSError:
                time.sleep(0.3)
    return False

@pytest.fixture(scope="session", autouse=True)
def start_api_server():
    """Start FastAPI (uvicorn) for tests that hit http://localhost:8000."""
    proc = subprocess.Popen([sys.executable, "-m", "uvicorn", "app.api:app", "--port", "8000"])
    ok = wait_for_port("127.0.0.1", 8000, 25)
    if not ok:
        proc.terminate()
        pytest.skip("API server failed to start on :8000")
    yield
    proc.terminate()

@pytest.fixture(scope="session", autouse=True)
def start_static_server():
    """Start a simple static server for UI pages at http://localhost:5500 only if needed."""
    # Only start if your local HTML exists (avoid running needlessly)
    root = os.getcwd()
    needs_ui = os.path.exists(os.path.join(root, "login.html")) or os.path.exists(os.path.join(root, "checkout.html"))
    if not needs_ui:
        # Skip starting if you test a real site like saucedemo.com
        yield
        return
    proc = subprocess.Popen([sys.executable, "-m", "http.server", "5500"])
    ok = wait_for_port("127.0.0.1", 5500, 15)
    if not ok:
        proc.terminate()
        pytest.skip("Static server failed to start on :5500")
    yield
    proc.terminate()
