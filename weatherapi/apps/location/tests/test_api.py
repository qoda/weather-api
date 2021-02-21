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
        "weatherapi/apps/location/fixtures/vcr/internal.200.yaml"
    )
    def test_api_endpoint(self):

        # Ensure the endpoint is reachable
        response = self.api_client.get(
            "/api/locations/johannesburg/",
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)

    @vcr.use_cassette(
        "weatherapi/apps/location/fixtures/vcr/internal.400.yaml",
        record_mode='new_episodes'
    )
    def test_internal_exceptions(self):

        # Ensure the endpoint is reachable
        response = self.api_client.get(
            "/api/locations/johannesburg/?days=abc",
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            "Forecast days range must be an integer.", response.json()
        )

        # Ensure the endpoint is reachable
        response = self.api_client.get(
            "/api/locations/johannesburg/?days=5",
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            "Forecast days range must be between 1 and 3.", response.json()
        )

    @test.override_settings(WEATHERAPI={
        'KEY': 'fake-key',
        'URL': 'https://api.weatherapi.com/v1/forecast.json'
    })
    @vcr.use_cassette(
        "weatherapi/apps/location/fixtures/vcr/external.403.yaml",
        record_mode='new_episodes'
    )
    def test_external_exceptions(self):

        # Ensure the endpoint is reachable
        response = self.api_client.get(
            "/api/locations/johannesburg/?day=1",
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 401)
        self.assertIn(
            "External API Error: API key is invalid.", response.json()['detail']
        )



