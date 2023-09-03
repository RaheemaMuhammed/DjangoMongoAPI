from django.urls import path
from .views import *
urlpatterns = [
    
    path('posts/',PostList.as_view()),
    path('singleposts/',BlogPost.as_view()),

]