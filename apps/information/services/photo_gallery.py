from django.db.models import Count

from apps.information.models import PhotoGallery


class PhotoGalleryService:
    @staticmethod
    def get_all_photos():
        return PhotoGallery.objects.all().annotate(count=Count('photo'))
