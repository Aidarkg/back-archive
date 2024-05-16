from django.db import models

from apps.common.models.mixins import DateTimeMixin


class News(DateTimeMixin):
    title = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='news', verbose_name="Картинка")
    description = models.TextField(verbose_name="Краткое описание")
    detailed_description = models.TextField(verbose_name="Полное описание")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата публикации")
    updated_at = models.DateField(auto_now_add=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"