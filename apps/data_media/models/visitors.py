from django.utils import timezone

from django.db import models


class Visit(models.Model):
    date = models.DateField(default=timezone.now)
    count = models.IntegerField(default=0)
