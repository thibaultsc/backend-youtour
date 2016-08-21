from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, viewsets

from .serializer import UserViewSet, TourViewSet, ActivityViewSet, VariationViewSet,LocationViewSet, TranslateTourViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tours', TourViewSet)
router.register(r'translatetours', TranslateTourViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'variations', VariationViewSet)
router.register(r'locations', LocationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]