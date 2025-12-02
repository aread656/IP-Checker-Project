import csv
import os
from http.server import BaseHTTPRequestHandler,HTTPServer
import uuid

csvfile = "saved_addresses.csv"
if not os.path.exists(csvfile):
    with open(csvfile,"w",newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["id","ip"])

class HTTPHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        #if path is save
        #create id
        #get length from header
        #ips from rfile read decode strip
        #open with append and write
        #ssend repone and headers
        #else errors
        if self.path == "/save":
            id = str(uuid.uuid4())[:8]
            file_length = int(self.headers.get("Content-Length",0))
            ips = self.rfile.read(file_length).decode().strip()
            with open(csvfile,"a", newline = '',buffering = 1) as f:
                w = csv.writer(f)
                w.writerow([id,ips])
                f.flush()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json');
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(id.encode())
        else:
            self.send_error(404)
            self.log_error("Error occurred")
    def do_GET(self):
        #if path load
        #retrieve id
        #open file under read
        #check each row, write out headers&id
        #errors
        if self.path.startswith("/load"):
            try:
                id = self.path.split("id=")[1]
            except:
                self.send_error(404)
            with open(csvfile,"r",newline = '') as f:
                r = csv.DictReader(f)
                for row in r:
                    if row["id"] == id:
                        self.send_response(200)
                        self.send_header('Content-Type', 'application/json');
                        self.send_header('Access-Control-Allow-Origin', '*')
                        self.end_headers()
                        self.wfile.write(row["ip"].encode())
                        return
        else:
            self.send_error(404)

print("csv saving running")
HTTPServer(("",86),HTTPHandler).serve_forever();