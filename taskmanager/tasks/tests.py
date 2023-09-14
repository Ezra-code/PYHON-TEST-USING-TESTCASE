from django.test import TestCase
from .models import Task

class TaskModelTestCase(TestCase):
    def setUp(self):
        Task.objects.create(title="Test Task", description="This is a test task.")

    def test_task_creation(self):
        task = Task.objects.get(title="Test Task")
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "This is a test task.")
        self.assertFalse(task.completed)

    def test_task_completion(self):
        task = Task.objects.get(title="Test Task")
        task.completed = True
        task.save()
        self.assertTrue(task.completed)
