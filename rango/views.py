from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #what the bold message will be
    context_dic = {'boldmessage':'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request,'rango/index.html',context=context_dic)


def about(request):
    context_dic = {'boldmessage':'This tutorial has been put together by Bobi'}
    return render(request,'rango/about.html',context=context_dic)

