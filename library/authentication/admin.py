from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'role', 'is_active', 'get_groups')
    list_filter = ('role', 'is_active', 'groups')
    search_fields = ('email', 'first_name', 'last_name')

    def get_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])
    get_groups.short_description = 'Groups'