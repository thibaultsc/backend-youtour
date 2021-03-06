# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beyt', '0017_auto_20160821_1631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour',
            old_name='arrival_location',
            new_name='arrivalLocation',
        ),
        migrations.RenameField(
            model_name='tour',
            old_name='arrival_time',
            new_name='arrivalTime',
        ),
        migrations.RenameField(
            model_name='tour',
            old_name='departure_location',
            new_name='departureLocation',
        ),
        migrations.RenameField(
            model_name='tour',
            old_name='departure_time',
            new_name='departureTime',
        ),
        migrations.AddField(
            model_name='tour',
            name='hotelPickup',
            field=models.BooleanField(default=False),
        ),
    ]
