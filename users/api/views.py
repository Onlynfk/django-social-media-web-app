from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer, UserSerializer, ProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import Profile

# I wrote this code


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


class ProfileListAPIView(ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.all().exclude(user=self.request.user)


class ProfileDetailAPIView(RetrieveAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile

# end of code I wrote
