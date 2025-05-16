from django.urls import path
from . import views
app_name = 'books'
urlpatterns = [
    path('freebooks',views.freebooks,name='freebooks'),
    path('bookdetails',views.bookdetails,name='bookdetails'),
]
