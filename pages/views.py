from datetime import date
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect

from hotel.forms import OrderForm, OrderStatusOrderForm, OrderStatusPaymentForm, OrderFormCreate
from hotel.models import Order, UserList, Shift, OrderUserList


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
    if request.user.groups.filter(name="Сотрудник предоставления услуг отеля").exists():
        orders = Order.objects.all()
    elif request.user.groups.filter(name='Сотрудник обслуживания номеров').exists():
        active_shift = Shift.objects.filter(userlist__user=request.user).order_by('-date_start').first()

        if active_shift:
            user_orders = OrderUserList.objects.filter(user=request.user).values_list('order', flat=True)
            orders = Order.objects.filter(
                id__in=user_orders,
                date_creation__range=[active_shift.date_start, active_shift.date_end]
            )
        else:
            orders = Order.objects.none()
    else:
        return render(request, 'error/error.html')

    return render(request, 'order/view_orders.html', {'orders': orders})

@user_passes_test(is_room_or_hotel_service)
def view_order_id(request, order_id):
    # if request.user.groups.filter(name="Сотрудник предоставления услуг отеля"):
    #     order = Order.objects.get(id=order_id)
    #     return render(request, 'order/views_orders_for_hotel.html', {'order': order})



    if request.user.groups.filter(name="Сотрудник предоставления услуг отеля").exists():
        order = get_object_or_404(Order, id=order_id)
        if request.method == 'POST':
            form = OrderStatusPaymentForm(request.POST, instance=order)
            if form.is_valid():
                form.save()
                return redirect('view_orders')
        else:
            form = OrderStatusPaymentForm(instance=order)
        return render(request, 'order/order_id.html', {'form': form, 'order': order})
    if request.user.groups.filter(name='Сотрудник обслуживания номеров'):
        active_shift = Shift.objects.filter(date_start__lte=now().date(), date_end__gte=now().date()).first()
        user_in_shift = UserList.objects.filter(user=request.user, shift=active_shift).exists()

        if not active_shift or not user_in_shift:
            return render(request, 'error/not_your_shift.html')
        order = get_object_or_404(Order, id=order_id, date_creation__range=[active_shift.date_start, active_shift.date_end], payment_status='принят')

        if request.method == 'POST':
            form = OrderStatusOrderForm(request.POST, instance=order)
            if form.is_valid():
                form.save()
                return redirect('view_orders')  # Замените 'view_orders' на URL, куда вы хотите перенаправить после успешного сохранения
        else:
            form = OrderStatusOrderForm(instance=order)

        return render(request, 'order/order_id.html', {'form': form, 'order': order})
        # active_shift = Shift.objects.filter(date_start__lte=now().date(), date_end__gte=now().date()).first()
        # user_in_shift = UserList.objects.filter(user=request.user, shift=active_shift).exists()
        # if not active_shift or not user_in_shift:
        #     return render(request, 'error/not_your_shift.html')
        # if active_shift:
        #     if request.method == 'POST':
        #         order = Order.objects.filter(date_creation__range=[active_shift.date_start, active_shift.date_end], payment_status='принят')
        #         form = OrderStatusOrderForm(request.POST, instance=order)
        #         if form.is_valid():
        #             form.save()
        #             return redirect('view_orders')
        # return render(request, 'error/error.html', {'message': 'У вас нет активной смены.'})


# orders = Order.objects.filter(date_creation__range=[active_shift.date_start, active_shift.date_end], payment_status='принят')
# return render(request, 'order/order_id.html', {'orders': orders})
@user_passes_test(is_room_service)
def create_order(request):
    active_shift = Shift.objects.filter(date_start__lte=now().date(), date_end__gte=now().date()).first()
    user_in_shift = UserList.objects.filter(user=request.user, shift=active_shift).exists()

    if not active_shift or not user_in_shift:
        return render(request, 'error/no_shift.html')
    if request.method == 'POST':
        form = OrderFormCreate(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()

            if form.is_valid():
                order = form.save()
                OrderUserList.objects.create(user=request.user, order=order)

                return redirect('view_orders')

            return redirect('view_orders')
    else:
        form = OrderFormCreate()
    return render(request, 'order/create_order.html', {'form': form})