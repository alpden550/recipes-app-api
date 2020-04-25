from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Tag, Recipe
from recipe.serializers import TagSerializer

TAG_URL = reverse('recipe:tag-list')


class PublicTagsApiTests(TestCase):
    """"Test the publicly available tags API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required to retrieving tags"""
        response = self.client.get(TAG_URL)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTagsApiTests(TestCase):
    """Test the authorized user tags API"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@mail.com',
            'password',
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_tags(self):
        """Test retrieving tags"""
        Tag.objects.create(user=self.user, name='Vegan')
        Tag.objects.create(user=self.user, name='Dessert')

        response = self.client.get(TAG_URL)
        tags = Tag.objects.all().order_by('-name')
        serializer = TagSerializer(tags, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_tags_limited_to_user(self):
        """Test that tags returned are for the authenticated user"""
        user2 = get_user_model().objects.create_user(
            'another@mail.com',
            'password',
        )
        Tag.objects.create(user=user2, name='Fruity')
        tag = Tag.objects.create(user=self.user, name='Food')

        response = self.client.get(TAG_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(tag.name, response.data[0]['name'])

    def test_create_tag_successful(self):
        """"Test creating a new tag"""
        payload = {'name': 'Test Tag'}
        self.client.post(TAG_URL, payload)

        exists = Tag.objects.filter(user=self.user, name=payload['name']).exists()

        self.assertTrue(exists)

    def test_create_tag_invalid(self):
        """Test creating a new tag with invalid payload"""
        payload = {'name': ''}
        response = self.client.post(TAG_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_tags_assigned_to_recipes(self):
        """Test filtering tags by those assigned to recipes"""
        tag1 = Tag.objects.create(user=self.user, name='Breakfast')
        tag2 = Tag.objects.create(user=self.user, name='Dinner')
        recipe = Recipe.objects.create(
            user=self.user,
            title='Coriander eggs on toasts',
            time_minutes=15,
            price=7.00,
        )
        recipe.tags.add(tag1)

        response = self.client.get(TAG_URL, {'assigned_only': 1})
        serializer1 = TagSerializer(tag1)
        serializer2 = TagSerializer(tag2)

        self.assertIn(serializer1.data, response.data)
        self.assertNotIn(serializer2.data, response.data)

    def test_retrieve_tag_assigned_unique(self):
        """Test filtering tags by assigned returns unique items"""
        tag1 = Tag.objects.create(user=self.user, name='Breakfast')
        Tag.objects.create(user=self.user, name='Dinner')
        recipe1 = Recipe.objects.create(
            user=self.user,
            title='Coriander eggs on toasts',
            time_minutes=15,
            price=7.00,
        )
        recipe2 = Recipe.objects.create(
            user=self.user,
            title='Porridge',
            time_minutes=1245,
            price=7.00,
        )
        recipe1.tags.add(tag1)
        recipe2.tags.add(tag1)

        response = self.client.get(TAG_URL, {'assigned_only': 1})

        self.assertEqual(len(response.data), 1)
