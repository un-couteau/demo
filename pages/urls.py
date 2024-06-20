from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
urlpatterns = [
    # главные страинцы
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', index, name='index'),


    # список заказов
    path('orders/', view_orders, name='view_orders'),
    path('order/<int:order_id>/', view_order_id, name='view_order_id'),
    path('order_create/', create_order, name='create_order'),

    # ошибки
    path('error', TemplateView.as_view(template_name='error/error.html'), name='error'),
    path('no_shift', TemplateView.as_view(template_name='error/no_shift.html'), name='no_shift'),
    path('no_my_shift', TemplateView.as_view(template_name='error/not_your_shift.html'), name='not_your_shift'),

]
