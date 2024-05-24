from django.db import models

from apps.common.models.mixins import DateTimeMixin


class Photo(models.Model):
    gallery = models.ForeignKey('PhotoGallery', on_delete=models.CASCADE, related_name='photo')
    photo = models.ImageField(upload_to='gallery/photos', verbose_name='Изображение')

    def __str__(self):
        return f"Photo {self.id}"


class PhotoGallery(DateTimeMixin):
    title = models.TextField(verbose_name='Заголовок')
    description = models.TextField(max_length=1000, blank=False, null=False, verbose_name='Описание')
    picture = models.ImageField(blank=False, null=False, upload_to='gallery/logo', verbose_name='Картинка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фотогалерея'
        verbose_name_plural = 'Фотогалерея'

    def count_photo(self):
        return self.photo.count()
