from celery import shared_task, chain
from apps.information.services.video_data import cover_video
from apps.information.models.video_data import VideoLink
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


@shared_task
def save_cover(path, instance_id):
    VideoLink.objects.filter(id=instance_id).update(cover=path)


@receiver(pre_save, sender=VideoLink)
def video_download(sender, instance, **kwargs):
    try:
        link = instance.video_link
        result = chain(
            cover_video.s(link),
            save_cover.s(instance.id),
        )
        result.delay()
    except Exception as e:
        pass
