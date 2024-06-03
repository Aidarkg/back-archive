from django.db import models
from apps.common.models.mixins import DateTimeMixin


class Logo(DateTimeMixin):
    logo = models.ImageField(upload_to='main_logo', verbose_name='Логотип')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Логотип'
        verbose_name_plural = 'Логотип'
        ordering = ['-created_at']
