from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello Products")
    return render(request, 'products/atc-sda.html')