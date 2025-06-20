from posts.models import Post
from rest_framework.decorators import api_view
from rest_framework.response import Response
from posts.serializers import PostSerializer, CommentSerializer
from django.shortcuts import get_object_or_404

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
    
@api_view(['POST'])
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        comment = serializer.save(post=post)
        return Response(CommentSerializer(comment).data, status=201)
    return Response(serializer.errors, status=400)
