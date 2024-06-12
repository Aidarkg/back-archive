import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
django.setup()
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.contenttypes.models import ContentType
from django.db import transaction, IntegrityError


class Command(BaseCommand):
    help = 'Force load fixture and handle duplicate content type entries'

    def handle(self, *args, **kwargs):
        try:
            with transaction.atomic():
                # Удаляем конфликтующие записи
                conflicting_entries = ContentType.objects.filter(app_label='information', model='kodeks')
                if conflicting_entries.exists():
                    self.stdout.write(self.style.WARNING('Conflicting entries found, deleting them...'))
                    conflicting_entries.delete()

                # Загружаем данные из фикстуры
                self.stdout.write(self.style.NOTICE('Loading fixture...'))
                call_command('loaddata', 'data.json')
                self.stdout.write(self.style.SUCCESS('Successfully loaded fixture'))
        except IntegrityError as e:
            self.stdout.write(self.style.ERROR(f'Error loading fixture: {e}'))
