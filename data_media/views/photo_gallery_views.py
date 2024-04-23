from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from data_media.serializers import PhotoGallerySerializer
from data_media.models import PhotoGallery


# get - Возвращает список объектов фотографии
# post - Создание фотографии
class PhotoGalleryListAPIView(APIView):
    def get(self, request):
        photos = PhotoGallery.objects.all()
        serializer = PhotoGallerySerializer(photos, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PhotoGallerySerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


# get_object - возвращает объект класса по id
# get - Получение одной вариации
# patch - Обновление одного или нескольких полей объекта фотографии
# delete - удаление объекта фотографии
class PhotoGalleryDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return PhotoGallery.objects.get(pk=pk)
        except PhotoGallery.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        photo = self.get_object(pk)
        serializer = PhotoGallerySerializer(photo, context={'request': request})
        return Response(serializer.data)

    def patch(self, request, pk):
        photo = self.get_object(pk)
        serializer = PhotoGallerySerializer(photo, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        photo = self.get_object(pk)
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
