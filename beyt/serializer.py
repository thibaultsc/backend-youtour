from django.contrib.auth.models import User
from .models import Tour, Activity, Variation, TranslateTour, Location, TourActivity, TourClean
from rest_framework import serializers, viewsets, generics

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
#TranslateTour Serializers
class TranslateTourSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TranslateTour
        fields = ('title', 'description', 'slug', 'language', 'type')

#TranslateTour Serializers
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
        
class TranslateTourViewSet(viewsets.ModelViewSet):
    queryset = TranslateTour.objects.all()
    serializer_class = TranslateTourSerializer
    
# TOUR Serializers define the API representation.
class TourSerializer(serializers.HyperlinkedModelSerializer):
    locales = TranslateTourSerializer(many=True, read_only=True)
    departureLocation = LocationSerializer(read_only=True)
    activities = TourActivitySerializer(many=True,read_only=True)
    class Meta:
        model = Tour

# TOUR ViewSets define the view behavior.
class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

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
    
# Location Serializers define the API representation.
class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location

# Variation ViewSets define the view behavior.
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    
    
class TourCleanSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    slug = serializers.CharField(max_length=255)
    hotelPickupAccepted = serializers.BooleanField()
    
# Variation ViewSets define the view behavior.
class  TourCleanViewSet(generics.ListCreateAPIView):
    queryset = Tour.objects.all()
    query = []
    serializer_class = TourCleanSerializer
    permission_classes = (IsAdminUser,)

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        query = self.get_query()
        for r in queryset:
          r = TourClean(r,'en')
          query.append(r)
          value 
        serializer = TourCleanSerializer(query, many=True)
        return Response(serializer.data)
    