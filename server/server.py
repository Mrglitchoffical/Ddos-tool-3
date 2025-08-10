from http.server import HTTPServer, BaseHTTPRequestHandler
import random
import string
import threading

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.log_request()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        random_data = ''.join(random.choices(string.ascii_letters + string.digits, k=50))
        self.wfile.write(f"GET Response: {random_data}".encode())

    def do_POST(self):
        self.log_request()
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length) if content_length > 0 else b""
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        response = {
            "status": "success",
            "received": post_data.decode(errors="ignore"),
            "random": ''.join(random.choices(string.ascii_letters + string.digits, k=20))
        }
        self.wfile.write(str(response).encode())

    def log_request(self, code='-', size='-'):
        print(f"[{self.client_address[0]}] {self.command} {self.path}")

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Starting HTTP server on port {port}... Press Ctrl+C to stop.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")

if __name__ == "__main__":
    run_server()
