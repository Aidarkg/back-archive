from django.urls import path
from data_media.views.video_data import VideoDataAPIView, VideoDataRetriveAPIView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('api/v1/video/', VideoDataAPIView.as_view()),
    path('api/v1/video/<int:id>', VideoDataRetriveAPIView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)