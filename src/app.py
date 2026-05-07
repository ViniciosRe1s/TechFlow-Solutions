from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return "Sistema de Gerenciamento de Tarefas"

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json

    if not data.get("title"):
        return jsonify({"error": "Título obrigatório"}), 400

    task = {
        "id": len(tasks) + 1,
        "title": data["title"]
    }

    tasks.append(task)

    return jsonify(task), 201

if __name__ == "__main__":
    app.run(debug=True)