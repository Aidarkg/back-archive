from django.db import models

from apps.common.models.mixins import DateTimeMixin
from apps.information.services.video_data import cover_video, validate_link


class VideoData(DateTimeMixin):
    video = models.FileField(upload_to='video', verbose_name='Видео')
    title = models.CharField(verbose_name='Название', max_length=300)
    public_date = models.DateTimeField(verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видеогалерея'
        verbose_name_plural = 'Видеогалерея'
        ordering = ['-public_date']


class VideoLink(DateTimeMixin):
    title = models.CharField(verbose_name='Название', max_length=300)
    video_link = models.CharField(max_length=300, validators=[validate_link], verbose_name='Ссылка на видео')
    public_date = models.DateTimeField(verbose_name='Дата публикации')
    cover = models.ImageField(upload_to='video/cover', default=None, null=True, blank=True, verbose_name='Обложка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео ссылка'
        verbose_name_plural = 'Видео ссылка'
        ordering = ['-public_date']

    def save(self, *args, **kwargs):
        try:
            cover = cover_video.delay(self.video_link)
            self.cover = cover
        except Exception as e:
            pass
        super().save(*args, **kwargs)
