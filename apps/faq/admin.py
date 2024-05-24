from django.contrib import admin
from .models import Faq, Question, Answer
from apps.common.admin.mixins import BaseAdminMixin
from .forms import AnswerForm


@admin.register(Faq)
class FaqAdmin(BaseAdminMixin):
    list_display = ('id', 'question', 'answer', 'created_at', 'updated_at')
    list_display_links = ('id', 'question')
    search_fields = ('question',)
    fields = ('question', 'answer',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    form = AnswerForm
    list_display = ('id', 'question', 'created_at', 'updated_at')
    search_fields = ('question', 'moderator',)
    fields = ('moderator', 'question', 'answer')
    raw_id_fields = ('moderator', 'question')


admin.site.register(Question)
