# flask_log_ip_example.py
# Simple Flask app that shows and logs visitor IPs (for your own testing / consented users)
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(filename='visitors.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

@app.route('/')
def index():
    # Get the client's IP as seen by the server
    ip = request.remote_addr
    # If behind proxies, you might check X-Forwarded-For (only if you control the proxy)
    forwarded = request.headers.get('X-Forwarded-For', '')
    logging.info(f"Visitor IP: {ip} X-Forwarded-For: {forwarded} Path: {request.path}")
    return jsonify({"message": "Hello — you agreed to this test", "your_ip": ip, "x_forwarded_for": forwarded})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
