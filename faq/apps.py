from django.apps import AppConfig


class FaqConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'faq'
    verbose_name = 'Вопросы-Ответы'
    verbose_name_plural = 'Вопросы-Ответы'
