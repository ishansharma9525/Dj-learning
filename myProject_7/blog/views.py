from django.shortcuts import render
from datetime import datetime

# Create your views here.
def control(request):
    dolo =[
        {"Title" : "Django Basic", "is_featured": True, "Auther" : "Ishan"},
        {"Title" : "Django Advanced", "is_featured": False, "Auther" : ""},
        {"Title" : "Django Rest Framework", "is_featured": False, "Auther" : "Rishav"}
    ]
    context={
        "Dolo" : dolo,
        "Poted_time" : datetime.now(),
        "html" : "<h1> welcome to my blog</h1>"
    }
    return render(request, 'blog/controlflow.html', context)