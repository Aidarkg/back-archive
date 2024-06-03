import string
import random
from django.contrib.auth.models import User
from django.db import IntegrityError


def generate_password(length=15):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password


def save_moderator(instance, *args, **kwargs):
    try:
        if instance.user_id:
            user = instance.user
            user.username = instance.username
            user.set_password(instance.password)
            user.email = instance.email
            user.save()

            user.groups.clear()
            user.groups.add(instance.group)

        else:
            user = User.objects.create_user(
                username=instance.username,
                email=instance.email,
                password=instance.password,
                is_staff=True,
                is_active=True,
            )
            user.groups.add(instance.group)
            instance.user = user
            instance.save()
    except IntegrityError:
        raise IntegrityError
