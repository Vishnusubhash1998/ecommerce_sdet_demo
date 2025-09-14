from locust import HttpUser, task, between

class Shopper(HttpUser):
    wait_time = between(1, 3)

    @task(2)
    def login(self):
        self.client.post("/login", json={
            "username": "standard_user",
            "password": "Passw0rd!"
        })

    @task(3)
    def checkout(self):
        self.client.post("/checkout", json={
            "items": [{"product_id": 1, "qty": 2}, {"product_id": 2, "qty": 1}],
            "coupon": "SAVE10"
        })
