from django.contrib.auth.models import User
from .models import Tour, Activity, Variation
from rest_framework import serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
# TOUR Serializers define the API representation.
class TourSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tour

# TOUR ViewSets define the view behavior.
class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    
    
# Activity Serializers define the API representation.
class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity

# Activity ViewSets define the view behavior.
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    
# Variation Serializers define the API representation.
class VariationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Variation

# Variation ViewSets define the view behavior.
class VariationViewSet(viewsets.ModelViewSet):
    queryset = Variation.objects.all()
    serializer_class = VariationSerializer