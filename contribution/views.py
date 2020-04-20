from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
app_name = 'contribution'

def contrib(request):
    return render(request,'contrib/index.html')
def thank(request):
    return render(request,'contrib/thank_you.html')
