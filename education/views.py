from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'education/schedule.html')