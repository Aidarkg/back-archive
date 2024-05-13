from django.db import models

from apps.common.models.mixins import DateTimeMixin


class PhotoGallery(DateTimeMixin):
    title = models.CharField(max_length=50, blank=False, null=False, verbose_name='Заголовок')
    description = models.TextField(max_length=1000, blank=False, null=False, verbose_name='Описание')
    picture = models.ImageField(blank=False, null=False, upload_to='gallery', verbose_name='Картинка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фотогалерея'
        verbose_name_plural = 'Фотогалерея'
