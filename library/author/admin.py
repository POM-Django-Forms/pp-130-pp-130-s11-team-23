from django.contrib import admin
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "surname", "name", "patronymic")
    list_filter = ("surname",)
    search_fields = ("surname", "name", "patronymic")

    fieldsets = (
        ("Статичні дані", {
            "fields": ("name", "surname", "patronymic")
        }),
    )
