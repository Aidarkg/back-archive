from celery import shared_task
from apps.information.services.video_data import cover_video
from apps.information.models.video_data import VideoLink
from django.db.models.signals import post_save
from django.dispatch import receiver


@shared_task
def save_cover(link):
    cover = cover_video(link)
    VideoLink.objects.filter(video_link=link).update(cover=cover)


@receiver(post_save, sender=VideoLink)
def video_link(sender, instance, **kwargs):
    link = instance.video_link
    save_cover(link)
