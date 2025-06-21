from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from posts.models import Post
from posts.serializers import PostSerializer, CommentSerializer

class AllWeblogs(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class DetailWeblog(APIView):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)

class CreateComment(APIView):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        comments = post.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save(post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
