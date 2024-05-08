from django.db import models

from common.models.mixins import DateTimeMixin


class VideoData(DateTimeMixin):
    video = models.FileField(upload_to='video', verbose_name='Видео')
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Видеогалерея'
        verbose_name_plural = 'Видеогалерея'

    def __str__(self):
        return self.title
