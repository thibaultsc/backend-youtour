from __future__ import unicode_literals

from django.db import models
from django_extensions.db.models import (
TitleSlugDescriptionModel, TimeStampedModel, TitleDescriptionModel)


#The model Tour represent a full packaged offer from an agency
class Tour (TitleSlugDescriptionModel, TimeStampedModel):
  def __unicode__(self):
    return self.departure_city + ' : ' + self.title
  departure_city = models.CharField(max_length=200)

#The model Activity represent a component of a Tour
class Activity (TitleSlugDescriptionModel, TimeStampedModel):
  def __unicode__(self):
    return  self.title

#The model Variation represent different option the traveler can 
#choose in an activity (different hotels for ex)
class Variation (TitleSlugDescriptionModel, TimeStampedModel):
  price = models.DecimalField(max_digits=20, decimal_places=2, null=True)
  activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
  def __unicode__(self):
    return  self.title

#The model TourActivity is the intermediate model to create a 
#Many to many relationship btw Tour and Activity
class TourActivity(TimeStampedModel):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    order = models.IntegerField()
    description = models.CharField(max_length=200, null=True)
    def __unicode__(self):
      return  self.tour.title + ' - ' + self.activity.title