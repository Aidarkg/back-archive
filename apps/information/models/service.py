from django.db import models

from apps.common.models.mixins import DateTimeMixin


class Service(DateTimeMixin):
    title = models.TextField(verbose_name='Название')
    status = models.CharField(max_length=20, verbose_name='Статус')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
