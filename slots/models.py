from django.db import models
from django.contrib.postgres.fields import ArrayField


class Slot(models.Model):
    booked = models.BooleanField(default=False)
    time = models.TextField(default="5:00 PM")
    party_size = models.IntegerField(default=0)
    status = models.TextField(default="")
    tables = ArrayField(models.CharField(max_length=10, blank=True), size=8, default='')


