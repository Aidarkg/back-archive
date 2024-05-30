from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

from apps.information.serializers import PhotoGallerySerializer, PhotoListSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from ..services.photo_gallery import PhotoGalleryService


class PhotoGalleryListAPIView(ListAPIView):
    queryset = PhotoGalleryService.get_all_photos()
    serializer_class = PhotoListSerializer
    pagination_class = PageNumberPagination

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PhotoGalleryDetailAPIView(RetrieveAPIView):
    queryset = PhotoGalleryService.get_all_photos()
    serializer_class = PhotoGallerySerializer

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
