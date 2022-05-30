from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User


class UserTest(APITestCase):
    fixtures = ['service/tests/massage_fixtures.json', ]

    def setUp(self) -> None:
        self.user_1 = User.objects.get(id=1)
        self.user_2 = User.objects.get(id=2)

    def test_get_massage_client(self):
        url = reverse('service:client_massage_list')
        self.client.force_login(user=self.user_1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['client']['pk'], 1)

    def test_get_massage_therapist(self):
        url = reverse('service:therapist_massage_list')
        self.client.force_login(user=self.user_2)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['therapist']['pk'], 2)
