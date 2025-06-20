from .models import Post
from django.shortcuts import render

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comments.order_by('-created_at')  # کوئری بهینه شده
    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments})