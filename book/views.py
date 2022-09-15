from django.db.models import Avg,Max,Min,Sum,Count
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import BookModel

def index(request):
    return HttpResponse("App Home")
def allbooks(request):
    # data = BooksModel.objects.all().order_by('bookname')
    data = BookModel.objects.all().order_by('bookname').reverse()
    # data = BooksModel.objects.all().order_by(Coalesce('bookname','bookname').desc())
    # data = BooksModel.objects.all().order_by(Lower('bookname').desc())
    return render(request, "allbooks.html", {'books': data, "title": "All Books"})

def between(request):
    # data = BooksModel.objects.all().order_by('bookname')
    data = BookModel.objects.filter(price__lt =300) & BookModel.objects.filter(price__gt =100)  .order_by('bookname').reverse()
    # data = BooksModel.objects.all().order_by(Coalesce('bookname','bookname').desc())
    # data = BooksModel.objects.all().order_by(Lower('bookname').desc())
    return render(request, "allbooks.html", {'books': data, "title": "Less than and greater than"})


def searchbooks(request):
    data = BookModel.objects.filter(subject="Python")
    return render(request, "allbooks.html", {'books': data, "title": "Search Subject"})


def searchor(request):
    data = BookModel.objects.filter(subject="Python") | BookModel.objects.filter(subject="Java")
    return render(request, "allbooks.html", {'books': data, "title": "Search Subject Or"})


def aggregates(request):
    # data = (BookModel.objects.filter(subject="2") | BookModel.objects.filter(subject="1")).aggregate(Avg('price'))
    data = BookModel.objects.aggregate(Avg('price'), Max('price'), Min('price'), Sum('price'), Count('price'))
    return render(request, "allbooks.html", {'books': data, "title": "Aggregatess"})

def showForm(request):
    return render(request, "testformbook.html", {'testform': TestBookForm(), "title": "Form"})



def user(request):
    return render(request,"user.html")
