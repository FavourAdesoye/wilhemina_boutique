from django.shortcuts import render
from django.http import HttpResponse


def accessories_view(request):
    return HttpResponse('this is our accessories section')
