from django.db import models


class KODEKS(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    pdf_file = models.FileField(upload_to='pdf_files/', verbose_name='Файл')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Кодекс'
        verbose_name_plural = 'Кодексы'