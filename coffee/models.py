from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Order(models.Model):
    waiter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='waiter_orders')
    cooker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cooker_orders')

    status = models.BooleanField(default=False)

