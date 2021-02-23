from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from todoapp.models import Post
from todoapp.models import Comment
from todoapp.serializers import PostSerializer
from todoapp.serializers import CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        post_serializer = PostSerializer(data=request.data)
        if post_serializer.is_valid(raise_exception=True):
            post_result = post_serializer.save()
            comment_data = {
                "post_id": post_result.id,
                "contents": request.data["post"]["contents"],
            }
        comment_serializer = CommentSerializer(data=comment_data)
        if comment_serializer.is_valid(raise_exception=True):
            comment_serializer.save()
            return Response({"message": "Operate successfully"}, status=status.HTTP_201_CREATED)
        

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
