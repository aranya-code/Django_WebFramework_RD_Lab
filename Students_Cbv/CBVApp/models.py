from django.db import models
from django.urls import reverse

class studentInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length= 100)
    score = models.FloatField()

    def get_absolute_url(self):
        return reverse ('detail', kwargs={'pk':self.pk})