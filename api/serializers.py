from rest_framework import serializers
from .models import Post, Vote, Comment

class PostDetailSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    author_id = serializers.ReadOnlyField(source='author.id')
    votes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'author_name', 'author_id', 'creation_date', 'votes', 'comments']

    def get_votes(self, post):
        return Vote.objects.filter(post=post).count()

    def get_comments(self, post):
        c_qs = Comment.objects.filter(post=post)
        comments = CommentDetailSerializer(c_qs, many=True).data
        return comments

class PostListSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'creation_date', 'votes',  'author_name']

    def get_votes(self, post):
        return Vote.objects.filter(post=post).count()

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']

class CommentDetailSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'author_name', 'content', 'creation_date']

class CommentCreateSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'author_name', 'content', 'creation_date']

