from django.contrib import admin
from apps.moderator.models import Moderator

from .models import Faq, Question
from apps.common.admin.mixins import BaseAdminMixin


class FaqAdmin(BaseAdminMixin):
    list_display = ('question', 'answer', 'created_at', 'updated_at')
    list_display_links = ('question', 'answer')
    search_fields = ('question',)
    fields = ('question', 'answer',)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'question_text', 'answer', 'moderator')
    list_display_links = ('full_name', 'question_text')
    search_fields = ('full_name',)

    fields = ('full_name', 'email', 'phone_number', 'question_text', 'answer', 'is_active')
    readonly_fields = ('full_name', 'email', 'phone_number', 'question_text')

    def save_model(self, request, obj, form, change):
        try:
            moderator = Moderator.objects.get(user=request.user)
            if obj.pk:
                obj.moderator = moderator
        except Moderator.DoesNotExist as e:
            pass

        super().save_model(request, obj, form, change)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Faq, FaqAdmin)
