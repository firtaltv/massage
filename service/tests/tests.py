from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User


class UserTest(APITestCase):
    fixtures = ['service/tests/massage_fixtures.json', ]

    def setUp(self) -> None:
        self.user_1 = User.objects.get(id=1)

    def test_get_massage_client(self):
        expected_data = {
            'pk': 2,
            'therapist':
                {
                    'pk': 2,
                    'last_name': 'Stoika',
                    'first_name': 'Philippp'
                 },
            'client':
                {
                    'pk': 1,
                    'last_name': 'Super',
                    'first_name': 'Admin'
                 },
            'start_time': '2022-05-27T16:19:52Z',
            'end_time': '2022-05-27T17:19:52Z',
            'status': 'TBD'
            }
        url = reverse('service:client_massages_list')
        self.client.force_login(user=self.user_1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertDictEqual(dict(response.data[0]), expected_data)

    def test_get_massage_therapist(self):
        expected_data = {
            'pk': 1,
            'therapist':
                {
                    'pk': 1,
                    'last_name': 'Super',
                    'first_name': 'Admin'
                },
            'client':
                {
                    'pk': 2,
                    'last_name': 'Stoika',
                    'first_name': 'Philippp'
                },

            'start_time': '2022-05-27T15:19:52Z',
            'end_time': '2022-05-27T16:19:52Z',
            'status': 'TBD'
        }
        url = reverse('service:therapist_massages_list')
        self.client.force_login(user=self.user_1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertDictEqual(dict(response.data[0]), expected_data)


class ScheduleTest(APITestCase):
    fixtures = ['service/tests/schedule_fixtures.json', ]

    def setUp(self) -> None:
        self.user_1 = User.objects.get(id=1)

    def test_get_therapist_schedule(self):
        expected_data = {
            'pk': 1,
            'therapist':
                {
                    'pk': 1,
                    'last_name': 'Super',
                    'first_name': 'Admin'
                },
            "days": ["Tuesday", "Thursday"],
            "start_time": "11:00:00",
            "end_time": "16:00:00"
        }
        url = reverse('service:therapist_schedule_object', kwargs={'pk': self.user_1.id})
        self.client.force_login(user=self.user_1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)
        self.assertDictEqual(dict(response.data), expected_data)
