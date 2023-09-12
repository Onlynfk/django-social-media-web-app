from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from blog.models import Post
from blog.api.serializers import PostSerializer 
from django.contrib.auth.models import User

class PostListAPIViewTestCase(TestCase):
    def setUp(self):
        author = User.objects.create(username="testuser", email="testuser@email.com", password="hellopass")
        # Create some test posts
        self.post1 = Post.objects.create(
            title='Test Post 1',
            author=author,
            content='This is test post 1 content.',
        )
        self.post2 = Post.objects.create(
            title='Test Post 2',
            content='This is test post 2 content.',
            author=author
        )

        # Create an API client for making requests
        self.client = APIClient()

    def test_post_list_api_view(self):
        # Get the URL for the PostListAPIView
        url = reverse('api-post-list')

        # Send a GET request to the view
        response = self.client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Deserialize the response data using the serializer
        expected_data = PostSerializer([self.post1, self.post2], many=True).data

        # Check if the response data matches the expected data
        self.assertEqual(response.data, expected_data)
