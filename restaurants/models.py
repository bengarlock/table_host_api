from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.TextField(default='')
