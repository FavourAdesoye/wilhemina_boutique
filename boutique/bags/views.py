from django.shortcuts import render
from django.http import HttpResponse


def bag_view(request):
    return HttpResponse('this is our bags  section')
# Create your views here.
