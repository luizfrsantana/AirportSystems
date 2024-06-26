# Generated by Django 5.0.3 on 2024-03-22 03:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flightID', models.AutoField(primary_key=True, serialize=False)),
                ('flightNumber', models.CharField(max_length=20)),
                ('departureAirport', models.CharField(max_length=3)),
                ('arrivalAirport', models.CharField(max_length=3)),
                ('departureTime', models.DateTimeField()),
                ('arrivalTime', models.DateTimeField()),
                ('capacity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('passengerID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('bookingID', models.AutoField(primary_key=True, serialize=False)),
                ('bookingDate', models.DateTimeField(auto_now_add=True)),
                ('seatNumber', models.CharField(max_length=10)),
                ('status', models.CharField(choices=[('confirmed', 'Confirmed'), ('pending', 'Pending'), ('canceled', 'Canceled')], max_length=20)),
                ('flightID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FlightBookingApp.flight')),
                ('passengerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FlightBookingApp.passenger')),
            ],
        ),
    ]
