from django.shortcuts import render


# Create your views here.

def addbooks(request):
    return render(request, 'AddBooks.html')


def editbooks(request):
    return render(request, 'EditBooks.html')


def managebooks(request):
    return render(request, 'ManageBooks.html')
