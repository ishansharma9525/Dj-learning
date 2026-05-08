from django.urls import path, re_path
from . import views

urlpatterns = [
    path('post/<int:post_id>/', views.post_details, name='post_details'),
    path('user/<str:username>/', views.user_profile, name='user_profile'), 

    re_path(r'^artical/(?p<year>[0-9]{4})/$',views.artical_year, name='artical_year'),
]
