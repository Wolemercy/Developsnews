from django.urls import path
from . import views

urlpatterns = [
    # posts
    path('posts/', (views.PostListCreateAPIView.as_view()), name='post-list-create'),
    path('posts/<int:pk>/', views.PostDetailAPIView.as_view(), name='post-detail'),
    path('posts/<int:pk>/vote/', views.VoteCreateAPIView.as_view(), name='post-vote'),

    # comments
    path('posts/<int:pk>/comments/', views.CommentListCreateAPIView.as_view(), name='post-comments'),
    path('posts/<int:pk>/comments/<int:id>/', views.CommentDetailAPIView.as_view(), name='post-comments-detail'),

]
