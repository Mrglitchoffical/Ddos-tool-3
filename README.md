# First Install Your Machine 

```
mkdir ~/Ddos-tool-3 && cd ~/Ddos-tool-3
```
```
python attack.py 192.0.0.1 10001
```
# Ctrl+C to stop
```
python3 server.py
```
# 2) Virtualenv + Locust install (recommended)
```
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install locust
```
```pkg install python```
# start locust UI, open http://localhost:8089 in browser
```
locust -f locustfile.py --host http://127.0.0.1:8000
```
### example: 200 users, spawn 50 users/sec, run 2 minutes, export CSV prefix "run1"
```
locust -f locustfile.py --host http://127.0.0.1:8000 --headless --users 200 --spawn-rate 50 --run-time 2m --csv=run1
```
```run1_stats.csv,run1_failures.csv```
# Install (Ubuntu example) and run:
```
sudo apt update
sudo apt install build-essential libssl-dev -y
```
# install wrk (build from source
```
git clone https://github.com/wg/wrk.git
cd wrk && make
sudo cp wrk /usr/local/bin/
```
# run wrk: -t threads, -c connections, -d duration
```
wrk -t4 -c200 -d30s http://127.0.0.1:8000/
```
# CPU / processes
```
htop
```
# Network usage (may need sudo)
```
sudo iftop -i eth0   # replace eth0 with correct interface
```
# socket summary
```
ss -s
```
# simple live IO/CPU
```
vmstat 1
```
