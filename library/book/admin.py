from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'count', 'get_authors')  
    list_editable = ('count',)
    list_filter = ('authors',) 
    search_fields = ('name', 'authors__name', 'authors__surname')
    ordering = ('name',)

    fieldsets = (
        ('Незмінна інформація', {
            'fields': ('name', 'authors')  
        }),
        ('Змінна інформація', {
            'fields': ('count',)
        }),
    )

    def get_authors(self, obj):
        return ", ".join([author.name for author in obj.authors.all()])
    get_authors.short_description = 'Authors'