from django.db import models
from apps.common.models.mixins import DateTimeMixin


class ArchiveContact(DateTimeMixin):
    location = models.CharField(max_length=700, verbose_name='Местоположение')
    phone_number = models.CharField(max_length=100, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронная почта')

    def __str__(self):
        return self.location

    class Meta:
        verbose_name = 'Архив'
        verbose_name_plural = 'Архив'


class Reception(models.Model):
    weekdays = models.CharField(max_length=200, verbose_name='В будние дни')
    general = models.ForeignKey('ArchiveContact', on_delete=models.CASCADE, related_name='reception')  # Изменено здесь

    def __str__(self):
        return self.weekdays

    class Meta:
        verbose_name = 'Приём граждан'


class Schedule(models.Model):
    weekdays = models.CharField(max_length=200, verbose_name='В будние дни')
    _break = models.CharField(max_length=100, verbose_name='Перерыв')
    weekend = models.CharField(max_length=100, default='Выходной', verbose_name='Суббота и Воскресенье')
    general = models.ForeignKey('ArchiveContact', on_delete=models.CASCADE, related_name='schedule')  # Изменено здесь

    def __str__(self):
        return self.weekdays

    class Meta:
        verbose_name = 'График работы'


class ReadingRoom(models.Model):
    weekdays = models.CharField(max_length=200, verbose_name='В будние дни')
    general = models.ForeignKey('ArchiveContact', on_delete=models.CASCADE, related_name='reading_room')  # Изменено здесь

    def __str__(self):
        return self.weekdays

    class Meta:
        verbose_name = 'Читальный зал'
