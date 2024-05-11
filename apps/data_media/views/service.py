from ..models.service import Service
from ..serializers import service
from rest_framework.generics import ListAPIView


class ServiceListView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = service.ServiceSerializers

