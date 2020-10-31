from django.db import models


class Table(models.Model):
    class_name = models.TextField(default="two-top-horizontal")
    position_left = models.TextField(default="0px")
    position_top = models.TextField(default="0px")
    name = models.TextField(blank=True)
    restaurant_id = models.IntegerField(default=1, blank=True)
    status = models.TextField(default='done')
    reservation_id = models.IntegerField(blank=True, default=1)


