from django.shortcuts import render
from .models import Clothes
# from django.shortcuts import HttpResponse


def cloth_view(request):
    clothes = {'clothings': Clothes.objects.all()}
    return render(request, 'products\clothview.html', clothes)
