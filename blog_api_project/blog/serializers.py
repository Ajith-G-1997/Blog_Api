from rest_framework import serializers
from .models import Blog
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
# serializers.py

from rest_framework import serializers
from .models import BlogPostCount

class BlogPostCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostCount
        fields = ['count']

# serializers.py



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user



class UserBlogCountSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    username = serializers.CharField(max_length=150)
    blog_count = serializers.IntegerField()
