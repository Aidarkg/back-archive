from rest_framework.generics import ListAPIView
from apps.information.serializers import service
from apps.information.models import Service


class ServiceListView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = service.ServiceSerializers
