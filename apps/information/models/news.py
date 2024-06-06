from django.db import models

from apps.common.models.mixins import DateTimeMixin


class News(DateTimeMixin):
    title = models.CharField(verbose_name='Название', max_length=300)
    image = models.ImageField(upload_to='news', verbose_name="Картинка")
    description = models.TextField(verbose_name="Описание", max_length=1000)
    public_date = models.DateTimeField(verbose_name="Дата публикации")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        ordering = ['-public_date']
