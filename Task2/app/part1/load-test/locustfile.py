from locust import HttpUser, task, between
# py 3.10

class ScaletestappUser(HttpUser):
    # wait_time = between(1, 5)
    wait_time = between(0.5, 2)
    
    @task(1)
    def get_root(self):
        self.client.get("/")

    @task(3)
    def simulate_load(self):
        self.client.get("/api/fake")