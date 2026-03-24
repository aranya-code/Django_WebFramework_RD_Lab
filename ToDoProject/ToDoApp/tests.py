from django.test import TestCase
from django.urls import reverse
from ToDoApp.models import ToDo


class ToDoModelTest(TestCase):

    def setUp(self):
        self.todo = ToDo.objects.create(
            name="Aranya",
            task="Write test cases",
            completed=False
        )

    def test_todo_creation(self):
        self.assertEqual(self.todo.name, "Aranya")
        self.assertEqual(self.todo.task, "Write test cases")
        self.assertFalse(self.todo.completed)

    def test_string_representation(self):
        self.assertEqual(str(self.todo), "Write test cases")


class ToDoViewTest(TestCase):

    def setUp(self):
        self.todo = ToDo.objects.create(
            name="Test User",
            task="Sample Task",
            completed=False
        )

    def test_add_task_get_request(self):
        response = self.client.get(reverse('Index'))
        self.assertEqual(response.status_code, 200)

    def test_add_task_post_request(self):
        response = self.client.post(reverse('Index'), {
            'name': 'New User',
            'task': 'New Task'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(ToDo.objects.count(), 2)

    def test_get_tasks_view(self):
        response = self.client.get(reverse('TaskList'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Task")

    def test_mark_task_completed(self):
        response = self.client.get(reverse('Cross', args=[self.todo.id]))
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.completed)
        self.assertEqual(response.status_code, 302)

    def test_mark_task_incomplete(self):
        self.todo.completed = True
        self.todo.save()

        response = self.client.get(reverse('Uncross', args=[self.todo.id]))
        self.todo.refresh_from_db()
        self.assertFalse(self.todo.completed)
        self.assertEqual(response.status_code, 302)