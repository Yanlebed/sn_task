from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from ..models import Post

User = get_user_model()
factory = APIRequestFactory()


def create_user(**params):
    return User.objects.create_user(**params)


def sample_post(user, **params):
    defaults = {
        'title': 'Sample recipe',
        'body': 'Sample body',
    }
    defaults.update(params)
    return Post.objects.create(user=user, **params)


def detail_url(post_id):
    # Return post detail url
    return reverse('posts:post-detail', args=[post_id])


class ViewSetTest(TestCase):
    # Test unauthenticated post API access
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

    def test_retrieve_post_success(self):
        # Test retrieving profile for logged in user
        sample_post(user=self.user)
        sample_post(user=self.user)

        res = self.client.get('/api/posts/')

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_view_post_detail(self):
        # Test viewing a post detail
        post = sample_post(user=self.user)

        url = '/api/posts/'+str(post.id)+'/'
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_update_post(self):
        # test updating a recipe with patch
        post = sample_post(user=self.user)

        payload = {'title': 'New sample post', 'body': 'New sample body'}
        url = '/api/posts/' + str(post.id) + '/'
        self.client.patch(url, payload)

        post.refresh_from_db()
        self.assertEqual(post.title, payload['title'])
        self.assertEqual(post.body, payload['body'])
