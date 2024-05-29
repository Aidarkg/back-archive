from rest_framework import generics
from apps.information.models.kodeks import KODEKS
from apps.information.serializers.kodeks import KODEKSSerializer
from rest_framework.pagination import PageNumberPagination


class KODEKSListCreateAPIView(generics.ListAPIView):
    queryset = KODEKS.objects.all()
    serializer_class = KODEKSSerializer
    pagination_class = PageNumberPagination


class KODEKSRetrieveUpdateDestroyAPIView(generics.RetrieveAPIView):
    queryset = KODEKS.objects.all()
    serializer_class = KODEKSSerializer
