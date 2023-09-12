from django.test import TestCase
from django.contrib.auth.models import User
from users.models import Profile

class ProfileModelTestCase(TestCase):
    def test_user_creation_creates_profile(self):
        # Create a test user
        test_user = User.objects.create_user(username='testuser', password='password123')

        # Check if a profile was created for the test user
        self.assertTrue(Profile.objects.filter(user=test_user).exists())

    def test_profile_methods(self):
        # Create a test user
        test_user = User.objects.create_user(username='testuser', password='password123')

        # Test profile_posts method
        self.assertEqual(list(test_user.profile.profile_posts()), list(test_user.post_set.all()))

        # Test get_friends method
        self.assertEqual(list(test_user.profile.get_friends()), list(test_user.profile.friends.all()))

        # Test get_friends_no method
        self.assertEqual(test_user.profile.get_friends_no(), test_user.profile.friends.all().count())

    def test_profile_str_method(self):
        # Create a test user
        test_user = User.objects.create_user(username='testuser', password='password123')

        expected_str = f'{test_user.username} Profile'
        self.assertEqual(str(test_user.profile), expected_str)

