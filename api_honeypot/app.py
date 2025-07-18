from flask import Flask, request
import logging
import os

app = Flask(__name__)
os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename="logs/api.log", level=logging.INFO)

@app.route('/api/data', methods=['POST'])
def api_data():
    logging.info(f"Received: {request.json}")
    return {"status": "ok"}, 200

@app.route('/')
def root():
    return "API Honeypot Running"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
