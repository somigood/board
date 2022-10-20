from django.db import models

class Point(models.Model):
  title = models.CharField(max_length=100)
  lat = models.FloatField()
  lng = models.FloatField()