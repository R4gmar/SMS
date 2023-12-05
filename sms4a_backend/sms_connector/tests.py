from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from unittest.mock import patch
from .utils import send_sms_mock  # Импортируем мокированный метод

class SMSTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    @patch('sms_connector.utils.send_sms', send_sms_mock)  # Патчим send_sms на мок
    def test_send_sms(self):
        data = {
            "recipients": ["+48576701979"],
            "text": "Hello world!",
        }

        response = self.client.post('/sms/send-sms/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['status'], 'SMS sent successfully')
