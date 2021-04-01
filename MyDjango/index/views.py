from django.shortcuts import render


# Create your views here.

def index(request):
    value = 'This is a test!'
    print(value)
    return render(request, 'index.html')
