from .models import Post
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer

@api_view(['GET'])
def AllIndex(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def index(request, post_id):
    try:
        posts = Post.objects.get(id=post_id)
        serializer = PostSerializer(posts)
        return Response(serializer.data)
    except Exception as e:
        return Response({'detail':'Post not exist'}, status=400)

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comments.filter(post=post).order_by('-created_at')
    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments})