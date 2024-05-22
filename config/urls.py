from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.faq.views.question_answer import question_create_view
from config.yasg import urlpatterns as yasg


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/question/create/', question_create_view, name='question-create'),
]

urlpatterns += i18n_patterns(
    path('', include('apps.data_media.urls')),
    path('', include('apps.faq.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += yasg