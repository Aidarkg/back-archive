from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

from data_media.serializers import PhotoGallerySerializer
from data_media.models import PhotoGallery


class PhotoGalleryListAPIView(ListAPIView):
    serializer_class = PhotoGallerySerializer
    pagination_class = PageNumberPagination


class PhotoGalleryDetailAPIView(RetrieveAPIView):
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoGallerySerializer
    lookup_url_kwarg = 'id'
