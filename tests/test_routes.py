import unittest
from app import create_app, db
from app.models import Task

class TaskAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_create_task(self):
        response = self.client.post("/api/tasks", json={
            "title": "Test Task",
            "description": "This is a test task",
            "due_date": "2024-12-01"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("Test Task", response.get_data(as_text=True))

    def test_get_tasks(self):
        response = self.client.get("/api/tasks")
        self.assertEqual(response.status_code, 200)
