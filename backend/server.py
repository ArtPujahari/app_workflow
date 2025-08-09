from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

workflow_data = {
    "nodes": [],
    "edges": []
}

@app.route("/get_workflow", methods=["GET"])
def get_workflow():
    return jsonify(workflow_data)

@app.route("/save_workflow", methods=["POST"])
def save_workflow():
    global workflow_data
    workflow_data = request.json
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
