import random
import string
from django.db import models
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db import transaction


def validate_username(value):
    if User.objects.filter(username=value):
        raise ValidationError("Модератор с таким именем уже существует.")

def validate_email(value):
    if User.objects.filter(email=value):
        raise ValidationError("Модератор с такой электронной почтой уже существует.")


class Moderator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)

    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[validate_username],
        error_messages={"unique": "Модератор с таким именем уже существует."},
        verbose_name="Имя пользователя"
    )
    email = models.EmailField(
        validators=[validate_email],
        unique=True,
        error_messages={"unique": "Модератор с такой электронной почтой уже существует."},
        verbose_name="Электронная почта",
        )
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')

    class Meta:
        verbose_name = 'Модератор'
        verbose_name_plural = 'Модераторы'

    @staticmethod
    def generate_password(length=20):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        return password

    def save(self, *args, **kwargs):
        if self.user_id:
            user = self.user
            user.username = self.username
            user.email = self.email
            user.save()

            user.groups.clear()
            user.groups.add(self.group)

        else:
            password = self.generate_password()
            user = User.objects.create_user(
                username=self.username,
                email=self.email,
                password=password,
                is_staff=True,
                is_active=True,
            )
            user.groups.add(self.group)

            self.user = user

            self.send_email_with_credentials(password)

        super().save(*args, **kwargs)

    def send_email_with_credentials(self, password):
        send_mail(
            'Вы были добавлены в модераторы',
            f'Ваш логин: {self.username}\n'
            f'Ваш пароль: {password}',
            settings.EMAIL_HOST_USER,
            [self.email],
            fail_silently=False
        )

    def __str__(self):
        return self.username
    

@receiver(post_delete, sender=Moderator)
def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()