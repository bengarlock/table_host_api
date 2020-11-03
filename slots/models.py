from django.db import models
from django.contrib.postgres.fields import ArrayField
from books.models import Book
from guests.models import Guest

class Slot(models.Model):
    booked = models.BooleanField(default=False)
    time = models.TextField(default="5:00 PM")
    party_size = models.IntegerField(default=0)
    status = models.TextField(blank=True)
    reservation_notes = models.TextField(blank=True)
    tables = ArrayField(models.CharField(max_length=15), default=list, blank=True)
    book = models.ForeignKey(Book, related_name="slots", on_delete=models.SET_DEFAULT, default=1)
    guest = models.ForeignKey(Guest, related_name="slots", on_delete=models.SET_DEFAULT, default=1)

    # class Meta:
    #     ordering = ["time", "party_size"]
    #
    # def __str__(self):
    #     return '%s: %s' % (self.time, self.party_size )






