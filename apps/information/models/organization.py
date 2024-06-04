from django.db import models
from apps.information.services.photo_compress import WEBPField
from apps.common.models.mixins import DateTimeMixin


class Organization(DateTimeMixin):
    title = models.TextField(verbose_name='название организации')
    logo = WEBPField(upload_to='logo', verbose_name='логотип')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Организации"
        verbose_name_plural = "Организации"
