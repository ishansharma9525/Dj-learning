from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, welcome to the blog!")
# Create your views here.

def about(request):
    a = (10/2) + 50
    return HttpResponse(f"The result is {a}.")