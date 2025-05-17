from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path('login.html' , views.login , name='login'),
    path('signup' , views.signup , name='signup'),
    path('verifyotp' , views.verifyotp , name='verify-otp'),
    path('forgetpassword' , views.forgetpassword , name='forgetpassword'),
    path('resetpassword' , views.resetpassword , name='resetpassword'),
]

