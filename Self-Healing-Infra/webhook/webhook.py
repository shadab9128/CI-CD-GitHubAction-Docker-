from flask import Flask, request, jsonify
import subprocess
import logging
import os

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/", methods=["GET"])
def home():
    return "✅ Webhook server is running!"

@app.route("/webhook", methods=["GET"])
def webhook_status():
    return "✅ Webhook endpoint is live and ready to accept POST alerts."

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    logging.info(f"Received alert: {data}")

    try:
        alerts = data.get("alerts", [])
        for alert in alerts:
            alert_name = alert.get("labels", {}).get("alertname")
            if alert_name == "NginxDown":
                logging.info("Triggering Ansible playbook for NginxDown alert...")

                # Run ansible-playbook (make sure it's installed in the container)
                result = subprocess.run(
                    ["ansible-playbook", "restart-nginx.yaml"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )

                logging.info(f"Ansible output: {result.stdout}")
                if result.stderr:
                    logging.error(f"Ansible error: {result.stderr}")

        return jsonify({"status": "success"}), 200

    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5001)
