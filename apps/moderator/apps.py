from django.apps import AppConfig


class ModeratorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.moderator'
    verbose_name = 'Модераторы'
    verbose_name_plural = 'Модераторы'

    def ready(self):
        import apps.moderator.tasks
