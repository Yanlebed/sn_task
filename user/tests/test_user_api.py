from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()

REGISTER_URL = reverse('user:register')
SELF_URL = reverse('user:self')


def create_user(**params):
    return User.objects.create_user(**params)


class PublicUserApiTest(TestCase):
    # Test the users API public

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        # Test creating valid user with valid payload is successful
        payload = {
            'email': 'test@gmail.com',
            'password': 'testpass',
            'username': 'testname'
        }
        res = self.client.post(REGISTER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(**res.data)
        # check if user created
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        # Test creating a user that already exists fails
        payload = {'email': 'test@gmail.com', 'password': 'testpass', 'username': 'testname'}
        create_user(**payload)

        res = self.client.post(REGISTER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_user_unauthorized(self):
        # Test that authentication is required for users
        res = self.client.get(SELF_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateUserApiTests(TestCase):
    # Test API requests that require authentication

    def setUp(self):
        self.user = create_user(
            email='test@gmail.com',
            password='testpass',
            username='testname'
        )
        self.client = APIClient()
        # creates a reusable client
        self.client.force_authenticate(user=self.user)
        # makes easy to simulate making authenticated requests


    def test_retrieve_profile_success(self):
        # Test retrieving profile for logged in user
        res = self.client.get(SELF_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {
            'username': self.user.username,
            'email': self.user.email
        })

    def test_post_me_not_allowed(self):
        # Test that POST is not allowed on the me url
        res = self.client.post(SELF_URL, {})
        # {} - post the empty object
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)