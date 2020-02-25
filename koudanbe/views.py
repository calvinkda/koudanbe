from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(resquest):
    text= """
    <h1> teste de la page koudanbe.cm depuis koudanbe merde </h1>
    """
    return HttpResponse(text)
def acceuil(request):
    return render(request, 'index.html')