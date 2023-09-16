from rest_framework import serializers
from friend.models import FriendList


class FriendListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendList
        fields = '__all__'
