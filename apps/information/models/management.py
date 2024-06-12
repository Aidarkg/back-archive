from django.db import models
from apps.common.models.mixins import DateTimeMixin
import datetime


class Management(DateTimeMixin):
    full_name = models.CharField(
        max_length=300,
        verbose_name='полное имя'
    )
    image = models.ImageField(
        upload_to='managements_image',
        verbose_name='фотография'
    )
    position = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name='Должность'
    )
    start_year = models.PositiveSmallIntegerField(
        verbose_name='Год начала работы'
    )
    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дата рождения'
    )
    clas_chin = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name='Классный чин'
    )

    @property
    def end_year(self):
        current_year = datetime.datetime.now().year
        return current_year

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = 'Руководство'
        verbose_name_plural = 'Руководства'
        ordering = ('-created_at',)


class ManagementEducation(models.Model):
    year = models.PositiveSmallIntegerField(
        verbose_name='Год образования'
    )
    place = models.CharField(
        max_length=500,
        verbose_name='Место образования'
    )
    specialization = models.CharField(
        max_length=500,
        verbose_name='Специальность'
    )
    management = models.ForeignKey(
        'Management',
        on_delete=models.CASCADE,
        related_name='managements_education',
        null=True,
        blank=True,
        verbose_name='Образование сотрудника'
    )

    def __str__(self):
        return self.place

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'


class ManagementWork(models.Model):
    year = models.CharField(
        max_length=300,
        verbose_name='Годы работы'
    )
    place = models.CharField(
        max_length=500,
        verbose_name='Место работы'
    )
    position = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name='Должность'
    )
    management = models.ForeignKey(
        'Management',
        on_delete=models.CASCADE,
        related_name='managements_work',
        null=True,
        verbose_name='Опыт Работы сотрудника'
    )

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Деятельность'
        verbose_name_plural = 'Деятельность'
