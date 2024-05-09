from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

from apps.data_media.serializers import PhotoGallerySerializer
from apps.data_media.models import PhotoGallery


class PhotoGalleryListAPIView(ListAPIView):
    queryset = PhotoGallery.objects.all().order_by('-created_at')
    serializer_class = PhotoGallerySerializer
    pagination_class = PageNumberPagination


class PhotoGalleryDetailAPIView(RetrieveAPIView):
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoGallerySerializer
