from django.urls import path
from . import views 

app_name = 'book_management'

urlpatterns = [
    path ('addbook',views.addbooks,name='add'),
    path ('editbooks',views.editbooks,name='edit'),
    path ('managebooks',views.managebooks,name='manage'),
    
]  
