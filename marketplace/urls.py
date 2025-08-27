from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('agents/', agents, name='agents'),
    path('affiliate/', affiliate, name='affiliate'),
    path('agent_details/', agent_details, name='agent_details'),
    path('cart/', cart, name='cart'),
    path('conforms/', conforms, name='conforms'),
    path('custom_agent/', custom_agent, name='custom_agent'),
    path('pricing/', pricing, name='pricing'),
]
