from django.shortcuts import render


def userprofile(request):
    return render(request, 'usersprofile.html')

def adminprofile(request):
    return render(request, 'AdminPage.html')