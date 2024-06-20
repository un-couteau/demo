from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),

    path('', index, name='index'),
    # список заказов
    path('orders/', view_orders, name='view_orders'),
    # path('order/<int:order_id>/', )
    path('order_create/', create_order, name='create_order')
]
