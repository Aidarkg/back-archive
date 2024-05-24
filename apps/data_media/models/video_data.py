from django.db import models

from apps.common.models.mixins import DateTimeMixin


class VideoData(DateTimeMixin):
    video = models.FileField(upload_to='video', verbose_name='Видео')
    title = models.TextField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видеогалерея'
        verbose_name_plural = 'Видеогалерея'