from django.contrib import admin
from .models import Agent, Order, Cart, Payment
# Register your models here.

admin.site.register(Agent)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Payment)
