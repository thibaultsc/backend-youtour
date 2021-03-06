from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers
from rest_framework.decorators import api_view

from .api_views import *
from . import api_views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tours', TourViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'variations', VariationViewSet)
router.register(r'locations', LocationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^(?P<lang>[a-z][a-z])/tours/', api_views.index, name='index'),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]