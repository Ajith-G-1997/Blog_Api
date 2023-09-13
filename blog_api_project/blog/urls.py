

from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView)
from .views import BlogPostListCreateView, BlogPostDetailView,UserRegistrationView,UserBlogCountView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('posts/', BlogPostListCreateView.as_view(), name='post-list-create'),
    path('posts/<slug:slug>/', BlogPostDetailView.as_view(), name='post-detail'),
    #path('api/blog-post-count/', BlogPostCountAPIView.as_view(), name='blog-post-count-api'),
    path('api/blog-post-count/', views.blog_post_count, name='blog-post-count-api'),
    path('user-blog-counts/', UserBlogCountView.as_view(), name='user-blog-counts'),
]
