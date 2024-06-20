from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect

from hotel.forms import OrderForm, OrderStatusForm
from hotel.models import Order


# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')


def is_manager(user):
    return user.groups.filter(name='Менеджер').exists()


def is_room_service(user):
    return user.groups.filter(name='Сотрудник обслуживания номеров').exists()


def is_hotel_service(user):
    return user.groups.filter(name='Сотрудник предоставления услуг отеля').exists()


@login_required
@user_passes_test(is_hotel_service)
# def view_orders(request):
#     orders = Order.objects.filter(status='accepted')
#     return render(request, 'order/view_orders.html', {'orders': orders})
# @login_requiredsad
@user_passes_test(is_hotel_service)
def view_orders_for_hotel(request):
    # if request.user.groups.filter(name="Сотрудник предоставления услуг отеля"):
    orders = Order.objects.filter(payment_status='принят')
    return render(request, 'order/views_orders_for_hotel.html', {'orders': orders})


@login_required
@user_passes_test(is_hotel_service)
def update_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('view_orders')
    else:
        form = OrderStatusForm(instance=order)
    return render(request, 'order/update_order_status.html', {'form': form, 'order': order})


@login_required
@user_passes_test(is_room_service)
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.waiter = request.user
            order.save()
            return redirect('view_orders')
    else:
        form = OrderForm()
    return render(request, 'order/create_order.html', {'form': form})


@login_required
@user_passes_test(is_room_service)
def update_order_status_room_service(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('view_orders')
    else:
        form = OrderStatusForm(instance=order)
    return render(request, 'order/update_order_status.html', {'form': form, 'order': order})
