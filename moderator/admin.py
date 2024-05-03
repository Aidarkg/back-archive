from django.contrib import admin
from .models import Moderator


class ModeratorAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'group', 'created_at', 'updated_at']
    list_display_links = ['id', 'username']
    search_fields = ['username']
    list_filter = ['created_at', 'updated_at']

    fields = ['id', 'username', 'email', 'group', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']


admin.site.register(Moderator, ModeratorAdmin)
