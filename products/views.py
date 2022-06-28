from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello Products")
    return render(request, 'products/atc-sda.html')

def atcsda(request):
    return render(request, 'products/atc-sda.html')

def atcsdae(request):
    return render(request, 'products/atc-sdae.html')

def atw01(request):
    return render(request, 'products/atw-01.html')

def atw02(request):
    return render(request, 'products/atw-02.html')