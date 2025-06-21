from django.contrib import admin
from order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'created_at', 'plated_end_at', 'end_at')
    list_filter = ('book', 'user', 'created_at', 'end_at')
    search_fields = ('book__name', 'user__email')

    fieldsets = (
        ('Постійні дані', {
            'fields': ('user', 'book')
        }),
        ('Динамічні дані', {
            'fields': ('created_at', 'plated_end_at', 'end_at')
        }),
    )
    readonly_fields = ('created_at',)
