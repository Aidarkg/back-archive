from django.contrib.auth.models import User, Group
from django.contrib import admin
from .models import Moderator, CustomGroup


class ModeratorAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'group', 'created_at', 'updated_at']
    list_display_links = ['username', 'email', 'group']
    search_fields = ['username']
    list_filter = ['created_at', 'updated_at']

    fields = ['username', 'email', 'password', 'group']
    readonly_fields = ['password']


class CustomGroupAdmin(admin.ModelAdmin):
    search_fields = ['name']
    filter_horizontal = ['permissions']


admin.site.register(Moderator, ModeratorAdmin)
admin.site.register(CustomGroup, CustomGroupAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
