from django.shortcuts import render
# from django.views.generic import ListView, DetailView
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# class HomeView(ListView):
#     model = Post
#     template_name = 'home.html'
