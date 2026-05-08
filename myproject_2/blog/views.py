# from django.shortcuts import render
from django.http import HttpResponse

def post_details(request, post_id):
    return HttpResponse(f"<h1>Post Details for Post ID: {post_id}</h1>")

def user_profile(request, username):
    return HttpResponse(f"<h1>User Profile for Username: {username}</h1>")

def artical_year(request, year):
    return HttpResponse(f"<h1>Articles from the Year: {year}</h1>")
# Create your views here.
