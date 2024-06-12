from django.db import models
from apps.common.models.mixins import DateTimeMixin
from apps.information.services.photo_compress import WEBPField
from apps.information.services.exception import EmblemException


class Logo(DateTimeMixin):
    name = models.CharField(max_length=20, default='Логотип', verbose_name='Название')
    logo = WEBPField(upload_to='main_logo', verbose_name='Логотип')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk and Emblem.objects.all().count() >= 1:
            raise EmblemException('Можно добавить только одно фото!')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Логотип'
        verbose_name_plural = 'Логотип'
        ordering = ['-created_at']


class Emblem(models.Model):
    emblem = models.ImageField(upload_to='main_logo/emblem', verbose_name='Герб')
    logo = models.ForeignKey(Logo, on_delete=models.CASCADE, verbose_name='Лого')

    def __str__(self):
        return self.emblem.name

    def save(self, *args, **kwargs):
        if not self.pk and Emblem.objects.all().count() >= 1:
            raise EmblemException('Можно добавить только одно фото!')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Герб'
        verbose_name_plural = 'Герб'
