import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
import requests

#load config
with open("config.json") as f:
    config = json.load(f)["services"]
host = "0.0.0.0"
port = 8080
class ProxyHTTPRequestHandling(BaseHTTPRequestHandler):
    # Helper to add CORS headers safely
    def send_cors_headers(self, backend_headers=None):
        self.send_header('Content-Type', 'application/json')
        self.send_header("Access-Control-Allow-Origin", "*")

    # Handle preflight requests
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_cors_headers()
        self.end_headers()

    def do_GET(self):
        #parsing heard connections
        req_query = parse_qs(urlparse(self.path).query);
        query_service = req_query.get("service",[""])[0];
        #routing logic
        route = config.get(query_service)
        if not route:
            self.send_error(404,"No service was found")
            self.send_cors_headers()
            return
        
        # make outgoing connection
        route_url = route+self.path
        #timeout handling
        try:
            req = requests.get(route_url, timeout = 8)
        except requests.exceptions.ConnectTimeout as ct:
            self.send_response(408)
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(f"Connection timeout: {ct}".encode())
            return
        except requests.exceptions.Timeout as t:
            self.send_response(408)
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(f"Timeout exception: {t}".encode())
            return
        except requests.exceptions.RequestException as e:
            self.send_response(404)
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(f"Exception: {e}".encode())
            return

        self.send_response(req.status_code)
        #send headers, include headers if not received
        #(e.g. python totalvalidips implementation)
        for h_name,h_value in req.headers.items():
            if h_name.lower() not in ("transfer-encoding","connection"):
                self.send_header(h_name,h_value)
        self.send_cors_headers()
        self.end_headers()
        self.wfile.write(req.content)
print(f"Proxy running on port 8080\n")
HTTPServer((host,port),ProxyHTTPRequestHandling).serve_forever()

