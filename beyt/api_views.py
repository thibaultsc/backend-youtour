from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .api_serializers import *
from .models import *

@api_view()
def index(request, lang):
  queryset = Tour.objects.all()
  query = []
  for r in queryset:
    t = TourCleanSerializer(TourLanguage(r,lang))
    query.append(t.data)
  return Response(query)

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TranslateTourViewSet(viewsets.ModelViewSet):
    queryset = TranslateTour.objects.all()
    serializer_class = TranslateTourSerializer

# TOUR ViewSets define the view behavior.
class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

# Activity ViewSets define the view behavior.
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    
# Variation ViewSets define the view behavior.
class VariationViewSet(viewsets.ModelViewSet):
    queryset = Variation.objects.all()
    serializer_class = VariationSerializer
    
# Variation ViewSets define the view behavior.
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    