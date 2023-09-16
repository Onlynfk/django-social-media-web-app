from django.urls import path
from blog.api import views

urlpatterns = [
    path('posts/', views.PostListAPIView.as_view(), name='api-post-list'),
    path('post/new/', views.PostCreateAPIView.as_view(), name='api-post-new'),
    path('post/<int:pk>/', views.PostDetailAPIView.as_view(), name='api-post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateDeleteAPIView.as_view(), name='api-post-update'),
    path('post/<int:pk>/delete/', views.PostUpdateDeleteAPIView.as_view(), name='api-post-delete'),
    path('search/', views.SearchAPIView.as_view(), name='api-search'),
    path('user_posts/', views.UserPostListView.as_view(), name='api-user-posts'),
    path('saved-posts/', views.SavedPostsAPIView.as_view(), name='api-all-save'),

]
