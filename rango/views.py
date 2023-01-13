from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    about_link = "<br><a href='/rango/about/'>About</a>"
    return HttpResponse("Rango says hey there partner!" + about_link)


def about(request):
    index_link = "<br><a href='/rango/'>Index</a>"
    return HttpResponse('Rango says here is the about page.' + index_link)

# Create your views here.
