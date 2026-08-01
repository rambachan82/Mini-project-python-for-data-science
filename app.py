from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Sample in-memory data store
tasks = [
    {"id": 1, "title": "Connect Python backend to Frontend"},
    {"id": 2, "title": "Style layout with CSS"},
    {"id": 3, "title": "Add interactivity with JavaScript"}
]

# Route to render the main HTML page
@app.route("/")
def home():
    return render_template("index.html")

# API Endpoint: Get all tasks
@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

# API Endpoint: Add a new task
@app.route("/api/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    if not data or "title" not in data or not data["title"].strip():
        return jsonify({"error": "Task title cannot be empty"}), 400
    
    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"].strip()
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

if __name__ == "__main__":
    app.run(debug=True, port=5000)