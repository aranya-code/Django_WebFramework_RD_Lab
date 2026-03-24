from django.test import TestCase
from django.urls import reverse
from .models import formCreation
from .forms import modelFormCreation
from datetime import date

class FormCreationModelTest(TestCase):

    def setUp(self):
        self.obj = formCreation.objects.create(
            startDate=date(2026, 1, 1),
            endDate=date(2026, 1, 10),
            name="Test Task",
            assignedTo="Aranya",
            priority=1
        )

    def test_object_creation(self):
        self.assertEqual(self.obj.name, "Test Task")
        self.assertEqual(self.obj.assignedTo, "Aranya")
        self.assertEqual(self.obj.priority, 1)

    def test_date_fields(self):
        self.assertLess(self.obj.startDate, self.obj.endDate)
   

class ModelFormCreationTest(TestCase):


    def test_valid_form(self):
        form = modelFormCreation(data={
            "startDate": "2026-01-01",
            "endDate": "2026-01-10",
            "name": "Valid Task",
            "assignedTo": "User",
            "priority": 2
        })
        self.assertTrue(form.is_valid())

    def test_invalid_missing_fields(self):
        form = modelFormCreation(data={})
        self.assertFalse(form.is_valid())

    def test_invalid_priority_type(self):
        form = modelFormCreation(data={
            "startDate": "2026-01-01",
            "endDate": "2026-01-10",
            "name": "Task",
            "assignedTo": "User",
            "priority": "high"
        })
        self.assertFalse(form.is_valid())
    

class IndexViewTest(TestCase):

  
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    

class ProductsViewTest(TestCase):


    def setUp(self):
        formCreation.objects.create(
            startDate="2026-01-01",
            endDate="2026-01-10",
            name="Task1",
            assignedTo="User1",
            priority=1
        )

    def test_products_view(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Task1")


class AddProductViewTest(TestCase):

    def test_get_request(self):
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 200)

    def test_post_valid(self):
        response = self.client.post(reverse('add_product'), {
            "startDate": "2026-01-01",
            "endDate": "2026-01-10",
            "name": "New Task",
            "assignedTo": "User",
            "priority": 1
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(formCreation.objects.count(), 1)

    def test_post_invalid(self):
        response = self.client.post(reverse('add_product'), {
            "name": ""
        })
        self.assertEqual(formCreation.objects.count(), 0)
   
