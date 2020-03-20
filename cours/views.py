from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def cours(request):
    return render(request, 'cours.html')

