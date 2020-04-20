from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'contribution'

urlpatterns = [

    path('', views.contrib, name='acceuil'),
    path('thank/', views.thank, name='thank'),


]



