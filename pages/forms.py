from django import forms
from coffee.models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['details']

class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']
