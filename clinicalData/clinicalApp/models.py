from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class ClinicalData(models.Model):
    COMPONENT_NAMES = [('Height','Height'),('Weight','Weight'),('Blood Pressure','Blood Pressure'),('HeartRate','Heart Rate')]
    componentName = models.CharField(choices=COMPONENT_NAMES,max_length=20)
    componentValue = models.CharField(max_length=20)
    measuredDate = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
