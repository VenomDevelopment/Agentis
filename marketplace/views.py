from django.shortcuts import render
from authentication.models import *
from .models import *


def index(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            affiliate_profile = AffiliateProfile.objects.get(user=user)
            print(affiliate_profile.affiliate_code)
        except AffiliateProfile.DoesNotExist:
            print("User does not have an affiliate profile.")
    return render(request, 'index.html')

def affiliate(request):
    return render(request, 'affiliate.html')

def agents(request):
    return render(request, 'agents.html')

def agent_details(request):
    return render(request, 'agent_details.html')

def cart(request):
    return render(request, 'cart.html')

def conforms(request):
    return render(request, 'conforms.html')

def custom_agent(request):
    return render(request, 'custom_agent.html')

def pricing(request):
    agents = Agent.objects.all()
    return render(request, 'pricing.html', {'agents': agents})
