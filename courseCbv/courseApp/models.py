from django.db import models
from django.urls import reverse

class course(models.Model):
    name = models.CharField(max_length= 50)
    description = models.TextField()
    instructor = models.CharField(max_length= 100)
    rating = models.IntegerField()

    def get_absolute_url(self):
        return reverse ('coursedetail', kwargs={'pk':self.pk})