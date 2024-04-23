from django.db import models


class VideoData(models.Model):
    video = models.FileField(upload_to='video', verbose_name='видео')
    title = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата изменения')

    class Meta:
        verbose_name = 'Видео данные'
        verbose_name_plural = 'Видео данные'