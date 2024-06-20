from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Order(models.Model):
    STATUS_CHOICES = [
        ('accepted', 'Принят'),
        ('preparing', 'Готовится'),
        ('ready', 'Готов'),
        ('paid', 'Оплачен'),
    ]

    waiter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='waiter_orders')
    cooker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cooker_orders', null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='accepted')
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.status}"

