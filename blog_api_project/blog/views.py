from rest_framework import generics,permissions
from .models import Blog
from .serializers import BlogSerializer
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BlogPostCount
from .serializers import BlogPostCountSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Blog
from .serializers import UserBlogCountSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]


class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'slug' 
    lookup_url_kwarg = 'slug'

@api_view(['GET'])
def blog_post_count(request):
    if request.method == 'GET':
      
        obj, created = BlogPostCount.objects.get_or_create(pk=1)
        serializer = BlogPostCountSerializer(obj)
        return Response(serializer.data)

class UserBlogCountView(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        user_data = []

        for user in users:
            blog_count = Blog.objects.filter(author=user).count()
            user_data.append({
                'user_id': user.id,
                'username': user.username,
                'blog_count': blog_count,
            })

        serializer = UserBlogCountSerializer(user_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
