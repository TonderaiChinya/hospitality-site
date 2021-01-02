from django.shortcuts import render, redirect
# from django.views.generic import ListView, DetailView
from .models import Post, Like


def home(request):
    
    context = {
        'posts': Post.objects.all(),
        'user' : request.user,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove()
        else:
            post_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save()
    return redirect('blog:blog-home')

# class HomeView(ListView):
#     model = Post
#     template_name = 'home.html'
