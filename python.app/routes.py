
from flask import jsonify, request
from services import TaskService
from validators import validate_task_title


def register_routes(app):

    @app.get("/")
    def home():
        return jsonify({
            "application": "Task Manager API",
            "message": "API is running",
            "endpoints": ["/tasks", "/health"]
        }), 200

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    @app.get("/tasks")
    def list_tasks():
        return jsonify({
            "tasks": TaskService.list_tasks()
        }), 200

    @app.post("/tasks")
    def create_task():
        payload = request.get_json(silent=True)

        if not isinstance(payload, dict):
            return jsonify({
                "error": "Request body must be a JSON object"
            }), 400

        title, error = validate_task_title(
            payload.get("title")
        )

        if error:
            return jsonify({"error": error}), 400

        task = TaskService.add_task(title)
        return jsonify({"task": task}), 201

    @app.delete("/tasks/<int:task_id>")
    def delete_task(task_id):
        deleted = TaskService.delete_task(task_id)

        if not deleted:
            return jsonify({
                "error": "Task not found"
            }), 404

        return jsonify({
            "message": "Task deleted"
        }), 200
