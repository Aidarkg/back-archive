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

    def get_queryset(self):
        queryset = PhotoGallery.objects.all().order_by('-created_at')

        search_query = self.request.query_params.get('search', None)

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query)
            )
        return queryset



class PhotoGalleryDetailAPIView(RetrieveAPIView):
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoGallerySerializer
    lookup_url_kwarg = 'id'