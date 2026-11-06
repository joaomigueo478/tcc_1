from flask import Flask, Blueprint,jsonify

app = Flask(__name__)
api = Blueprint("api", __name__, url_prefix="/api")

API_STATUS = ["OK", 201]

@api.get("/status")
def api_status():
    return jsonify({"status": API_STATUS[0]}), API_STATUS[1]

