from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task
from rest_framework.test import APIClient


class TaskModelTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username = 'testuser', password='testpassword')

    def test_create_task(self):
        task = Task.objects.create(
            title='Test Task',
            description= 'This is a test task',
            completed=False,
            user=self.user
        )
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.user.username, 'testuser')
        self.assertFalse(task.completed)

    def test_task_api(self):
        data = {
            'title' : 'API Test Task',
            'description' : 'Task created via API',
            'completed' : False,
            'user' : self.user.id
        }

        response = self.client.post('/api/tasks/',data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['title'], 'API Test Task')