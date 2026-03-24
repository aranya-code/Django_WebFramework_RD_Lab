from django.db import models

class formCreation(models.Model):
    startDate = models.DateField()
    endDate = models.DateField()
    name = models.CharField(max_length= 50)
    assignedTo = models.CharField(max_length= 30)
    priority = models.IntegerField()