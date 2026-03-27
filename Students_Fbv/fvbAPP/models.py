from django.db import models

class studentInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length= 100)
    score = models.FloatField()