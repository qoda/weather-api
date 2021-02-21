from rest_framework import exceptions, serializers, status, views
from rest_framework.response import Response

from weatherapi.apps.location.integration import WeatherAPI

from rest_framework.exceptions import APIException
from django.utils.encoding import force_text
from rest_framework import status


class AuthAPIException(exceptions.APIException):
    status_code = status.HTTP_401_UNAUTHORIZED


class BadRequestAPIException(exceptions.APIException):
    status_code = status.HTTP_400_BAD_REQUEST


class LocationView(views.APIView):
    """View the agrigated weather data for a particular city
    """
    http_method_names = ['get', 'options']
    external_excepttion_map = {
        400: BadRequestAPIException,
        401: AuthAPIException,
    }

    def get(self, request, format=None, **kwargs):
        """Return the agrigated data for specific city including:

        - Maximum temperature
        - Minimum temperature
        - Average temperature
        - Median temperature
        """
        city = kwargs.get('city')
        try:
            days = int(request.query_params.get('days', 1))
        except ValueError:
            raise serializers.ValidationError(
                'Forecast days range must be an integer.', 400
            )
        if 3 < days > 1:
            raise serializers.ValidationError(
                'Forecast days range must be between 1 and 3.', 400
            )

        weather_api = WeatherAPI(city=city)
        raw_response = weather_api.get_forecast(days=days)
        status_code, parsed_response = weather_api.parse_response(raw_response)

        if status_code == 200:
            return Response(parsed_response)
        else:
            try:
                exception = self.external_excepttion_map[status_code]
            except KeyError:
                exception = exceptions.APIException
            raise exception(
                detail='External API Error: {}'.format(parsed_response)
            )
