import json

from django import test
from django.utils import timezone

from rest_framework.test import APIClient


class APITestCase(test.TestCase):
    """Tests the api endpoints exposed in the agrigated weather data.
    """

    @classmethod
    def setUpTestData(cls):
        super(APITestCase, cls).setUpTestData()
        cls.api_client = APIClient()

    def test_api_endpoint_reachable(self):

        # Ensure the endpoint is reachable
        response = self.api_client.get(
            "/api/locations/johannesburg/?days=1",
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)


