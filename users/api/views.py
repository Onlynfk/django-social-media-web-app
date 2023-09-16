from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserRegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)


class UserLoginView(ObtainAuthToken):
    permission_classes = (AllowAny,)


class SearchUsersAPIView(APIView):
    def get(self, request):
        query = self.request.query_params.get('query')

        if not query:
            return Response([], status=status.HTTP_200_OK)

        # Perform a case-insensitive search for both title and username
        user = User.objects.filter(username__icontains=query)

        # Serialize the search results
        serializer = UserSerializer(user, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
