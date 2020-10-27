from django.db import models
from django.contrib.postgres.fields import ArrayField

class Book(models.Model):
    date = models.TextField(max_length=20)
    restaurant_id = models.IntegerField()
