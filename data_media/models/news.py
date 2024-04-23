from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='news', verbose_name="Картинка")
    description = models.TextField(verbose_name="Краткое описание")
    detailed_description = models.TextField(verbose_name="полное описание")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"