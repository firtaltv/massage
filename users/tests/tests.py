from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User


class UserTest(APITestCase):
    fixtures = ['users/tests/user_fixtures.json', ]

    def setUp(self) -> None:
        self.admin_user = User.objects.get(id=1)

    def test_get_user(self):
        expected_data = {
            "pk": 1,
            "username": "admin",
            "first_name": "",
            "last_name": "",
            "email": "admin@email.com",
            "profile_photo": None
        }
        url = reverse('users:user_profile')
        self.client.force_login(user=self.admin_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data, expected_data)

    def test_edit_user(self):
        url = reverse('users:user_profile')
        self.client.force_login(user=self.admin_user)
        response = self.client.patch(url, {'first_name': 'Philip', 'email': 'admin1@email.com'})
        self.assertEqual(response.data['first_name'], 'Philip')
        self.assertEqual(response.data['email'], self.admin_user.email)
