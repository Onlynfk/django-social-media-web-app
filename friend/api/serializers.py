from rest_framework import serializers
from friend.models import FriendList

# I wrote this code


class FriendListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendList
        fields = '__all__'
# end of code I wrote
