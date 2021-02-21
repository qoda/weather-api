from django.conf import settings

import requests

from weatherapi.apps.location import utils


class WeatherAPI(object):
    """Weather API Wrapper which retrieves data via the external API's various
    endpoints for a specific city.
    """
    def __init__(self, city, *arg, **kwargs):
        self.city = city
        self.api_url = kwargs.get('api_url', settings.WEATHERAPI['URL'])
        self.api_key = kwargs.get('api_key', settings.WEATHERAPI['KEY'])
        self.calculation_method = kwargs.get(
            'calculation_method', utils.calculate_weather_stats
        )

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
        """Parse the weather data by calling an external calculation method.
        """
        status = response.status_code
        if status != 200:
            response_message = response.json()
            try:
                return response.status_code, response_message['error']['message']
            except KeyError:
                return response.status_code, 'Unknown Error'

        weather_data = response.json()
        forecast_data = weather_data['forecast']['forecastday']

        return response.status_code, self.calculation_method(forecast_data)
