from apps.information.services.video_data import cover_video
from apps.information.models.video_data import VideoLink
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


# @shared_task
# def save_cover(link):
#     path = cover_video(link)
#     VideoLink.objects.filter(video_link=link).update(cover=path)


@receiver(post_save, sender=VideoLink)
def video_download(sender, instance, **kwargs):
    try:
        link = instance.video_link
        path = cover_video(link)
        VideoLink.objects.filter(video_link=link).update(cover=path)
    except Exception as e:
        pass
