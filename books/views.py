from django.shortcuts import render

# Create your views here.
def freebooks(request):
    # books = Book.objects.all()
    return render(request, 'freeBooks.html')

def bookdetails(request):
    return render(request, 'bookdetailed.html')
