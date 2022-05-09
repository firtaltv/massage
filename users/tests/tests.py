import json

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User


class UserTest(APITestCase):
    fixtures = ['users/tests/user_fixtures.json', ]

    def setUp(self) -> None:
        self.admin_user = User.objects.get(id=1)
        self.test_user = {
            "password": "pbkdf2_sha256$320000$zChYapqPL2yP7cynuxLgZu$kaOSUfTwQnJnEFBsjMt/kxUyz/HNR27DbRSZh+8J08Y=",
            "last_login": "2022-05-06 21:36:33.090145 +00:00",
            "is_superuser": "true",
            "username": "admin",
            "first_name": "",
            "last_name": "",
            "email": "admin@email.com",
            "is_staff": "true",
            "is_active": "true",
            "date_joined": "2022-05-01 09:11:43.922664 +00:00",
            "profile_photo": None
        }

    def test_get_user(self):
        url = reverse('users:user_profile')
        self.client.force_login(user=self.admin_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        content = json.loads(response.content)
        self.assertEqual(self.test_user['username'], content['username'])

    def test_edit_user(self):
        url = reverse('users:user_profile')
        self.client.force_login(user=self.admin_user)
        response = self.client.patch(url, {'first_name': 'Philip'})
        content = json.loads(response.content)
        self.assertEqual('Philip', content['first_name'])
