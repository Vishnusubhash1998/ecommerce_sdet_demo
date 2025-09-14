from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self):
        self.driver.get(self.base_url + "/login.html")

    def login(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "submit").click()

    def is_logged_in(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "dashboard")))
        return True

class CheckoutPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self):
        self.driver.get(self.base_url + "/checkout.html")

    def apply_coupon(self, code):
        self.driver.find_element(By.ID, "coupon").clear()
        self.driver.find_element(By.ID, "coupon").send_keys(code)
        self.driver.find_element(By.ID, "apply").click()

    def total_text(self):
        el = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "total")))
        return el.text
