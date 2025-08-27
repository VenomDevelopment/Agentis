from django.shortcuts import redirect, render
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from .models import AffiliateProfile, AffiliateCommission
from django.db import transaction
import uuid

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@transaction.atomic
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')
        affiliate_code = request.POST.get('affiliate_code', '').strip()
        if not username or not email or not password:
            return render(request, 'signup.html', {'error': 'All fields are required.'})
        if password != confirm_password:
            return render(request, 'signup.html', {'error': 'Passwords do not match.'})
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already taken.'})
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email already registered.'})
        user = User.objects.create_user(username=username, email=email, password=password)
        referred_by = None
        if affiliate_code:
            try:
                referred_by = AffiliateProfile.objects.get(affiliate_code=affiliate_code).user
                AffiliateCommission.objects.create(affiliate=referred_by.affiliate_profile, referred_user=user)
            except AffiliateProfile.DoesNotExist:
                referred_by = None
        while True:
            affiliate_code = str(uuid.uuid4())[:8].upper()
            if not AffiliateProfile.objects.filter(affiliate_code=affiliate_code).exists():
                break
        AffiliateProfile.objects.create(user=user, affiliate_code=affiliate_code, referred_by=referred_by)
        return redirect('login')
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return redirect('login')