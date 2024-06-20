from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),

    path('', index, name='index'),
    # path('orders/', view_orders, name='view_orders'),
    path('orders/<int:order_id>/update/', update_order_status, name='update_order_status'),
    path('create_order/', create_order, name='create_order'),
    path('orders/<int:order_id>/update_room_service/', update_order_status_room_service, name='update_order_status_room_service'),

    # список заказов
    path('orders/', view_orders_for_hotel, name='view_orders'),
    path('order/<int:order_id>/', )
]
