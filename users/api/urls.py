from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='api-user-register'),
    path('login/', views.UserLoginView.as_view(), name='api-user-login'),
    path('users/', views.SearchUsersAPIView.as_view(), name='api-search-users'),
    path('profiles/', views.ProfileListAPIView.as_view(), name='profile-list-api'),
    path('profile/', views.ProfileDetailAPIView.as_view(), name='profile-detail-api'),

]
