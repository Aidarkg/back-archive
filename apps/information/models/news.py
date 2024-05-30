from django.db import models

from apps.common.models.mixins import DateTimeMixin


class News(DateTimeMixin):
    title = models.TextField(verbose_name='Название')
    image = models.ImageField(upload_to='news', verbose_name="Картинка")
    description = models.TextField(verbose_name="Описание")
    public_date = models.DateTimeField(verbose_name="Дата публикации")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        ordering = ['-public_date']
