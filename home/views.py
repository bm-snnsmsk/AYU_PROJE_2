from django.shortcuts import render

# Create your views here.

def index(request) :
    context = {
        "name" : "Sinan Şimşek </br> Bilgisayar Mühendisliği"
    }
    return render(request, "index.html", context)

