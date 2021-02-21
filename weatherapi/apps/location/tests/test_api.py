from django import test

from rest_framework.test import APIClient
import vcr


class APITestCase(test.TestCase):
    """Tests the api endpoints exposed in the agrigated weather data.
    """

    @classmethod
    def setUpTestData(cls):
        super(APITestCase, cls).setUpTestData()
        cls.api_client = APIClient()

    @vcr.use_cassette(
        "weatherapi/apps/location/fixtures/vcr/api.200.yaml",
        record_mode="new_episodes"
    )
    def test_api_endpoint(self):

        # Ensure the endpoint is reachable
        response = self.api_client.get(
            "/api/locations/johannesburg/",
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)



