from django.db import models
from django.contrib.postgres.fields import ArrayField
from books.models import Book

class Slot(models.Model):
    booked = models.BooleanField(default=False)
    time = models.TextField(default="5:00 PM")
    party_size = models.IntegerField(default=0)
    status = models.TextField(blank=True)
    tables = ArrayField(models.CharField(max_length=50, blank=True), size=8, blank=True)
    book_id = models.ForeignKey(Book, related_name="slots", on_delete=models.SET_NULL, null=True)



