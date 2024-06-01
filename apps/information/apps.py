from django.apps import AppConfig


class DataMediaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.information'
    verbose_name = 'Данные'
    verbose_name_plural = 'Данные'

    def ready(self):
        import apps.information.services.signals
