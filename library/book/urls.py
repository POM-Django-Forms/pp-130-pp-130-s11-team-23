from django.urls import path, include
from .views import book_list_view, book_detail_view, books_by_user_view, add_book_view

urlpatterns = [
    path('', book_list_view, name='book_list'),
    path('<int:book_id>/', book_detail_view, name='book_detail'),
    path('user/<int:user_id>/', books_by_user_view, name='books_by_user'),
    path('add/', add_book_view, name='add_book'),
]