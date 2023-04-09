from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('hakkimizda', views.hakkimizda, name="hakkimizda"),
    path('iletisim', views.iletisim, name="iletisim"),
    path('anketler', views.anketler, name="anketler"),
    
]
