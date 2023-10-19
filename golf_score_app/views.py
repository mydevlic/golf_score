#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("Hello, Azure Django App!")
    return render(request, 'page/index.html')

def capture(request):
    return render(request, 'page/capture_photo.html')
