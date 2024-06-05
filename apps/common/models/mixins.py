from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class DateTimeMixin(models.Model):
    created_at = models.DateTimeField(verbose_name='Дата создания', null=True, blank=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(DateTimeMixin, self).save(*args, **kwargs)
