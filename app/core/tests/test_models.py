"""
Tests for models.
"""
from django.test import TestCase
# It's always good to use get_user_model it gets the default user model
# in order to get reference to your custom user model.
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful."""
        email = 'test@example.com',
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        # we use user.check_password not user.password to check the hashed pass.
        self.assertTrue(user.check_password(password))
