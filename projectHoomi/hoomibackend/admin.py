from django.contrib import admin
from .models import User, Property, Booking, Payment, Review

admin.site.register(User)   
admin.site.register(Property)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Review)
