from django.db import models

# Create your models here.

class Movie(models.Model):
    rdate = models.DateField()
    Moviename = models.CharField(max_length = 20)
    hero = models.CharField(max_length = 20)
    heroine = models.CharField(max_length = 20)
    rating = models.IntegerField()
