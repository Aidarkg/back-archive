from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

from apps.data_media.serializers import PhotoGallerySerializer
from apps.data_media.models import PhotoGallery
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class PhotoGalleryListAPIView(ListAPIView):
    queryset = PhotoGallery.objects.all().order_by('-created_at')
    serializer_class = PhotoGallerySerializer
    pagination_class = PageNumberPagination

    @method_decorator(cache_page(60 * 2))
    def retrieve(self, request, *args, **kwargs):
        return super(PhotoGalleryListAPIView, self).list(request, *args, **kwargs)


class PhotoGalleryDetailAPIView(RetrieveAPIView):
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoGallerySerializer

    @method_decorator(cache_page(60 * 5))
    def retrieve(self, request, *args, **kwargs):
        return super(PhotoGalleryDetailAPIView, self).retrieve(request, *args, **kwargs)
