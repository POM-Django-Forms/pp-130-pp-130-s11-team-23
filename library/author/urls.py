from django.urls import path
from .views import author_list_view, add_author_view, delete_author_view

urlpatterns = [
    path('', author_list_view, name='author_list'),
    path('add/', add_author_view, name='add_author'),
    path('delete/<int:author_id>/', delete_author_view, name='delete_author'),
]