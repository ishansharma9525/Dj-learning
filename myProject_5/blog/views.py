from django.shortcuts import render
from datetime import datetime

class user:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

def home(request):
    context ={
        'name': 'Ishan Sharma',
        'email': 'ishan@gamil.com',
        'age': 25,
        "skill": ['Python', 'Django', 'JavaScript'],
        'user': user('Ishan Sharma', 'ishan@gamil.com', 25),
        "blog": {
            'title': 'django template intro',
            'content': '<b>This is the content of my first blog post.</b>',
            'author': 'Ishan Sharma',
            'date_posted': datetime.now(),
            "created_at": datetime(2025, 11, 1, 10, 30 ),     
        },
        "empty_value": None,
    }
    return render(request, 'blog/blog.html', context)

# the context we mentained in the perameter of the return nor it is in dict if it is in array or list then we have to mention the context like this {context} mean in curlly braces
 



# Create your views here.git remote add origin https://github.com/ishansharma9525/Dj-learning.git
