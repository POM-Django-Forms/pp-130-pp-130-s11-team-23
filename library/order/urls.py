from django.urls import path
from .views import (
    order_list_view,
    my_orders_view,
    create_order_view,
    close_order_view,
)

urlpatterns = [
    path('', order_list_view, name='order_list'),                    
    path('my/', my_orders_view, name='my_orders'),                   
    path('create/', create_order_view, name='create_order'),         
    path('close/<int:order_id>/', close_order_view, name='close_order'), 
]