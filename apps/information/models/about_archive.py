from django.db import models
from apps.common.models.mixins import DateTimeMixin


class AboutArchive(DateTimeMixin):
    title = models.CharField('Название', max_length=300)
    description = models.TextField('Описание')
    photo = models.ImageField('Фото', upload_to='about_archive')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Об Архиве'
        verbose_name_plural = 'Об Архиве'
