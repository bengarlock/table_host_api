from django.db import models

class Guest(models.Model):
    first_name = models.TextField(default='', max_length=50)
    last_name = models.TextField(default='', max_length=50)
    phone_number = models.TextField(default='')
    guest_notes = models.TextField(default='')
    root_user = models.BooleanField(default=False)

