from rest_framework import views
from rest_framework.response import Response

from weatherapi.apps.location.integration import WeatherAPI


class LocationView(views.APIView):
    """View the agrigated weather data for a particular city
    """
    http_method_names = ['get', 'options']

    def get(self, request, format=None, **kwargs):
        """Return the agrigated data for specific city including:

        - Maximum temperature
        - Minimum temperature
        - Average temperature
        - Median temperature
        """
        city = kwargs.get('city')

        weather_api = WeatherAPI(city=city)
        raw_response = weather_api.get_forecast(days=3)
        status_code, parsed_response = weather_api.parse_response(raw_response)
        return Response(parsed_response)
