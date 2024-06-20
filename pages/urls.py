from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', index, name='index'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(next_page="/login"), name='logout'),


    path('create_order/', create_order, name='create_order'),
    path('orders/', view_orders, name='view_orders'),
    path('orders/<int:order_id>/update/', update_order_status, name='update_order_status'),
]

