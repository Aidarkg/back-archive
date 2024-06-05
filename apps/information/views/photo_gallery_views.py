from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from apps.information.serializers import (PhotoGallerySerializer, PhotoListSerializer,
                                          PhotoHomeListSerializer, PhotoHomeDetailSerializer)
from apps.information.models import PhotoGallery, PhotoHome
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from ..services.photo_gallery import PhotoGalleryService


class PhotoGalleryListAPIView(APIView):
    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        paginator = PageNumberPagination()

        photo_home = PhotoHome.objects.all()[:5]
        photos = PhotoGallery.objects.all()

        paginated_photos = paginator.paginate_queryset(photos, request)
        serializer = {
            'photo_home': PhotoHomeListSerializer(photo_home, many=True, context={'request': request}).data,
            'gallery': PhotoListSerializer(paginated_photos, many=True, context={'request': request}).data
        }
        return paginator.get_paginated_response(serializer)


class PhotoGalleryDetailAPIView(RetrieveAPIView):
    queryset = PhotoGalleryService.get_all_photos()
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
