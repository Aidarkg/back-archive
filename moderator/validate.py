from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validate_username(value):
    if User.objects.filter(username=value):
        raise ValidationError("Модератор с таким именем уже существует.")

def validate_email(value):
    if User.objects.filter(email=value):
        raise ValidationError("Модератор с такой электронной почтой уже существует.")
