from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from apps.information.serializers.kodeks import KODEKSSerializer
from apps.information.models import KODEKS


class KODEKSListCreateAPIView(generics.ListAPIView):
    queryset = KODEKS.objects.all()
    serializer_class = KODEKSSerializer
    pagination_class = PageNumberPagination


class KODEKSRetrieveUpdateDestroyAPIView(generics.RetrieveAPIView):
    queryset = KODEKS.objects.all()
    serializer_class = KODEKSSerializer
