from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, generics

from .models import *


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
    
#TranslateTour Serializers
class TranslateTourSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TranslateTour
        fields = ('title', 'description', 'slug', 'language', 'type')

#LocationSerializer
class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('url','addressLocality', 'latitude', 'longitude')
        
#Activity Serializers
class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        
#TourActivity Serializers
class TourActivitySerializer(serializers.HyperlinkedModelSerializer):
    activity = ActivitySerializer(read_only=True)
    class Meta:
        model = TourActivity
        fields = ('order', 'activity')
    
# TOUR Serializers define the API representation.
class TourSerializer(serializers.HyperlinkedModelSerializer):
    locales = TranslateTourSerializer(many=True)
    departureLocation = LocationSerializer(read_only=True)
    activities = TourActivitySerializer(many=True,read_only=True)
    class Meta:
        model = Tour
    
# Variation Serializers define the API representation.
class VariationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Variation
    
# Location Serializers define the API representation.
class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
    
class TourCleanSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    slug = serializers.CharField(max_length=255)
    hotelPickupAccepted = serializers.BooleanField()
    