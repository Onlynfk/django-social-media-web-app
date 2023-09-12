
from rest_framework import serializers
from ..models import Post 
from users.api.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
    
    def get_author(self, obj):
        user = obj.author
        if user:
            serializer = UserSerializer(user)
            return serializer.data
        return None
