from django import forms
from django.contrib.auth.models import User

from hotel.models import Order, Shift, UserList


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_status', 'payment_status']
        read_only_fields = ['date_creation', 'room_number', 'amount_clients', 'hotel_services',]

class OrderFormCreate(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['room_number', 'amount_clients', 'hotel_services',]

class OrderStatusPaymentForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_status',]
        read_only_fields = ['room_number', 'amount_clients', 'hotel_services', 'order_status']
class OrderStatusOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_status',]
        read_only_fields = ['room_number', 'amount_clients', 'hotel_services', 'payment_status']


class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['date_start', 'date_end']


class UserShiftForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select,
        label="Сотрудник",
        empty_label="Выберите сотрудника"
    )

    shift = forms.ModelChoiceField(
        queryset=Shift.objects.all(),
        widget=forms.Select,
        label="Смена",
        empty_label="Выберите смену"
    )

    class Meta:
        model = UserList
        fields = ['user', 'shift']

    def __init__(self, *args, **kwargs):
        super(UserShiftForm, self).__init__(*args, **kwargs)
        self.fields['user'].label_from_instance = lambda obj: f"{obj.first_name} {obj.last_name}"
        self.fields['shift'].label_from_instance = lambda obj: f"{obj.date_start} {obj.date_end}"
