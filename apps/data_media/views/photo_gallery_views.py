from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

from apps.data_media.serializers import PhotoGallerySerializer, PhotoListSerializer
from apps.data_media.models import PhotoGallery
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class PhotoGalleryListAPIView(ListAPIView):
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoListSerializer
    pagination_class = PageNumberPagination

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PhotoGalleryDetailAPIView(RetrieveAPIView):
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoGallerySerializer

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
