from django.db import models

from apps.common.models.mixins import DateTimeMixin

ISFREE = (
    ('free', 'Беслатно'),
    ('paid', 'Платно')
)


class Service(DateTimeMixin):
    title = models.TextField(verbose_name='Название')
    status = models.CharField(max_length=20, verbose_name='Статус')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги '

    def __str__(self):
        return self.title
