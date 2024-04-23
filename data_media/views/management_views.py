from rest_framework.response import Response
from rest_framework.views import APIView

from data_media.models.management import Management
from ..serializers.management_serializers import ManagementSerializers
from rest_framework import status


class ManagementListAPIView(APIView):
    def get(self, request):
        management = Management.objects.all()
        serializer_data = ManagementSerializers(management, many=True).data
        return Response(serializer_data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer_data = ManagementSerializers(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data, status=status.HTTP_201_CREATED)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)


class ManagementDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Management.objects.get(pk=pk)
        except Management.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        management = self.get_object(pk)
        serializer = ManagementSerializers(management)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        management = self.get_object(pk)
        serializer = ManagementSerializers(data=request.data, instance=management, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        management = self.get_object(pk)
        management.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
