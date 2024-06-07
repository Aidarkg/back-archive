from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from apps.information.serializers import (PhotoGallerySerializer, PhotoListSerializer,
                                          PhotoHomeListSerializer, PhotoHomeDetailSerializer)
from apps.information.models import PhotoGallery, PhotoHome
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class PhotoGalleryListAPIView(ListAPIView):
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoListSerializer

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PhotoHomeListAPIView(ListAPIView):
    queryset = PhotoHome.objects.all()
    serializer_class = PhotoHomeListSerializer

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PhotoGalleryDetailAPIView(RetrieveAPIView):
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoGallerySerializer

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PhotoHomeDetailAPIView(RetrieveAPIView):
    queryset = PhotoHome.objects.all()
    serializer_class = PhotoHomeDetailSerializer

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
