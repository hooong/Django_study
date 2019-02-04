from django.shortcuts import render, get_object_or_404
from .models import Portfolio

def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios': portfolios})

def view(request, img_id):
    img = get_object_or_404(Portfolio, pk = img_id)
    return render(request, 'view.html', {'img': img})

