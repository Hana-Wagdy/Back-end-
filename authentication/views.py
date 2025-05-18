from django.contrib.auth import authenticate, login as auth_login
from django.core.mail import send_mail  
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser
import random
#commented out for now
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
        role = request.POST.get('rule', 'user')  # Matches 'rule' from signup.html

        # Validation
        if password != confirm_password:
            messages.error(request, "Passwords don't match!")
            return redirect('auth:signup')
        
        if len(password) < 6:
            messages.error(request, "Password must be at least 6 characters")
            return redirect('auth:signup')

        try:
            # Create user
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
    if request.method == 'POST':
        otp_input = request.POST.get('otp')
        session_otp = request.session.get('reset_otp')
        if otp_input == session_otp:
            return redirect('auth:resetpassword')
        else:
            messages.error(request, "Invalid OTP.")
            return redirect('auth:verify-otp')
    return render(request, 'verify-otp.html')











def forgetpassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        users = CustomUser.objects.filter(email=email)
        if not users.exists():
            messages.error(request, "No user with that email.")
            return redirect('auth:forgetpassword')
        elif users.count() > 1:
            messages.error(request, "Multiple accounts found with this email. Please contact support.")
            return redirect('auth:forgetpassword')
        user = users.first()

        otp = random.randint(100000, 999999)
        request.session['reset_email'] = email
        request.session['reset_otp'] = str(otp)

        # For real use, send email:
        # send_mail('Your OTP', f'Your OTP is {otp}', 'from@example.com', [email])

        # For testing, show OTP as a message:
        messages.info(request, f"OTP for {email}: {otp}")

        return redirect('auth:verify-otp')
    return render(request, 'forgot-password.html')


#hi
#heloooooooooooooooooo

def resetpassword(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.session.get('reset_email')
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('auth:resetpassword')
        users = CustomUser.objects.filter(email=email)
        if not users.exists():
            messages.error(request, "User not found.")
            return redirect('auth:resetpassword')
        elif users.count() > 1:
            messages.error(request, "Multiple accounts found with this email. Please contact support.")
            return redirect('auth:resetpassword')
        user = users.first()
        user.set_password(password)
        user.save()
        messages.success(request, "Password reset successful. Please login.")
        request.session.pop('reset_email', None)
        request.session.pop('reset_otp', None)
        return redirect('auth:login')
    return render(request, 'reset-password.html')