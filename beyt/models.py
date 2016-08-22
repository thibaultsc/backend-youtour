from __future__ import unicode_literals

from django.db import models
from django_extensions.db.models import (
TitleSlugDescriptionModel, TimeStampedModel, TitleDescriptionModel)

TYPE_CHOICE = (
    ('1', 'Default'),
    ('2', 'Human'),
    ('3', 'Machine'),
)

#The model Location 
class Location(TimeStampedModel):
    streetAddress	= models.CharField(max_length=200, null=True)
    postalCode = models.CharField(max_length=200, null=True)
    addressLocality = models.CharField(max_length=200, null=True)
    addressRegion = models.CharField(max_length=200, null=True)
    addressCountry = models.CharField(max_length=200, null=True)
    telephone = models.CharField(max_length=20, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=15, null=True)
    defaultLanguage = models.CharField(max_length=2, default='en')
    def __unicode__(self):
      return  self.streetAddress + ' - ' + self.addressLocality

#The model TranslateLocation 
class TranslateLocation(TimeStampedModel):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='locales')
    language = models.CharField(max_length=2, default='en')
    type = models.CharField(max_length=2,choices=TYPE_CHOICE,default='1',)
    name = models.CharField(max_length=200, null=True)
    details = models.CharField(max_length=200, null=True)
    def __unicode__(self):
      return  self.streetAddress + ' - ' + self.addressLocality
    class Meta:
      verbose_name_plural = "translatelocations"


#The model Tour represent a full packaged offer from an agency
class Tour (TimeStampedModel):
  def __unicode__(self):
    return  self.locales.all().get(type='1').title
  departureLocation = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, related_name='departure_location')
  departureTime = models.TimeField(null=True)
  arrivalLocation = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, related_name='arrival_location')
  arrivalTime = models.TimeField(null=True)
  duration = models.DurationField(null=True)
  hotelPickupAccepted = models.BooleanField(default=False)
  price = models.DecimalField(max_digits=20, decimal_places=2, null=True)
  currency = models.CharField(max_length=3, null=True)
  sizeMin = models.IntegerField(null=True)
  sizeMax = models.IntegerField(null=True)
  def titleSlugDescription(self, lg):
    queryset = self.locales.filter(language=lg).order_by('type', '-modified')
    if queryset.count() > 0 :
      return queryset[0]
    else:
      return self.locales.filter(type='1').order_by('-modified')[0]
    return "error"

  
#The model Tour represent a full packaged offer from an agency
class TranslateTour (TitleSlugDescriptionModel, TimeStampedModel):
  def __unicode__(self):
    return  self.title
  tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='locales')
  language = models.CharField(max_length=2, default='en')
  type = models.CharField(max_length=2,choices=TYPE_CHOICE,default='1',)


#The model Activity represent a component of a Tour
class Activity (TitleSlugDescriptionModel, TimeStampedModel):
  def __unicode__(self):
    return  self.title
  class Meta:
    verbose_name_plural = "Activities"

#The model Variation represent different option the traveler can 
#choose in an activity (different hotels for ex)
class Variation (TitleSlugDescriptionModel, TimeStampedModel):
  price = models.DecimalField(max_digits=20, decimal_places=2, null=True)
  currency = models.CharField(max_length=3, null=True)
  activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
  def __unicode__(self):
    return  self.title

#The model TourActivity is the intermediate model to create a 
#Many to many relationship btw Tour and Activity
class TourActivity(TimeStampedModel):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='activities')
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='tours')
    order = models.IntegerField()
    description = models.CharField(max_length=200, null=True)
    def __unicode__(self):
      return  self.activity.title
    class Meta:
      verbose_name_plural = "Tour activities"


    
  
