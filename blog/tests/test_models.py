
from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from blog.models import Post, Comment

class PostModelTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create a test post
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            date_posted=timezone.now(),
            author=self.user,
        )

    def test_total_likes(self):
        # Initially, there should be no likes
        self.assertEqual(self.post.total_likes(), 0)

        # Add a like
        self.post.likes.add(self.user)
        self.assertEqual(self.post.total_likes(), 1)

        # Remove the like
        self.post.likes.remove(self.user)
        self.assertEqual(self.post.total_likes(), 0)

    def test_total_saves(self):
        # Initially, there should be no saves
        self.assertEqual(self.post.total_saves(), 0)

        # Add a save
        self.post.saves.add(self.user)
        self.assertEqual(self.post.total_saves(), 1)

        # Remove the save
        self.post.saves.remove(self.user)
        self.assertEqual(self.post.total_saves(), 0)


class CommentModelTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create a test post
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            date_posted=timezone.now(),
            author=self.user,
        )

        # Create a test comment
        self.comment = Comment.objects.create(
            post=self.post,
            name=self.user,
            body='This is a test comment.',
        )

    def test_total_clikes(self):
        # Initially, there should be no comment likes
        self.assertEqual(self.comment.total_clikes(), 0)

        # Add a like to the comment
        self.comment.likes.add(self.user)
        self.assertEqual(self.comment.total_clikes(), 1)

        # Remove the like
        self.comment.likes.remove(self.user)
        self.assertEqual(self.comment.total_clikes(), 0)

    def test_get_absolute_url(self):
        # Check if the get_absolute_url method returns a valid URL
        url = self.comment.get_absolute_url()
        expected_url = f'/post/{self.comment.post.pk}/'  # Replace with your actual URL pattern
        self.assertEqual(url, expected_url)

    def test_comment_str_representation(self):
        # Check the __str__ representation of a comment
        expected_str = f'Test Post - testuser - {self.comment.id}'
        self.assertEqual(str(self.comment), expected_str)
