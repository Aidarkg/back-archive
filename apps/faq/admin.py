from django.contrib import admin
from .models import Faq, Question, Answer
from apps.common.admin.mixins import BaseAdminMixin
# from .forms import AnswerForm


@admin.register(Faq)
class FaqAdmin(BaseAdminMixin):
    # form = AnswerForm
    list_display = ('id', 'question', 'answer', 'created_at', 'updated_at')
    list_display_links = ('id', 'question')
    search_fields = ('question', )


admin.site.register(Question)
admin.site.register(Answer)
