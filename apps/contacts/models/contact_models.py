from django.db import models
from apps.common.models.mixins import DateTimeMixin


class Contact(DateTimeMixin):
    address = models.CharField(max_length=300, verbose_name='Адрес')
    phone_number = models.CharField(max_length=100, verbose_name='Телефон')
    index = models.CharField(max_length=100, verbose_name='Индекс')
    fax = models.CharField(max_length=100, verbose_name='Факс')
    email = models.EmailField(verbose_name='Электронная почта')
    facebook = models.CharField(max_length=200, verbose_name='Facebook')

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
