from django.db import models

class Book(models.Model):
    date = models.TextField(max_length=20)
    restaurant_id = models.IntegerField()