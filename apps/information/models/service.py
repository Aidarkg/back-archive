from django.db import models

from apps.common.models.mixins import DateTimeMixin


class Service(DateTimeMixin):
    title = models.CharField(max_length=500, verbose_name='Название')
    status = models.CharField(max_length=20, verbose_name='Статус')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class PriceList(DateTimeMixin):
    title = models.CharField(max_length=50, default='Прейскурант услуг', verbose_name='Название')
    file = models.FileField(upload_to='prices', verbose_name='Файл')

    class Meta:
        verbose_name = 'Прейскурант услуг'
        verbose_name_plural = 'Прейскурант услуг'

    def __str__(self):
        return self.title
