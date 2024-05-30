from rest_framework import generics
from apps.information.serializers.kodeks import KODEKSSerializer
from rest_framework.pagination import PageNumberPagination
from ..services.kodeks import KodeksService


class KODEKSListCreateAPIView(generics.ListAPIView):
    queryset = KodeksService.get_all_kodeks()
    serializer_class = KODEKSSerializer
    pagination_class = PageNumberPagination


class KODEKSRetrieveUpdateDestroyAPIView(generics.RetrieveAPIView):
    queryset = KodeksService.get_all_kodeks()
    serializer_class = KODEKSSerializer
