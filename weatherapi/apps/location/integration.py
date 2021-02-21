from django.conf import settings

import requests

from weatherapi.apps.location import utils


class WeatherAPI(object):
    """Weather API Wrapper which retrieves data via the external API's various
    endpoints for a specific city.
    """
    def __init__(self, city, *arg, **kwargs):
        self.city = city
        self.api_url = settings.WEATHERAPI['URL']
        self.api_key = settings.WEATHERAPI['KEY']

    def get_forecast(self, days):
        """Get a weather forecast for period of time.
        """
        payload = {
            'key': self.api_key,
            'days': days,
            'q': self.city
        }
        response = requests.get(self.api_url, payload)
        return response

    def parse_response(self, response):
        status = response.status_code
        if status != 200:
            response_message = response.json()
            try:
                return response.status_code, response_message['error']['message']
            except KeyError:
                return response.status_code, 'Unknown Error'

        weather_data = response.json()
        forecast_data = weather_data['forecast']['forecastday']

        return response.status_code, utils.calculate_weather_stats(forecast_data)
