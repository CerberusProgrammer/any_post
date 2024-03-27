from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Post

def posts(request):
    posts = Post.objects.all().order_by('-id')[:10]
    return render(request, 'posts.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post.html', {'post': post})
