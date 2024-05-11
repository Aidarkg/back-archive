from django.urls import path

from apps.data_media.views import VideoDataAPIView, VideoDataRetrieveAPIView, \
    NewsListAPIView, NewsDetailAPIView, \
    PhotoGalleryListAPIView, PhotoGalleryDetailAPIView, \
    ServiceListView, \
    KODEKSListCreateAPIView, KODEKSRetrieveUpdateDestroyAPIView, \
    SearchAPIView, ContactListAPIView, ContactDetailAPIView, \
    VisitorsAPIView, \
    ManagementListAPIView, ManagementDetailAPIView

urlpatterns = [
    path('api/v1/video/', VideoDataAPIView.as_view()),
    path('api/v1/video/<int:pk>', VideoDataRetrieveAPIView.as_view()),
    path('api/v1/management/', ManagementListAPIView.as_view()),
    path('api/v1/management/<int:pk>/', ManagementDetailAPIView.as_view()),
    path('api/v1/news/', NewsListAPIView.as_view()),
    path('api/v1/news/<int:pk>/', NewsDetailAPIView.as_view()),
    path('api/v1/photos/', PhotoGalleryListAPIView.as_view()),
    path('api/v1/photos/<int:pk>/', PhotoGalleryDetailAPIView.as_view()),
    path('api/v1/service/', ServiceListView.as_view()),
    path('api/v1/kodeks/', KODEKSListCreateAPIView.as_view()),
    path('api/v1/kodeks/<int:pk>/', KODEKSRetrieveUpdateDestroyAPIView.as_view()),
    path('api/v1/contacts', ContactListAPIView.as_view()),
    path('api/v1/contacts/<int:pk>', ContactDetailAPIView.as_view()),
    path('api/v1/search/', SearchAPIView.as_view(), name='search'),
    path('api/v1/visitors/', VisitorsAPIView.as_view()),

]
