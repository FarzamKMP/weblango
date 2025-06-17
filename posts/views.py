from django.http import HttpResponse
from .models import Post
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the posts index.")

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comments.filter(post=post).order_by('-created_at')
    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments})