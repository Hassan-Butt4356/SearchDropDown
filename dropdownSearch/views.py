from django.shortcuts import render
from .forms import PostCreateForm
from .models import Post
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from dal import autocomplete
from django.views.generic.list import ListView

class AllPosts(ListView):
    model=Post
    queryset=Post.objects.all()
    template_name='dropdownSearch/home.html'

class CreatePost(CreateView):
    model=Post
    form_class=PostCreateForm
    template_name='dropdownSearch/create.html'
    success_url=reverse_lazy('home')

