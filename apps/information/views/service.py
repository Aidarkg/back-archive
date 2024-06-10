from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.information.serializers import service
from apps.information.models import Service, PriceList


class ServiceListView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = service.ServiceSerializers


class PriceListAPIView(APIView):
    def get(self, request):
        price_list = PriceList.objects.all()
        serializer = service.PriceSerializers(price_list, many=True, context={'request': request}).data
        return Response(serializer, status=status.HTTP_200_OK)
