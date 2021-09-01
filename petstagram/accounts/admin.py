from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from petstagram.accounts.models import PetstagramUser


@admin.register(PetstagramUser)
class PetstagramUserAdmin(UserAdmin):
    list_display = ('email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
