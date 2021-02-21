from django.urls import include, path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from weatherapi.apps.location.api import LocationView


API_TITLE = 'Weather API'

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

# Django rest framework urlpatterns
urlpatterns = [
    path(
        'api/swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'api/redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
    path('api/locations/<city>/',
        LocationView.as_view(),
        name='location'
    )
]
