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

    def test_new_user_invalid_email(self):
        """Test creating user with no email raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'password')

    def test_creating_superuser(self):
        """Test cretaing a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'password',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
