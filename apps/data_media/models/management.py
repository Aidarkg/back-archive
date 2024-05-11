from django.db import models
from apps.common.models.mixins import DateTimeMixin


class ManagementEducation(models.Model):
    year = models.PositiveSmallIntegerField(
        blank=False,
        null=False,
        verbose_name='Год образования'
    )
    place = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name='Место образования'
    )
    specialization = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Специальность'
    )


class ManagementWork(models.Model):
    start_year = models.DateField(
        blank=False,
        null=False,
        verbose_name=''
    )
    end_year = models.DateField(
        blank=False,
        null=False,
        verbose_name=''
    )
    place = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name='Место работы'
    )
    position = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Должность'
    )


class Management(DateTimeMixin):
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
    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дата рождения'
    )


    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = 'Руководство'
        verbose_name_plural = 'Руководства'
