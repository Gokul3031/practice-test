from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Python app running")

def run():
    server = HTTPServer(("0.0.0.0", 8000), Handler)
    print("Python app started on port 8000:)")
    server.serve_forever()

if __name__ == "__main__":
    run()
