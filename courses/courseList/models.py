from django.db import models

class course(models.Model):
    name = models.CharField(max_length= 50)
    description = models.TextField()
    instructor = models.CharField(max_length= 100)
    rating = models.IntegerField()

