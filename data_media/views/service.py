from ..models.service import Service
from ..serializers import service
from rest_framework.generics import ListAPIView, RetrieveAPIView


class ServiceListView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = service.ServiceSerializers


class ServiceDetailView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = service.ServiceSerializers
    lookup_field = 'id'