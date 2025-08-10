cat > server.py <<'PY'
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import random, string, json

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type","text/plain")
        self.end_headers()
        data = ''.join(random.choices(string.ascii_letters + string.digits, k=128))
        self.wfile.write(f"OK {data}".encode())

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length) if length else b""
        self.send_response(200)
        self.send_header("Content-Type","application/json")
        self.end_headers()
        resp = {"status": "ok", "len": len(body)}
        self.wfile.write(json.dumps(resp).encode())

if __name__ == "__main__":
    server = ThreadedHTTPServer(("", 8000), SimpleHandler)
    print("Starting server on :8000")
    server.serve_forever()
PY
