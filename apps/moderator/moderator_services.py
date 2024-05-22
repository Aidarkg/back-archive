import string
import random
from .tasks import send_email_with_credentials
from django.contrib.auth.models import User


def generate_password(length=20):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password


def save_moderator(instance, *args, **kwargs):
    if instance.user_id:
        user = instance.user
        user.username = instance.username
        user.email = instance.email
        user.save()

        user.groups.clear()
        user.groups.add(instance.group)

    else:
        password = generate_password()
        user = User.objects.create_user(
            username=instance.username,
            email=instance.email,
            password=password,
            is_staff=True,
            is_active=True,
        )
        user.groups.add(instance.group)

        instance.user = user
        send_email_with_credentials.delay(user.id, password)
