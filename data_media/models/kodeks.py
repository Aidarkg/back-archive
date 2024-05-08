from django.db import models
from common.models.mixins import DateTimeMixin


class KODEKS(DateTimeMixin):
    title = models.CharField(max_length=100, verbose_name='Название')
    pdf_file = models.FileField(upload_to='pdf_files/', verbose_name='Файл')

    class Meta:
        verbose_name = 'Кодекс'
        verbose_name_plural = 'Кодексы'