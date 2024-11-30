from flask import Blueprint, jsonify, request
from app.models import Task, db

task_bp = Blueprint('tasks', __name__)

@task_bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    new_task = Task(
        title = data['title'],
        description = data.get('description'),
        due_date = data['due_date']
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201

@task_bp.route("/tasks", methods=["GET"])
def get_tasks():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    tasks = Task.query.paginate(page=page, per_page=per_page, error_out=False)
    response = {
        'items': [task.to_dict() for task in tasks.items],
        'pagination': {
            'page': tasks.page,
            'per_page': tasks.per_page,
            'total': tasks.total,
            'pages': tasks.pages
        }
    }
    return jsonify(response)

@task_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task Deleted"}), 200
