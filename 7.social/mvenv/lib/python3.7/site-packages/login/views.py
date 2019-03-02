from django.shortcuts import render
from .models import Pictures

# Create your views here.
def home(request):
    blog = Pictures.objects
    return render(request, 'home.html', {'blog':blog})