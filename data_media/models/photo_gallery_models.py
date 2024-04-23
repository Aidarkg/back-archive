from django.db import models


class PhotoGallery(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False, verbose_name='Заголовок')
    description = models.TextField(max_length=1000, blank=False, null=False, verbose_name='Описание')
    picture = models.ImageField(blank=False, null=False, upload_to='gallery', verbose_name='Картинка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
