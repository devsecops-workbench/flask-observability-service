from flask import Flask, jsonify
import psutil
import platform
import time

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "devops-sre-lab",
        "status": "running",
        "timestamp": time.time()
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory().percent,
        "system": platform.system(),
        "hostname": platform.node()
    })

@app.route("/metrics")
def metrics():
    return jsonify({
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory()._asdict(),
        "boot_time": psutil.boot_time()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)