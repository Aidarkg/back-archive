from django.urls import path
from data_media.views import VideoDataAPIView, VideoDataRetriveAPIView


urlpatterns = [
    path('api/v1/video/', VideoDataAPIView.as_view()),
    path('api/v1/video/<int:id>', VideoDataRetriveAPIView.as_view()),
]
