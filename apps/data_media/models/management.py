from django.db import models
from apps.common.models.mixins import DateTimeMixin


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
    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дата рождения'
    )
    clas_chin = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Классный чин'
    )

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = 'Руководство'
        verbose_name_plural = 'Руководства'
        ordering = ('-created_at', )


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
    management = models.ForeignKey(
        'Management',
        on_delete=models.CASCADE,
        related_name='managements_education',
        null=True,
        blank=True,
        verbose_name='Образование сотрудника'
    )


class ManagementWork(models.Model):
    start_year = models.PositiveSmallIntegerField(
        blank=False,
        null=False,
        verbose_name='Год начало работы'
    )
    end_year = models.PositiveSmallIntegerField(
        blank=False,
        null=False,
        verbose_name='Год окончания работы'
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
    management = models.ForeignKey(
        'Management',
        on_delete=models.CASCADE,
        related_name='managements_work',
        null=True,
        verbose_name='Опыт Работы сотрудника'
    )
