from django.db import models
from apps.information.services.photo_compress import WEBPField
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


class PhotoHome(DateTimeMixin):
    title = models.CharField(max_length=300, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    photo = WEBPField(upload_to='gallery/home', verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Историческое фото'
        verbose_name_plural = 'Исторические фото'
        ordering = ['-created_at']
