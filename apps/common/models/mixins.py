from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class DateTimeMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', null=True, blank=True)

    class Meta:
        abstract = True
