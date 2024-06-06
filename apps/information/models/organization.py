from django.db import models

from apps.common.models.mixins import DateTimeMixin


class Organization(DateTimeMixin):
    title = models.CharField(max_length=300, verbose_name='Название организации')
    logo = models.ImageField(upload_to='logo', verbose_name='Логотип')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Организации"
        verbose_name_plural = "Организации"
