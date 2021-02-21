from rest_framework import views
from rest_framework.response import Response


class LocationView(views.APIView):
    """
    View the agrigated weather data for a particular city
    """
    http_method_names = ['get', 'options']

    def get(self, request, format=None, **kwargs):
        """
        Return the agrigated data for specific city including:

        - Maximum temperature
        - Minimum temperature
        - Average temperature
        - Median temperature
        """
        weather_data = {
            'maximum': 20.4,
            'minimu': 11.0,
            'average': 15.7,
            'median': 14.2,
        }
        return Response(weather_data)
