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

from django.http import Http404
from django.shortcuts import get_object_or_404

import logging

logger_info = logging.getLogger("info")


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    This view returns the details about a news post. It supports
    GET, POST, PUT, and DELETE methods
    """

    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        post = Post.objects.filter(pk=self.kwargs["pk"])
        if post.exists():
            logger_info.info("Post retrieved successfully")
            return post
        else:
            logger_info.error("This post does not exist!")
            raise Http404

    def delete(self, request, *args, **kwargs):
        post = Post.objects.filter(pk=self.kwargs["pk"])
        if post.exists():
            post = Post.objects.filter(pk=self.kwargs["pk"],
                                       author=self.request.user)
            if post.exists():
                self.destroy(request, *args, **kwargs)
                logger_info.info("Post deleted successfully")
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                logger_info.warning("This is not your post to delete!")
                raise ValidationError(
                    ("This is not your post to delete!"), code="invalid"
                )
        else:
            logger_info.error("This post does not exist!")
            raise Http404

    def put(self, request, *args, **kwargs):
        post = Post.objects.filter(pk=self.kwargs["pk"])
        if post.exists():
            post = Post.objects.filter(pk=self.kwargs["pk"],
                                       author=self.request.user)
            if post.exists():
                self.update(request, *args, **kwargs)
                logger_info.info("Post updated successfully")
                return Response(status=status.HTTP_200_OK)
            else:
                logger_info.warning("This is not your post to update!")
                raise ValidationError(
                    ("This is not your post to update!"), code="invalid"
                )
        else:
            logger_info.error("This post does not exist!")
            raise Http404


class PostListCreateAPIView(generics.ListCreateAPIView):
    """
    This view returns a list of all news posts. It supports
    GET and POST methods
    """

    queryset = Post.objects.all().order_by("vote")
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
        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        return Comment.objects.filter(post=post)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        serializer.save(author=self.request.user, post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_paginated_response(self, data):
        return Response(data, status=status.HTTP_200_OK)


class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    This view returns the details about a comment. It supports
    GET, POST, PUT, and DELETE methods
    """

    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    lookup_field = "id"

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        return Comment.objects.filter(post=post, pk=self.kwargs["id"])

    def delete(self, request, *args, **kwargs):
        comment = Comment.objects.filter(pk=self.kwargs["id"],
                                         author=self.request.user)
        if comment.exists():
            self.destroy(request, *args, **kwargs)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            logger_info.error("This comment does not exist!")
            raise Http404

    def put(self, request, *args, **kwargs):
        comment = Comment.objects.filter(pk=self.kwargs["id"],
                                         author=self.request.user)
        if comment.exists():
            self.update(request, *args, **kwargs)
            return Response(status=status.HTTP_200_OK)
        else:
            logger_info.error("This comment does not exist!")
            raise Http404
