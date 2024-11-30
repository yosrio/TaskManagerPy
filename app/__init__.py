from flask import Flask
from app.models import db
from app.routes import task_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()  # Tambahkan tanda kurung untuk memanggil fungsi

    app.register_blueprint(task_bp, url_prefix="/api")

    return app