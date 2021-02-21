from django.urls import include, path

from rest_framework.documentation import include_docs_urls
from rest_framework import routers

from weatherapi.apps.location.api import LocationView

API_TITLE = 'Weather API'

docs_view = include_docs_urls(title=API_TITLE)

urlpatterns = []

# Django rest framework urlpatterns
urlpatterns += [
    path('api/docs/', docs_view),
    path(
        'api/drf/', include(
            'rest_framework.urls', namespace='rest_framework'
        )
    ),
    path('api/locations/<city>/',
        LocationView.as_view(),
        name='location'
    ),
]
