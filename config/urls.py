from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.faq.views.question_answer import question_create_view
from config.yasg import urlpatterns as yasg


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/question/create/', question_create_view, name='question-create'),
    path('api/v1/', include('apps.information.urls')),
    path('api/v1/', include('apps.faq.urls')),
    path('api/v1/', include('apps.contacts.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += yasg

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
