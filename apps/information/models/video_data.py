from django.db import models
from apps.common.models.mixins import DateTimeMixin
from apps.information.services.validator import validate_link, validate_video_format


class VideoData(DateTimeMixin):
    title = models.CharField(max_length=500, verbose_name='Название')
    video = models.FileField(upload_to='video', verbose_name='Видео')
    public_date = models.DateTimeField(verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    def clean(self):
        validate_video_format(self.video)

    def save(self, *args, **kwargs):
        self.clean()
        super(VideoData, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Видеогалерея'
        verbose_name_plural = 'Видеогалерея'
        ordering = ['-public_date']


class VideoLink(DateTimeMixin):
    title = models.CharField(max_length=500, verbose_name='Название')
    video_link = models.CharField(max_length=300, validators=[validate_link], verbose_name='Ссылка на видео')
    public_date = models.DateTimeField(verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео ссылка'
        verbose_name_plural = 'Видео ссылка'
        ordering = ['-public_date']
