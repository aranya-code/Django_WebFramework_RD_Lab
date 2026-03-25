from django.test import TestCase
from django.urls import reverse
from CBVApp.models import studentInfo


# -----------------------------
# 🧠 MODEL TESTS
# -----------------------------
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

    def test_get_absolute_url(self):
        url = self.student.get_absolute_url()
        self.assertEqual(url, reverse('detail', kwargs={'pk': self.student.pk}))  # :contentReference[oaicite:0]{index=0}


# -----------------------------
# 🌐 VIEW TESTS (CBVs)
# -----------------------------
class StudentViewTests(TestCase):

    def setUp(self):
        self.student = studentInfo.objects.create(
            id=1,
            name="Test Student",
            score=88.0
        )

    # ✅ List View
    def test_student_list_view(self):
        response = self.client.get(reverse('student'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Student")

    # ✅ Detail View
    def test_student_detail_view(self):
        response = self.client.get(reverse('detail', args=[self.student.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Student")

    # ✅ Create View
    def test_student_create_view(self):
        response = self.client.post('/create/', {
            'id': 2,
            'name': 'New Student',
            'score': 90
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(studentInfo.objects.count(), 2)

    # ✅ Update View
    def test_student_update_view(self):
        response = self.client.post(f'/update/{self.student.id}/', {
            'name': 'Updated Student',
            'score': 75
        })
        self.assertEqual(response.status_code, 302)

        self.student.refresh_from_db()
        self.assertEqual(self.student.name, "Updated Student")

    # ✅ Delete View
    def test_student_delete_view(self):
        response = self.client.post(f'/delete/{self.student.id}/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(studentInfo.objects.count(), 0)


# -----------------------------
# ⚠️ EDGE CASE TESTS
# -----------------------------
class StudentEdgeCaseTests(TestCase):

    def test_invalid_create(self):
        response = self.client.post('/create/', {
            'id': '',
            'name': '',
            'score': ''
        })
        self.assertEqual(response.status_code, 200)  # stays on form
        self.assertEqual(studentInfo.objects.count(), 0)

    def test_nonexistent_detail(self):
        response = self.client.get(reverse('detail', args=[999]))
        self.assertEqual(response.status_code, 404)