from django.apps import AppConfig


class FaqConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.faq'
    verbose_name = 'Вопросы-Ответы'
    verbose_name_plural = 'Вопросы-Ответы'

    def ready(self):
        import apps.faq.services.signals
