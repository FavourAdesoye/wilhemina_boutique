# from django.http import HttpResponse
from django.shortcuts import render


def homeview(request):
    return render(request, 'products\Home\homeview.html')
