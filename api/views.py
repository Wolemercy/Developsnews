from rest_framework import generics, mixins, permissions, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import Post, Vote, Comment
from .serializers import (
    CommentDetailSerializer,
    PostDetailSerializer,
    PostListSerializer,
    VoteSerializer,
    CommentCreateSerializer,
)

# Create your views here.


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    This view returns the details about a news post. It supports
    GET, POST, PUT, PATCH, and DELETE methods
    """

    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):

        return Post.objects


class PostListCreateAPIView(generics.ListCreateAPIView):
    """
    This view returns a list of all news posts. It supports
    GET and POST methods
    """

    queryset = Post.objects.all().order_by('vote')
    serializer_class = PostListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_paginated_response(self, data):
        return Response(data, status=status.HTTP_200_OK)


class VoteCreateAPIView(generics.CreateAPIView, mixins.DestroyModelMixin):
    serializer_class = VoteSerializer

    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs["pk"])
        return Vote.objects.filter(voter=user, post=post)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError("You have already voted for this post")
        serializer.save(
            voter=self.request.user,
            post=Post.objects.get(pk=self.kwargs["pk"])
        )

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError("You never voted for this post")


class CommentListCreateAPIView(generics.ListCreateAPIView):
    """
    This view returns a list of all news posts. It supports
    GET and POST methods
    """

    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

    def get_queryset(self):
        post = Post.objects.get(pk=self.kwargs["pk"])
        return Comment.objects.filter(post=post)

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs["pk"])
        serializer.save(author=self.request.user, post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_paginated_response(self, data):
        return Response(data, status=status.HTTP_200_OK)


class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    This view returns the details about a comment. It supports
    GET, POST, PUT, PATCH, and DELETE methods
    """

    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    lookup_field = "id"

    def get_queryset(self):
        post = Post.objects.get(pk=self.kwargs["pk"])
        return Comment.objects.filter(post=post, pk=self.kwargs["id"])
