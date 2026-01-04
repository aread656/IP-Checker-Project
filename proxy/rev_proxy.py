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
    def send_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods","GET,POST,OPTIONS")
        self.send_header("Access-Control-Allow-Headers","*")

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
        for h_name, h_value in req.headers.items():
            lname = h_name.lower()
            if lname in (
                "transfer-encoding",
                "connection",
                "access-control-allow-origin",
                "access-control-allow-methods",
                "access-control-allow-headers"
            ):
                continue
            self.send_header(h_name, h_value)        
        self.send_cors_headers()
        self.end_headers()
        self.wfile.write(req.content)

    def do_POST(self):
        #get query
        #get "service" from url
        #make route
        #handle no route
        #content_length
        #body = self.rfile.read(length)
        #do responses
        req_query = parse_qs(urlparse(self.path).query)
        query_service = req_query.get("service",[""])[0]
        route = config.get(query_service)
        if not route:
            self.send_response(404)
            self.send_cors_headers()
            self.end_headers()
            return
        length = int(self.headers.get("Content-Length",0))
        data = self.rfile.read(length)

        try:
            req = requests.post(route,timeout=8,data=data)
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
        for h_name, h_value in req.headers.items():
            lname = h_name.lower()
            if lname in (
                "transfer-encoding",
                "connection",
                "access-control-allow-origin",
                "access-control-allow-methods",
                "access-control-allow-headers"
            ):
                continue
            self.send_header(h_name, h_value)        
        self.send_cors_headers()
        self.end_headers()
        self.wfile.write(req.content)

    
print(f"Proxy running on port 8080\n")
HTTPServer((host,port),ProxyHTTPRequestHandling).serve_forever()

