
from rest_framework import serializers
from ..models import Post 

# I wrote this code


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
# end of code I wrote
