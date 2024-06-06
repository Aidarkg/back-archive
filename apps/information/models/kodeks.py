from django.db import models
from apps.common.models.mixins import DateTimeMixin


class KODEKS(DateTimeMixin):
    title = models.TextField(verbose_name='Название', max_length=300)
    pdf_file = models.FileField(upload_to='pdf_files', verbose_name='Файл')
    date_file = models.DateField(verbose_name='Дата')
    document_number = models.PositiveIntegerField(verbose_name='Номер документа')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'НПА'
        verbose_name_plural = 'НПА'
        ordering = ['-date_file']
