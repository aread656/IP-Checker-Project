from flask import Flask, request, jsonify
from totalvalidips import totalValidIPs
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
PORT = 81
HOST = "0.0.0.0"

@app.route("/", methods = ["GET"])
def getTotalValidIPs():
    items = request.args.get('items','')
    ips = []
    for ip in items.split(','):
        ips.append(ip.strip())
    valid_ips = totalValidIPs(ips)
    return jsonify(totalValid = valid_ips)

if __name__ == "__main__":
    app.run(host = HOST,port = PORT)