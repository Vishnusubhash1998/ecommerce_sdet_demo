import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from .pages import LoginPage, CheckoutPage

BASE_UI = "http://localhost:5500"  # e.g., if you serve static demo pages locally

@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    d = webdriver.Chrome(service=service, options=options)
    yield d
    d.quit()

def test_login_flow(driver):
    page = LoginPage(driver, BASE_UI)
    page.open()
    page.login("standard_user", "Passw0rd!")
    assert page.is_logged_in()

def test_checkout_coupon_flow(driver):
    page = CheckoutPage(driver, BASE_UI)
    page.open()
    page.apply_coupon("SAVE10")
    assert page.total_text() in {"81.00", "$81.00", "81"}  # tolerant assertion
