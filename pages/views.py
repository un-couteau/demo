# from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from coffee.models import Order
#
# # Create your views here.
#
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')
#
# @login_required(login_url='login')
# def order_id(request, id):
#     try:
#         order = Order.objects.get(id=id)
#         return render(request, 'order/order_id.html', context={'order': order})
#     except Order.DoesNotExist:
#         pass
# @login_required(login_url='login')
# def order_request(request):
#     orders = Order.objects.all()
#     return render(request, 'order/order_request.html', context={'orders': orders})
#
# @login_required(login_url='login')
# def order_create(request):
#     pass

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from coffee.models import Order
from .forms import OrderForm, OrderStatusForm

def is_waiter(user):
    return user.groups.filter(name='Официант').exists()

def is_cooker(user):
    return user.groups.filter(name='Повар').exists()

def is_admin(user):
    return user.groups.filter(name='Администратор').exists()

# @login_required
# @user_passes_test(is_waiter)
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

# @login_required
# @user_passes_test(is_cooker)
def view_orders(request):
    orders = Order.objects.all()
    # orders = Order.objects.filter(status='accepted')
    return render(request, 'order/order_request.html', {'orders': orders})

# @login_required
# @user_passes_test(is_cooker)
def update_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('view_orders')
    else:
        form = OrderStatusForm(instance=order)
    return render(request, 'order/order_update.html', {'form': form, 'order': order})
