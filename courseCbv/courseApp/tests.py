from django.test import TestCase
from django.urls import reverse
from courseApp.models import course


# -----------------------------
# 🧠 MODEL TESTS
# -----------------------------
class CourseModelTest(TestCase):

    def setUp(self):
        self.course = course.objects.create(
            name="Django",
            description="Learn Django framework",
            instructor="Aranya",
            rating=5
        )

    def test_course_creation(self):
        self.assertEqual(self.course.name, "Django")
        self.assertEqual(self.course.instructor, "Aranya")
        self.assertEqual(self.course.rating, 5)

    def test_get_absolute_url(self):
        url = self.course.get_absolute_url()
        self.assertEqual(url, reverse('coursedetail', kwargs={'pk': self.course.pk}))


# -----------------------------
# 🌐 VIEW TESTS (CBVs)
# -----------------------------
class CourseViewTests(TestCase):

    def setUp(self):
        self.course = course.objects.create(
            name="Python",
            description="Learn Python",
            instructor="John",
            rating=4
        )

    # ✅ List View
    def test_course_list_view(self):
        response = self.client.get(reverse('courselist'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python")

    # ✅ Detail View
    def test_course_detail_view(self):
        response = self.client.get(reverse('coursedetail', args=[self.course.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python")

    # ✅ Create View
    def test_course_create_view(self):
        response = self.client.post(reverse('coursecreate'), {
            'name': 'FastAPI',
            'description': 'Learn FastAPI',
            'instructor': 'Alice',
            'rating': 5
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(course.objects.count(), 2)

    # ✅ Update View
    def test_course_update_view(self):
        response = self.client.post(reverse('courseupdate', args=[self.course.id]), {
            'name': 'Updated Course',
            'description': 'Updated Desc',
            'instructor': 'Updated Instructor',
            'rating': 3
        })
        self.assertEqual(response.status_code, 302)

        self.course.refresh_from_db()
        self.assertEqual(self.course.name, "Updated Course")

    # ✅ Delete View
    def test_course_delete_view(self):
        response = self.client.post(reverse('coursedelete', args=[self.course.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(course.objects.count(), 0)


# -----------------------------
# ⚠️ EDGE CASE TESTS
# -----------------------------
class CourseEdgeCaseTests(TestCase):

    def test_invalid_create(self):
        response = self.client.post(reverse('coursecreate'), {
            'name': '',   # invalid
            'description': '',
            'instructor': '',
            'rating': ''
        })
        self.assertEqual(response.status_code, 200)  # stays on form
        self.assertEqual(course.objects.count(), 0)

    def test_nonexistent_detail(self):
        response = self.client.get(reverse('coursedetail', args=[999]))
        self.assertEqual(response.status_code, 404)