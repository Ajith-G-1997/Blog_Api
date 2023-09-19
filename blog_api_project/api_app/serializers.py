from rest_framework import serializers
from .models import Item
from rest_framework import serializers
from django.contrib.auth.models import User







class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
class ItemSerializer(serializers.ModelSerializer):
   
    user_details = UserSerializer(source='user_id', read_only=True)

    class Meta:
        model = Item
        fields = ['user_id', 'user_details', 'item_name', 'description', 'file_upload']