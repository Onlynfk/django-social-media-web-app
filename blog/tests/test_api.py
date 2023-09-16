from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from blog.models import Post
from blog.api.serializers import PostSerializer 
from django.contrib.auth.models import User
from rest_framework.test import APITestCase

# I wrote this code


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


class PostCreateAPIViewTestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.test_user = User.objects.create_user(username='testuser5', password='password123')
        self.test_user.profile.is_online = True
        self.test_user.profile.save()
        self.client.force_authenticate(user=self.test_user)

    def test_create_post(self):
        # Define request data
        data = {
            'title': 'Test Post',
            'content': 'Test Content',
        }

        # Send a POST request to create a new post
        response = self.client.post('/api/post/new/', data, format='json')

        # Check if the response status code is 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if a new post was created in the database
        self.assertTrue(Post.objects.filter(title='Test Post').exists())


class PostDetailAPIViewTestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.test_user = User.objects.create_user(username='testuser', password='password123')

        # Create a test post
        self.test_post = Post.objects.create(
            title='Test Post',
            content='Test Content',
            author=self.test_user,
        )

    def test_get_post_detail(self):
        # Send a GET request to retrieve the detail of the test post
        response = self.client.get(f'/api/post/{self.test_post.pk}/')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response data matches the serialized test post
        expected_data = PostSerializer(self.test_post).data
        self.assertEqual(response.data, expected_data)

    def test_get_nonexistent_post_detail(self):
        # Send a GET request to retrieve the detail of a nonexistent post (invalid PK)
        response = self.client.get('/api/post/999999/')

        # Check if the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class PostUpdateDeleteAPIViewTestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.test_user = User.objects.create_user(username='testuser', password='password123')

        # Create a test post authored by the test user
        self.test_post = Post.objects.create(
            title='Test Post',
            content='Test Content',
            author=self.test_user,
        )

        # Log in the test user
        self.client.force_authenticate(user=self.test_user)

    def test_get_post_detail(self):
        # Send a GET request to retrieve the detail of the test post
        response = self.client.get(f'/api/post/{self.test_post.pk}/')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response data matches the serialized test post
        expected_data = PostSerializer(self.test_post).data
        self.assertEqual(response.data, expected_data)


class SearchAPIViewTestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.test_user = User.objects.create_user(username='testuser', password='password123')

        # Create test posts
        self.post1 = Post.objects.create(title='Search Post 1', content='Content 1', author=self.test_user)
        self.post2 = Post.objects.create(title='Search Post 2', content='Content 2', author=self.test_user)
        self.post3 = Post.objects.create(title='Another Post', content='Content 3', author=self.test_user)

    def test_search_posts(self):
        # Send a GET request to search for posts with a specific query
        response = self.client.get(reverse('api-search'), {'query': 'Search'})

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response data contains the expected posts
        expected_data = PostSerializer([self.post1, self.post2], many=True).data
        self.assertEqual(response.data, expected_data)

    def test_search_empty_query(self):
        # Send a GET request with an empty query parameter
        response = self.client.get(reverse('api-search'), {'query': ''})

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response data is an empty list
        self.assertEqual(response.data, [])

    def test_search_no_results(self):
        # Send a GET request with a query that has no matching results
        response = self.client.get(reverse('api-search'), {'query': 'Nonexistent'})

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response data is an empty list
        self.assertEqual(response.data, [])

# end of code I wrote
