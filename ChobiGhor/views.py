from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request,'home.html')

def showContact(request):
    return HttpResponse("Hello")
