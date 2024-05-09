from rest_framework import generics
from data_media.models.kodeks import KODEKS
from data_media.serializers.kodeks import KODEKSSerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q


class KODEKSListCreateAPIView(generics.ListAPIView):
    queryset = KODEKS.objects.all().order_by('-created_at')
    serializer_class = KODEKSSerializer
    pagination_class = PageNumberPagination


class KODEKSRetrieveUpdateDestroyAPIView(generics.RetrieveAPIView):
    queryset = KODEKS.objects.all()
    serializer_class = KODEKSSerializer
