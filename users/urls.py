from django.urls import path
from . import views
 #yaaa rabbbb 
app_name = 'users'
urlpatterns =[
    path('usersprofile',views.userprofile,name='usersprofile'),
    path('adminprofile',views.adminprofile,name='adminprofile'),

    
] 