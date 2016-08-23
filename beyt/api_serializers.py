from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, generics
from django.db.models import Q

from .models import *


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
        

class TranslateTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslateTour

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
    locales = serializers.SerializerMethodField('get_rigth_language')
    departureLocation = LocationSerializer(read_only=True)
    activities = TourActivitySerializer(many=True,read_only=True)
    def get_rigth_language(self, obj):
        translate_tour = TranslateTour.objects.filter(Q(tour = obj) & (Q(language=self.context['request'].query_params['a']) | Q(type='1')))
        serializer = TranslateTourSerializer(translate_tour, many=True)
        return serializer.data
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
    

    