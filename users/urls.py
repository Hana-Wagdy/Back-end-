from django.urls import path
from . import views
 
app_name = 'users'
urlpatterns =[
    path('usersprofile',views.userprofile,name='usersprofile'),
    path('adminprofile',views.adminprofile,name='adminprofile'),

    
] #bye cutie -- bye bye 