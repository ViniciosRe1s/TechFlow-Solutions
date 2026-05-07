from flask import Flask, request, jsonify

# Inicializa a aplicação Flask
app = Flask(__name__)

# Lista que armazena as tarefas do sistema
tasks = []

# Rota principal do sistema
@app.route("/")
def home():
    return "Sistema de Gerenciamento de Tarefas"

# Rota para listar tarefas
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

# Rota para adicionar tarefas
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

# Executa o sistema
if __name__ == "__main__":
    app.run(debug=True)