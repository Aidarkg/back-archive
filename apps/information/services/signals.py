import os.path

from celery import shared_task
from django.conf import settings

from apps.information.services.video_data import cover_video
from apps.information.services.services_price import PriceListService
from apps.information.models import VideoLink, Service, PriceList
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


@shared_task
def save_cover(link):
    path = cover_video(link)
    VideoLink.objects.filter(video_link=link).update(cover=path)


@receiver(post_save, sender=VideoLink)
def video_download(sender, instance, **kwargs):
    try:
        link = instance.video_link
        save_cover.delay(link)
    except Exception as e:
        pass


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
def price_list(sender, instance, **kwargs):
    try:
        save_file.delay()
    except Exception as e:
        pass
