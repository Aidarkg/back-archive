from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.faq.serializers.question_answer import QuestionSerializer


@api_view(['POST'])
def question_create_view(request):
    serializer = QuestionSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
