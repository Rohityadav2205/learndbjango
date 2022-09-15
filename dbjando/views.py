from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("this is my user login page")

def user(request):
    return render(request,"user.html")