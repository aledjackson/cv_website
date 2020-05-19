from django.shortcuts import render
from django.http import HttpResponse
from .models import intro

# Create your views here.
def index(request) -> HttpResponse:
    return render(request, 'home/index.html',{"intro" : intro()})
