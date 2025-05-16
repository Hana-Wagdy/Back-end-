from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # Add validation as needed
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Account created! Please log in.')
        return redirect('auth:login')
    return render(request, 'signup.html')

def verifyotp(request):
    return render(request, 'verify-otp.html')

def forgetpassword(request):
    return render(request, 'forgot-password.html')

def resetpassword(request):
    return render(request, 'reset-password.html')