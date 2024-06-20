from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Order(models.Model):
    order_status_choices = [
        ('готовится', 'Готовится'),
        ('готов', 'Готов'),
    ]
    payment_status_choices = [
        ('принят', 'Принят'),
        ('оплачен', 'Оплачен'),
    ]

    date_creation = models.DateField()
    order_status = models.CharField(max_length=255, choices=order_status_choices)
    room_number = models.CharField(max_length=255)
    amount_clients = models.IntegerField()
    hotel_services = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=255, choices=payment_status_choices)

    def __str__(self):
        return f"Order {self.id} - {self.order_status}"


class OrderUserList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class Shift(models.Model):
    date_start = models.DateField()
    date_end = models.DateField()


class UserList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
