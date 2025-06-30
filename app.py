import os
from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

def get_connected_devices():
    output = subprocess.check_output("arp -a", shell=True).decode()
    devices = []
    for line in output.splitlines():
        if "dynamic" in line:
            parts = line.split()
            devices.append({
                "ip": parts[0],
                "mac": parts[1]
            })
    return devices

@app.route("/devices")
def devices():
    return jsonify(get_connected_devices())

@app.route("/")
def home():
    return "API çalışıyor. /devices endpoint'ine gidin."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
