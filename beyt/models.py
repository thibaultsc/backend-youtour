from __future__ import unicode_literals

from django.db import models
from django_extensions.db.models import (
TitleSlugDescriptionModel, TimeStampedModel)


class Tour (TitleSlugDescriptionModel, TimeStampedModel):
  departure = models.CharField(max_length=200)
# Create your models here.
