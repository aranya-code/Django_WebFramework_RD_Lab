from django.test import TestCase, Client
from django.urls import reverse
from .forms import userRegistration

class TestUserRegistrationForm(TestCase):
    def test_form_valid_data(self):
        # Test that the form accepts correctly formatted data
        form = userRegistration(data={
            'firstName': 'John',
            'lastName': 'Doe',
            'email': 'john.doe@example.com'
        })
        self.assertTrue(form.is_valid())

    def test_form_invalid_email(self):
        # Test that the form catches invalid email formats
        form = userRegistration(data={
            'firstName': 'John',
            'lastName': 'Doe',
            'email': 'not-an-email'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_form_empty_data(self):
        # Test that all required fields trigger validation errors if left blank
        form = userRegistration(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3) # Expecting errors for all 3 fields


class TestUserRegistrationView(TestCase):
    def setUp(self):
        self.client = Client()
        # Using the exact name defined in your urls.py
        self.url = reverse('User_Register')

    def test_user_registration_view_get(self):
        # Test that a GET request loads the page and passes an empty form to the template
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'formsApp/userform.html')
        self.assertIsInstance(response.context['form'], userRegistration)
    
    def test_user_registration_view_post_valid(self):
        # Test simulating a user filling out and submitting the form
        response = self.client.post(self.url, data={
            'firstName': 'Jane',
            'lastName': 'Smith',
            'email': 'jane.smith@example.com'
        })
        
        # Since your view currently just re-renders the template after success,
        # the status code should be 200 OK
        self.assertEqual(response.status_code, 200)
        
        # Check that the form passed into the context is valid
        self.assertTrue(response.context['form'].is_valid())