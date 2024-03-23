from django.contrib import admin
from .models import Passenger,Flight,Booking

# Register your models here.
admin.site.register(Passenger)
admin.site.register(Flight)
admin.site.register(Booking)