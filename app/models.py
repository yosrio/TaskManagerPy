from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Task(db.Model):  # Mengubah kelas Task untuk mewarisi dari db.Model
    __tablename__ = 'tasks'  # Menambahkan nama tabel
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    due_date = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(10), default='pending')

    def __init__(self, title, description, due_date):  # Menambahkan konstruktor
        self.title = title
        self.description = description
        self.due_date = due_date

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }