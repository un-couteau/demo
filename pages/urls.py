from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page="/login"), name='logout'),

    path('orders', order_request, name='orders'),
    path('order/<int:id>', order_id, name='order'),
]