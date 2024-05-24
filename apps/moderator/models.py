from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .moderator_services import save_moderator
from apps.common.models.mixins import DateTimeMixin


class Moderator(DateTimeMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)

    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Имя пользователя"
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Электронная почта",
    )
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')

    class Meta:
        verbose_name = 'Модератор'
        verbose_name_plural = 'Модераторы'

    def save(self, *args, **kwargs):
        save_moderator(self, *args, **kwargs)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


@receiver(post_delete, sender=Moderator)
def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()
