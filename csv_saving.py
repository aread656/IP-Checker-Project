import csv
import os
from http.server import BaseHTTPRequestHandler,HTTPServer
import uuid
import json

csvfile = "saved_addresses.csv"
if not os.path.exists(csvfile):
    with open(csvfile,"w",newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["id","ips"])

class HTTPHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/save":
            id = str(uuid.uuid4())[:8]
            file_length = int(self.headers.get("Content-Length",0))
            ips = self.rfile.read(file_length).decode().strip()
            if not ips:
                self.send_error(404,"IPs not given")
                return
            with open(csvfile,"a", newline = '',buffering = 1) as f:
                w = csv.writer(f)
                w.writerow([id,ips])
                f.flush()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json');
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            res = {"id":id,"ips":ips}
            self.wfile.write(json.dumps(res).encode())
        else:
            self.send_error(404,"Path not found")
    def do_GET(self):
        if self.path.startswith("/load"):
            try:
                id = self.path.split("id=")[1]
            except:
                self.send_error(404,"ID not found")
                return
            with open(csvfile,"r",newline = '') as f:
                r = csv.DictReader(f)
                for row in r:
                    if row["id"] == id:
                        self.send_response(200)
                        self.send_header('Content-Type', 'application/json');
                        self.send_header('Access-Control-Allow-Origin', '*')
                        self.end_headers()
                        res = {"id":id,"ips":row["ips"]}
                        self.wfile.write(json.dumps(res).encode())
                        return
        else:
            self.send_error(404,"Path not found")
    def send_error(self, code, message=None):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps({"error": True, "message": message}).encode())


print("csv saving running")
HTTPServer(("",86),HTTPHandler).serve_forever();