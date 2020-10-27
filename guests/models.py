from django.db import models

class Guest(models.Model):
    first_name = models.TextField(default='', max_length=50, blank=True)
    last_name = models.TextField(default='', max_length=50, blank=True)
    phone_number = models.TextField(default='', blank=True)
    guest_notes = models.TextField(default='', blank=True)
    root_user = models.BooleanField(default=False, blank=True)

