# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 19:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beyt', '0006_remove_tourcomponent_component_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourcomponent',
            name='tour',
        ),
    ]