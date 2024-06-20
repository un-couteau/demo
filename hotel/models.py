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

    date_creation = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    order_status = models.CharField(max_length=255, choices=order_status_choices, default='готовится', verbose_name='Статус заказа')
    room_number = models.CharField(max_length=255, verbose_name='Номер комнаты')
    amount_clients = models.IntegerField(verbose_name='Количество клиентов')
    hotel_services = models.CharField(max_length=255, verbose_name='Услуги')
    payment_status = models.CharField(max_length=255, choices=payment_status_choices, default='принят', verbose_name='Статус оплаты')

    def __str__(self):
        return f"Заказ {self.id} - {self.order_status}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class OrderUserList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"Связь {self.id} | {self.user.username} - Заказ {self.order.id}"

    class Meta:
        verbose_name = 'Связанный заказ'
        verbose_name_plural = 'Связанные заказы'

class Shift(models.Model):
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return f"{self.date_start} - {self.date_end} | ID {self.id}"

    class Meta:
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'

class UserList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} | {self.shift.date_start} - {self.shift.date_end}"

    class Meta:
        verbose_name = 'Связанная смена'
        verbose_name_plural = 'Связанные смены'
