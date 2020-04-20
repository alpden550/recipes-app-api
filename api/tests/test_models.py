from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successfull"""
        email = 'test@gmail.com'
        password = 'password'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for new user is normalized"""
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'password')

        self.assertEqual(user.email, email.lower())
