from django.db import models
from apps.common.models.mixins import DateTimeMixin


class KODEKS(DateTimeMixin):
    title = models.TextField(verbose_name='Название')
    pdf_file = models.FileField(upload_to='pdf_files', verbose_name='Файл')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кодекс'
        verbose_name_plural = 'Кодексы'
