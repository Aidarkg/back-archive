from ..serializers import service
from rest_framework.generics import ListAPIView
from ..services.service import ServiceModelService


class ServiceListView(ListAPIView):
    queryset = ServiceModelService.get_all_services()
    serializer_class = service.ServiceSerializers
