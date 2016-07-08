from django.contrib import admin
from .models import UserBooking,BookingSlots
# Register your models here.
admin.site.register(UserBooking)
admin.site.register(BookingSlots)
