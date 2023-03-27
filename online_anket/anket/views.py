from django.shortcuts import render

# Create your views here.

def index(request) :
    return render(request, 'anket/index.html')

def hakkimizda(request) :
    return render(request, 'anket/hakkimizda.html')

def iletisim(request) :
    return render(request, 'anket/iletisim.html')
