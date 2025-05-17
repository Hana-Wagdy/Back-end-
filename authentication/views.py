from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if user.role == 'admin':
                return redirect('users:adminprofile')
            else:
                return redirect('users:usersprofile')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('auth:login')
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('rule', 'user')

        if password != confirm_password:
            messages.error(request, "Passwords don't match!")
            return redirect('auth:signup')
        if len(password) < 6:
            messages.error(request, "Password must be at least 6 characters")
            return redirect('auth:signup')
        try:
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                role=role
            )
            messages.success(request, 'Account created successfully! Please login.')
            return redirect('auth:login')
        except Exception as e:
            messages.error(request, f"Error creating account: {str(e)}")
            return redirect('auth:signup')
    return render(request, 'signup.html')

def verifyotp(request):
    return render(request, 'verify-otp.html')

def forgetpassword(request):
    return render(request, 'forgot-password.html')

def resetpassword(request):
    return render(request, 'reset-password.html')