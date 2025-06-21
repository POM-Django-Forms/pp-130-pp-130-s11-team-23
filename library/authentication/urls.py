from django.urls import path
from .views import home_view, user_list_view, user_detail_view

urlpatterns = [
    path('users/', user_list_view, name='user_list'),
    path('users/<int:user_id>/', user_detail_view, name='user_detail'),
    path('', home_view, name='home'),
]