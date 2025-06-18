from django.http import HttpResponse
from .models import Post
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def index(request):
    try:
        posts = Post.objects.all()
        return Response({
            'message': 'Welcome to the Weblog API',
            'posts': [{'id': post.id, 'title': post.title} for post in posts]
        })
    except Exception as e:
        return Response({"Error": "Something went wrong"}, status=400)

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comments.filter(post=post).order_by('-created_at')
    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments})