from pyexpat import model
from django.shortcuts import render

from posts.models import Post

# Create your views here.

from django.views.generic import ListView
from .models import Post



class Homepageview(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'