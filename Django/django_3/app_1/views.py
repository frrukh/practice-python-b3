from django.shortcuts import render ,redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('home page')

# making the C of crud i.e create.
def signup(request):
    return render(request,'signup.html')