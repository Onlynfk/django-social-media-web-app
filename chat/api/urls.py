from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_enroll, name='api-room-enroll'),
    path('friends/', views.my_friends, name='api-my-friends'),
    path('room/<str:room_name>/<int:friend_id>/', views.room, name='room-api'),   
]
