from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello Introduce")
    return render(request, 'introduce/greeting.html')

def history(request):
    return render(request, 'introduce/history.html')