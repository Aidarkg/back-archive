from django.contrib import admin
from .models import Faq, Question, Answer
from common.admin.mixins import BaseAdminMixin


@admin.register(Faq)
class FaqAdmin(BaseAdminMixin):
    list_display = ('id', 'question', 'answer', 'created_at', 'updated_at')
    list_display_links = ('id', 'question')
    search_fields = ('question', )


admin.site.register(Question)
admin.site.register(Answer)
