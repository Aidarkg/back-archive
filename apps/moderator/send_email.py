from django.core.mail import send_mail
from django.conf import settings


def send_email_with_credentials(self, password):
        send_mail(
            'Вы были добавлены в модераторы',
            f'Ваш логин: {self.username}\n'
            f'Ваш пароль: {password}',
            settings.EMAIL_HOST_USER,
            [self.email],
            fail_silently=False
        )