from django.db import models
from apps.common.models.mixins import DateTimeMixin


class Anticore(DateTimeMixin):
    location = models.CharField(max_length=700, verbose_name='Местоположение')
    phone_number = models.CharField(max_length=100, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронная почта')

    def __str__(self):
        return self.location

    class Meta:
        verbose_name = 'Антикоррупционные дела'
        verbose_name_plural = 'Антикоррупционные дела'

