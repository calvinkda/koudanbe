from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(resquest):
    text = """

    <h1> KOUDANBE.CM </h1>
    """
    return HttpResponse(text)
def acceuil(request):
    return render(request,'index.html')