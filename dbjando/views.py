from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("this is my query set program")

def user(request):
    return render(request,"user.html")