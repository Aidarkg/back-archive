from django.db import models


class Management(models.Model):
    full_name = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        verbose_name='полное имя'
    )
    image = models.ImageField(
        upload_to='managements_image',
        blank=False,
        null=False,
        verbose_name='фотография'
    )
    position = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Должность'
    )
    experience = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        default=0,
        verbose_name='Стаж'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = 'Руководство'
        verbose_name_plural = 'Руководства'
