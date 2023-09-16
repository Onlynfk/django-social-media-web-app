from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from notification.models import Notification
from .serializers import NotificationSerializer


class ShowNotificationsAPIView(APIView):
    def get(self, request):
        user = request.user
        notifications = Notification.objects.filter(user=user).order_by('-date')
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
