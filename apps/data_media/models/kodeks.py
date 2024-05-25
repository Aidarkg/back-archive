from django.db import models
from apps.common.models.mixins import DateTimeMixin


class KODEKS(DateTimeMixin):
    title = models.TextField(verbose_name='Название')
    pdf_file = models.FileField(upload_to='pdf_files/', verbose_name='Файл')
    date_file = models.DateField(null=True, blank=True, verbose_name='Дата')
    document_number = models.IntegerField(null=True, blank=True, verbose_name='Номер документа')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кодекс'
        verbose_name_plural = 'Кодексы'
        ordering = ['-date_file']
