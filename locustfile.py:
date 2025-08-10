cat > locustfile.py <<'PY'
from locust import HttpUser, task, between
import random, string, json

def rand_path():
    return "/" + "".join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(3,15)))

def rand_payload():
    return {"data": "".join(random.choices(string.ascii_letters + string.digits, k=random.randint(20,200)))}

class WebsiteUser(HttpUser):
    wait_time = between(0.05, 0.5)

    @task(7)
    def get_rand(self):
        headers = {"User-Agent": random.choice([
            "Mozilla/5.0", "curl/7.64.1", "Wget/1.20.3"
        ])}
        self.client.get(rand_path(), headers=headers, name="GET /random")

    @task(3)
    def post_rand(self):
        payload = rand_payload()
        self.client.post("/api/data", json=payload, name="POST /api/data")
PY
