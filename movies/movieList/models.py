from django.db import models

class movie(models.Model):
    # Creating model for movie
    name = models.CharField(max_length= 100)
    releaseDate = models.DateField()
    rating = models.IntegerField()
