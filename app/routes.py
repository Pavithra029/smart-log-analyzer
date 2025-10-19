from flask import Blueprint, render_template, request, jsonify
from app.analyzer import analyze_log

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/analyze", methods=["POST"])
def analyze():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400
    
    log_text = file.read().decode("utf-8")
    result = analyze_log(log_text)
    return jsonify(result)
