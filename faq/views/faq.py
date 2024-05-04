from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from faq.models import Faq
from faq.serializers.faq_serializer import FaqSerializer


class FaqAPIView(APIView):
    def get(self, request):
        faqs = Faq.objects.all()
        serializer = FaqSerializer(faqs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer_data = FaqSerializer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data, status=status.HTTP_201_CREATED)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)


class FaqAPIDetailPIView(APIView):
    def get_object(self, pk):
        try:
            return Faq.objects.get(pk=pk)
        except Faq.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        faq = self.get_object(pk)
        serializer = FaqSerializer(faq)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        faq = self.get_object(pk)
        serializer = FaqSerializer(data=request.data, instance=faq, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        faq = self.get_object(pk)
        faq.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
