from django.shortcuts import render
from django.http import HttpResponse
from .models import Bag


def bag_view(request):
    bag = {'bags': Bag.objects.all()}
    return render(request, 'products/bagview.html', bag)
# Create your views here.


# def cloth_view(request):
    # clothes = {'clothings': Clothes.objects.all()}
   # return render(request, 'products\clothview.html', clothes)
