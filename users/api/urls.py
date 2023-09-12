from django.urls import path
from .views import UserRegistrationView, UserLoginView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='api-user-register'),
    path('login/', UserLoginView.as_view(), name='api-user-login'),
]
