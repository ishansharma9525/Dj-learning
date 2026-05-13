from django.shortcuts import render
from datetime import datetime

def blog_detail(request):
    current_time = datetime.now()
    post = {
        "title" : "story told by life",
        "description" : "life is a story, and we are the authors of our own stories. We have the power to shape our lives and create the narrative we want to tell. Every experience, every choice, and every moment contributes to the story we are writing. Embrace the journey, learn from the challenges, and celebrate the triumphs. Your story is unique and valuable, so make it a story worth telling.",
        "author" : "Ishan Sharma",
        "created_at" : datetime(2024, 6, 1, 10, 0, 0),
        "Skill" : ["django", "python", "html" , "CSS" , "reactjs"],
        "price" : 125,
        "number" : 36,

        

    }
    return render(request, 'blog/blog_detail.html', {'current_time': current_time, 'post': post})
# Create your views here.
