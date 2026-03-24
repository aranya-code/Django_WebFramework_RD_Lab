from django.test import TestCase
from django.urls import reverse
from clinicalApp.models import Patient, ClinicalData
from clinicalApp.forms import PatientForm, ClinicalDataForm


# -----------------------------
# 🧠 MODEL TESTS
# -----------------------------
class ModelTestCase(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(name="John", age=30)
        self.clinical = ClinicalData.objects.create(
            componentName="Height",
            componentValue="180",
            patient=self.patient
        )

    def test_patient_creation(self):
        self.assertEqual(self.patient.name, "John")
        self.assertEqual(self.patient.age, 30)

    def test_patient_str(self):
        self.assertEqual(str(self.patient), "John")

    def test_clinical_data_creation(self):
        self.assertEqual(self.clinical.componentName, "Height")
        self.assertEqual(self.clinical.componentValue, "180")
        self.assertEqual(self.clinical.patient, self.patient)


# -----------------------------
# 🧾 FORM TESTS
# -----------------------------
class FormTestCase(TestCase):

    def test_patient_form_valid(self):
        form = PatientForm(data={'name': 'Alice', 'age': 25})
        self.assertTrue(form.is_valid())

    def test_patient_form_invalid(self):
        form = PatientForm(data={'name': '', 'age': ''})
        self.assertFalse(form.is_valid())

    def test_clinical_form_valid(self):
        patient = Patient.objects.create(name="Test", age=40)
        form = ClinicalDataForm(data={
            'componentName': 'Weight',
            'componentValue': '70',
            'patient': patient.id
        })
        self.assertTrue(form.is_valid())

    def test_clinical_form_invalid(self):
        form = ClinicalDataForm(data={})
        self.assertFalse(form.is_valid())


# -----------------------------
# 🌐 VIEW TESTS (CBVs)
# -----------------------------
class PatientViewTests(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(name="TestUser", age=35)

    def test_patient_list_view(self):
        response = self.client.get(reverse('Index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "TestUser")

    def test_patient_create_view(self):
        response = self.client.post(reverse('Create'), {
            'name': 'New Patient',
            'age': 28
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Patient.objects.count(), 2)

    def test_patient_update_view(self):
        response = self.client.post(reverse('Update', args=[self.patient.id]), {
            'name': 'Updated Name',
            'age': 40
        })
        self.assertEqual(response.status_code, 302)
        self.patient.refresh_from_db()
        self.assertEqual(self.patient.name, "Updated Name")

    def test_patient_delete_view(self):
        response = self.client.post(reverse('Delete', args=[self.patient.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Patient.objects.count(), 0)


# -----------------------------
# 🧪 FUNCTION VIEW TEST
# -----------------------------
class ClinicalDataViewTest(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(name="Patient1", age=50)

    def test_add_data_get(self):
        response = self.client.get(reverse('AddData', args=[self.patient.id]))
        self.assertEqual(response.status_code, 200)

    def test_add_data_post(self):
        response = self.client.post(reverse('AddData', args=[self.patient.id]), {
            'componentName': 'Blood Pressure',
            'componentValue': '120/80',
            'patient': self.patient.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ClinicalData.objects.count(), 1)