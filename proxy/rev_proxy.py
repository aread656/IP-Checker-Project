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
    def do_GET(self):
        #parsing heard connections
        req_query = parse_qs(urlparse(self.path).query);
        query_service = req_query.get("service",[""])[0];
        #routing logic
        route = config.get(query_service)
        if not route:
            self.send_error(404,"No service was found")
            return
        #old logic backup
        """match query_service:
            case "total-ip":
                route = "http://localhost:70"
            case "empty-ip":
                route = "http://localhost:90"
            case "valid-ip":
                route = "http://localhost:81"
            case "bad-ip":
                route = "http://localhost:82"
            case "classify-ip":
                route = "http://localhost:83"
            case "country-ip":
                route = "http://localhost:84"
            case _:
                self.send_error(404,"IP address checker cannot be run on this address")
                return"""

        # make outgoing connection
        route_url = route+self.path
        #timeout handling
        try:
            req = requests.get(route_url, timeout = 8)
        except requests.exceptions.ConnectTimeout as ct:
            self.send_error(408, f"Connection timeout: {ct}")
            return
        except requests.exceptions.Timeout as t:
            self.send_error(408, f"Timeout exception {t}")
            return
        except requests.exceptions.RequestException as e:
            self.send_error(404, f"Exception: {e}")
            return
        #result returns to user
        self.send_response(req.status_code)
        #send headers, include headers if not received
        #(e.g. python totalvalidips implementation)
        for h_name,h_value in req.headers.items():
            if h_name.lower() not in ("transfer-encoding","connection"):
                self.send_header(h_name,h_value)
        if "Content-Type" not in req.headers:
            self.send_header("Content-Type", "application/json")
        if "Access-Control-Allow-Origin" not in req.headers:
            self.send_header("Access-Control-Allow-Origin","*")
        self.end_headers()
        self.wfile.write(req.content)
print(f"Proxy running on port 8080\n")
HTTPServer((host,port),ProxyHTTPRequestHandling).serve_forever()
