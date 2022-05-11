import json

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User


class UserTest(APITestCase):
    fixtures = ['users/tests/user_fixtures.json', ]

    def setUp(self) -> None:
        self.admin_user = User.objects.get(id=1)

    def test_get_user(self):
        url = reverse('users:user_profile')
        self.client.force_login(user=self.admin_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        content = response.data
        print(content)
        self.assertEqual(self.admin_user.username, content['username'])
        self.assertEqual(self.admin_user.first_name, content['first_name'])
        self.assertEqual(self.admin_user.last_name, content['last_name'])
        self.assertEqual(self.admin_user.email, content['email'])
        self.assertEqual(self.admin_user.profile_photo, content['profile_photo'])

    def test_edit_user(self):
        url = reverse('users:user_profile')
        self.client.force_login(user=self.admin_user)
        response = self.client.patch(url, {'first_name': 'Philip', 'email': 'admin1@email.com'})
        content = response.data
        self.assertEqual('Philip', content['first_name'])
        self.assertEqual(self.admin_user.email, content['email'])
