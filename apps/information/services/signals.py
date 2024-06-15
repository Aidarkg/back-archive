from celery import shared_task
from apps.information.services.services_price import PriceListService
from apps.information.models import Service, PriceList
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@shared_task
def save_file():
    price_ru = PriceListService('ru')
    price_en = PriceListService('en')
    price_ky = PriceListService('ky')
    path_ru = f'prices/{price_ru.file_name}'
    path_en = f'prices/{price_en.file_name}'
    path_ky = f'prices/{price_ky.file_name}'
    PriceList.objects.update_or_create(
        file=path_ru,
        file_ru=path_ru, file_en=path_en, file_ky=path_ky
    )


@receiver(post_save, sender=Service)
def price_list_save(sender, instance, **kwargs):
    try:
        save_file()
    except Exception as e:
        pass


@receiver(post_delete, sender=Service)
def price_list_delete(sender, instance, **kwargs):
    try:
        save_file()
    except Exception as e:
        pass
