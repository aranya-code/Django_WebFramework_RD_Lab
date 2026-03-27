from django.test import TestCase
from django.contrib.auth.models import User, Permission
from .models import studentInfo


class StudentModelTest(TestCase):

    def setUp(self):
        self.student = studentInfo.objects.create(
            id=1,
            name="Aranya",
            score=95.5
        )

    def test_student_creation(self):
        self.assertEqual(self.student.name, "Aranya")
        self.assertEqual(self.student.score, 95.5)


class StudentViewTest(TestCase):

    def setUp(self):
        # Create user
        self.user = User.objects.create_user(
            username='testuser',
            password='password123'
        )

        # Create student
        self.student = studentInfo.objects.create(
            id=1,
            name="John",
            score=88.5
        )

    # 🔹 Login required test
    def test_index_requires_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    # 🔹 Index view
    def test_index_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John")

    # 🔹 Create GET
    def test_create_view_get(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 200)

    # 🔹 Create POST
    def test_create_view_post(self):
        self.client.login(username='testuser', password='password123')

        response = self.client.post('/create/', {
            'id': 2,
            'name': 'Alice',
            'score': 92.0
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(studentInfo.objects.count(), 2)

    # 🔹 Update view
    def test_update_view(self):
        self.client.login(username='testuser', password='password123')

        response = self.client.post(f'/update/{self.student.id}', {
            'id': 1,
            'name': 'Updated John',
            'score': 90.0
        })

        self.assertEqual(response.status_code, 302)

        self.student.refresh_from_db()
        self.assertEqual(self.student.name, 'Updated John')

    # 🔹 Delete without permission
    def test_delete_without_permission(self):
        self.client.login(username='testuser', password='password123')

        response = self.client.get(f'/delete/{self.student.id}')
        self.assertNotEqual(response.status_code, 200)

    # 🔹 Delete with permission
    def test_delete_with_permission(self):
        self.client.login(username='testuser', password='password123')

        permission = Permission.objects.get(codename='delete_studentinfo')
        self.user.user_permissions.add(permission)

        response = self.client.get(f'/delete/{self.student.id}')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(studentInfo.objects.count(), 1)

    # 🔹 Logout view
    def test_logout_view(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 200)