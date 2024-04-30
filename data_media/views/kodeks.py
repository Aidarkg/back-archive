from rest_framework import generics
from data_media.models.kodeks import KODEKS
from data_media.serializers.kodeks import KODEKSSerializer

class KODEKSListCreateAPIView(generics.ListCreateAPIView):
    queryset = KODEKS.objects.all()
    serializer_class = KODEKSSerializer



class KODEKSRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KODEKS.objects.all()
    serializer_class = KODEKSSerializer
