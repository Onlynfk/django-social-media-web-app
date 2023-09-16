from django.test import TestCase
from django.contrib.auth.models import User
from notification.models import Notification

# I wrote this code


class NotificationModelTestCase(TestCase):
    def setUp(self):
        # Create test users
        self.sender_user = User.objects.create_user(username='sender', password='password1')
        self.receiver_user = User.objects.create_user(username='receiver', password='password2')

    def test_notification_creation(self):
        # Create a notification
        notification = Notification.objects.create(
            post=None,
            sender=self.sender_user,
            user=self.receiver_user,
            notification_type=1,  # Assuming 'Like' notification type
            text_preview='Notification Text',
        )

        # Check if the notification was created successfully
        self.assertEqual(notification.post, None)
        self.assertEqual(notification.sender, self.sender_user)
        self.assertEqual(notification.user, self.receiver_user)
        self.assertEqual(notification.notification_type, 1)
        self.assertEqual(notification.text_preview, 'Notification Text')
        self.assertFalse(notification.is_seen)

    def test_notification_str_method(self):
        notification = Notification.objects.create(
            post=None,
            sender=self.sender_user,
            user=self.receiver_user,
            notification_type=1,  # Assuming 'Like' notification type
            text_preview='Notification Text',
        )

        expected_str = f'{notification.id} - None - {self.sender_user.username} - {self.receiver_user.username} - 1'
        self.assertEqual(str(notification), expected_str)

    def test_notification_default_values(self):
        notification = Notification.objects.create(
            post=None,
            sender=self.sender_user,
            user=self.receiver_user,
            notification_type=1,  # Assuming 'Like' notification type
            # No text_preview provided
        )

        # Check default values
        self.assertEqual(notification.post, None)
        self.assertEqual(notification.sender, self.sender_user)
        self.assertEqual(notification.user, self.receiver_user)
        self.assertEqual(notification.notification_type, 1)
        self.assertEqual(notification.text_preview, '')
        self.assertFalse(notification.is_seen)

# end of code I wrote
