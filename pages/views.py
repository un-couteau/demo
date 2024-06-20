from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect

from hotel.forms import OrderForm, OrderStatusForm, OrderFormCreate
from hotel.models import Order


# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')


def is_room_service(user):
    return user.groups.filter(name='Сотрудник обслуживания номеров').exists()


def is_hotel_service(user):
    return user.groups.filter(name='Сотрудник предоставления услуг отеля').exists()

def is_room_or_hotel_service(user):
    return is_room_service(user) or is_hotel_service(user)

@user_passes_test(is_room_or_hotel_service)
def view_orders(request):
    if request.user.groups.filter(name="Сотрудник предоставления услуг отеля"):
        orders = Order.objects.all()
        return render(request, 'order/view_orders.html', {'orders': orders})
    if request.user.groups.filter(name='Сотрудник обслуживания номеров'):
        orders = Order.objects.filter(payment_status='')
        return render(request, 'order/view_orders.html', {'orders': orders})
    return render(request, 'error.html')

@user_passes_test(is_room_or_hotel_service)
def view_order_id(request, order_id):
    if request.user.groups.filter(name="Сотрудник предоставления услуг отеля"):
        order = Order.objects.get(id=order_id)
        return render(request, 'order/views_orders_for_hotel.html', {'order': order})
    if request.user.groups.filter(name='Сотрудник обслуживания номеров'):

        order = Order.objects.get(id=order_id)
        return render(request, 'order/views_orders_for_hotel.html', {'order': order})
    return render(request, 'error.html')

@user_passes_test(is_room_service)
def create_order(request):
    if request.method == 'POST':
        form = OrderFormCreate(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.waiter = request.user  # Если нужно связать заказ с текущим пользователем
            order.save()
            return redirect('view_orders')
    else:
        form = OrderFormCreate()
    return render(request, 'order/create_order.html', {'form': form})