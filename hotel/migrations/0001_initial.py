# Generated by Django 5.0.6 on 2024-06-20 09:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateField()),
                ('order_status', models.CharField(choices=[('готовится', 'Готовится'), ('готов', 'Готов')], max_length=255)),
                ('room_number', models.CharField(max_length=255)),
                ('amount_clients', models.IntegerField()),
                ('hotel_services', models.CharField(max_length=255)),
                ('payment_status', models.CharField(choices=[('принят', 'Принят'), ('оплачен', 'Оплачен')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderUserList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.shift')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
