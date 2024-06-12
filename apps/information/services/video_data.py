from django.core.validators import URLValidator


def validate_link(link):
    url_validator = URLValidator()
    url_validator(link)
    return link
