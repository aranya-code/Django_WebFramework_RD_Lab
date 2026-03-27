from django.test import TestCase
from django.urls import reverse
from .models import course

class CourseModelTest(TestCase):

    def setUp(self):
        self.course = course.objects.create(
            name="Django",
            description="Learn Django",
            instructor="Aranya",
            rating=5
        )

    def test_course_creation(self):
        self.assertEqual(self.course.name, "Django")
        self.assertEqual(self.course.rating, 5)


class CourseViewTest(TestCase):

    def setUp(self):
        self.course = course.objects.create(
            name="Python",
            description="Learn Python",
            instructor="John",
            rating=4
        )

    # 🔹 Test Home Page (renderCourse)
    def test_render_course(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python")

    # 🔹 Test Add Course (GET)
    def test_add_course_get(self):
        response = self.client.get('/add/')
        self.assertEqual(response.status_code, 200)

    # 🔹 Test Add Course (POST)
    def test_add_course_post(self):
        response = self.client.post('/add/', {
            'name': 'AI',
            'description': 'AI course',
            'instructor': 'Sam',
            'rating': 5
        })
        self.assertEqual(response.status_code, 302)  # redirect
        self.assertEqual(course.objects.count(), 2)

    # 🔹 Test Update Course
    def test_update_course(self):
        response = self.client.post(f'/update/{self.course.id}', {
            'name': 'Updated Python',
            'description': 'Updated',
            'instructor': 'John',
            'rating': 5
        })
        self.assertEqual(response.status_code, 302)

        self.course.refresh_from_db()
        self.assertEqual(self.course.name, 'Updated Python')

    # 🔹 Test Delete Course
    def test_delete_course(self):
        response = self.client.get(f'/delete/{self.course.id}')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(course.objects.count(), 0)