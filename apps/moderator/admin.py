from django.contrib import admin
from .models import Moderator


class ModeratorAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'group', 'created_at', 'updated_at']
    list_display_links = ['username', 'email', 'group']
    search_fields = ['username']
    list_filter = ['created_at', 'updated_at']

    fields = ['username', 'email', 'password', 'group', 'is_active']
    readonly_fields = ['password']


admin.site.register(Moderator, ModeratorAdmin)
