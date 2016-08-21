# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beyt', '0004_auto_20160820_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourcomponent',
            name='component_type',
            field=models.CharField(choices=[('ACT', 'Activity'), ('TRA', 'Transport'), ('HOU', 'Hotel')], default='ACTIVITY', max_length=10),
        ),
    ]
