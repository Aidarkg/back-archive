import os
from django.core.validators import URLValidator, ValidationError


def validate_link(link):
    url_validator = URLValidator()
    try:
        url_validator(link)
    except ValidationError:
        raise ValidationError('Введите корректную ссылку!')


def validate_video_format(file):
    valid_extensions = [
        'mp4', 'webm', 'avi', 'mkv', 'flv', 'm4v', 'mov', 'wmv', 'mpeg', 'mpg',
        '3gp', '3g2', 'ogv', 'vob', 'asf', 'rm', 'rmvb', 'ts', 'mts', 'divx', 'xvid'
    ]
    file_extension = os.path.splitext(file.name)[1][1:].lower()
    if file_extension not in valid_extensions:
        raise ValidationError('Загрузите видео!')


def validate_pdf_format(file):
    valid_extensions = ['pdf']
    file_extension = os.path.splitext(file.name)[1][1:].lower()
    if file_extension not in valid_extensions:
        raise ValidationError('Загрузите документ в формате PDF!')
