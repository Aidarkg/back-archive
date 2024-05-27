from django.db import models
from apps.common.models.mixins import DateTimeMixin


class CollCenter(DateTimeMixin):
    number = models.CharField(max_length=100, verbose_name='Номер телефона')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Колл-центр'
        verbose_name_plural = 'Колл-центр'