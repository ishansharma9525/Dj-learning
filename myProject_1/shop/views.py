# from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Shop home page")

def product(request):
    return HttpResponse("Shop product page")
# Create your views here.
