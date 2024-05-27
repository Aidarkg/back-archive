from django.db import models
from apps.data_media.services.photo_compress import WEBPField
from apps.common.models.mixins import DateTimeMixin


class Photo(models.Model):
    gallery = models.ForeignKey('PhotoGallery', on_delete=models.CASCADE, related_name='photo')
    photo = WEBPField(upload_to='gallery/photos', verbose_name='Изображение')

    def __str__(self):
        return f"Photo {self.id}"


class PhotoGallery(DateTimeMixin):
    title = models.TextField(verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    picture = WEBPField(upload_to='gallery/logo', verbose_name='Картинка')
    public_date = models.DateTimeField(verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фотогалерея'
        verbose_name_plural = 'Фотогалерея'
        ordering = ['-public_date']

    def count_photo(self):
        return self.photo.count()
