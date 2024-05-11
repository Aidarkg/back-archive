from django.db import models

from apps.common.models.mixins import DateTimeMixin


class Contact(DateTimeMixin):
    address = models.CharField(max_length=255, verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name='Телефоны', blank=True, null=True)
    email = models.EmailField(verbose_name='Электронная почта', blank=True, null=True)
    work_time = models.CharField(max_length=100, verbose_name="Время работы")
    reception = models.CharField(max_length=100, verbose_name="Прием граждан")
    reading_room = models.CharField(max_length=100, verbose_name="Читальный зал")

    def __str__(self):
        return f"{self.address} - {self.email}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
