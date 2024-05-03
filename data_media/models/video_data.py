from django.db import models


class VideoData(models.Model):
    video = models.FileField(upload_to='video', verbose_name='Видео')
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Видеогалерея'
        verbose_name_plural = 'Видеогалерея'