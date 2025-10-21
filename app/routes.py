from flask import Blueprint, render_template, request, jsonify
from app.analyzer import analyze_log

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route('/analyze', methods=['POST'])

def analyze():
    # Check if file part is in request
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    # Read file content
    log_text = file.read().decode('utf-8', errors='ignore')

    # Analyze
    result = analyze_log(log_text)

    # Return JSON or HTML summary
    return jsonify(result)
