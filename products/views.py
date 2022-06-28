from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello Products")
    return render(request, 'products/product_list.html')

def atcsda(request):
    return render(request, 'products/atc-sda.html')

def atcsdae(request):
    return render(request, 'products/atc-sdae.html')

def atw01(request):
    return render(request, 'products/atw-01.html')

def atw02(request):
    return render(request, 'products/atw-02.html')

def atges11(request):
    return render(request, 'products/atg-es11.html')

def atges12(request):
    return render(request, 'products/atg-es12.html')

def atges100(request):
    return render(request, 'products/atg-es100.html')

def trainingkit(request):
    return render(request, 'products/training-kit.html')