from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from coffee.models import Order

# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def order_id(request, id):
    try:
        order = Order.objects.get(id=id)
        return render(request, 'order/order_id.html', context={'order': order})
    except Order.DoesNotExist:
        pass
@login_required(login_url='login')
def order_request(request):
    orders = Order.objects.all()
    return render(request, 'order/order_request.html', context={'orders': orders})

@login_required(login_url='login')
def order_create(request):
    pass