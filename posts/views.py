from django.shortcuts import render
from django.views import generic

from .models import Post
from posts import models
# Create your views here.


class HomePageView(generic.ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts_list'
