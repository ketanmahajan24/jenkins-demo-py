 
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"""
        <html>
        <head><title>Python App</title></head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h1>🚀 App is running on port 5000</h1>
            <p>Deployed using Jenkins</p>
        </body>
        </html>
        """)

if __name__ == "__main__":
    print("Server running on http://localhost:5000")
    HTTPServer(("0.0.0.0", 5000), SimpleHandler).serve_forever()
