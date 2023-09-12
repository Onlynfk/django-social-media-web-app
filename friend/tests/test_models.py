from django.test import TestCase
from django.contrib.auth.models import User
from friend.models import FriendRequest, FriendList


class FriendListModelTestCase(TestCase):
    def test_friend_list_created_for_user(self):
        # Create a test user
        test_user = User.objects.create_user(
            username='testuser', password='password123')

        # Check if a FriendList was created for the test user
        self.assertTrue(FriendList.objects.filter(user=test_user).exists())

    def test_friend_list_methods(self):
        # Create two test users
        user1 = User.objects.create_user(
            username='user1', password='password1')
        user2 = User.objects.create_user(
            username='user2', password='password2')

        # Ensure FriendLists exist for both users
        friend_list_user1 = FriendList.objects.get(user=user1)
        friend_list_user2 = FriendList.objects.get(user=user2)

        # Test add_friend method
        friend_list_user1.add_friend(user2)
        self.assertTrue(user2 in friend_list_user1.friends.all())

        # Test remove_friend method
        friend_list_user1.remove_friend(user2)
        self.assertFalse(user2 in friend_list_user1.friends.all())

        # Test is_mutual_friend method
        friend_list_user1.add_friend(user2)
        self.assertTrue(friend_list_user1.is_mutual_friend(user2))

        # Test unfriend method
        friend_list_user1.unfriend(user2)
        self.assertFalse(friend_list_user1.is_mutual_friend(user2))
        self.assertFalse(friend_list_user2.is_mutual_friend(user1))

    def test_friend_list_str_method(self):
        # Create a test user
        test_user = User.objects.create_user(
            username='testuser', password='password123')

        # Ensure a FriendList exists for the test user
        friend_list_test_user = FriendList.objects.get(user=test_user)

        expected_str = test_user.username
        self.assertEqual(str(friend_list_test_user), expected_str)


class FriendRequestModelTestCase(TestCase):
    def setUp(self):
        # Create two test users
        self.sender = User.objects.create_user(
            username='sender',
            password='senderpassword'
        )
        self.receiver = User.objects.create_user(
            username='receiver',
            password='receiverpassword'
        )

        # Create FriendRequest instances
        self.friend_request = FriendRequest.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            is_active=True,
        )

    def test_accept_friend_request(self):
        # Accept the friend request
        self.friend_request.accept()

        # Check if the friend request is no longer active
        self.assertFalse(self.friend_request.is_active)

        # Check if sender and receiver are now friends
        sender_friend_list = FriendList.objects.get(user=self.sender)
        receiver_friend_list = FriendList.objects.get(user=self.receiver)
        self.assertTrue(self.receiver in sender_friend_list.friends.all())
        self.assertTrue(self.sender in receiver_friend_list.friends.all())

    def test_decline_friend_request(self):
        # Decline the friend request
        self.friend_request.decline()

        # Check if the friend request is no longer active
        self.assertFalse(self.friend_request.is_active)

    def test_cancel_friend_request(self):
        # Cancel the friend request
        self.friend_request.cancel()

        # Check if the friend request is no longer active
        self.assertFalse(self.friend_request.is_active)
