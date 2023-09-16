from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowNotificationsAPIView.as_view(), name='show-notifications-api'),

]
