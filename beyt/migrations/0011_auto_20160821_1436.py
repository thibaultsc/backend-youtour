# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beyt', '0010_touractivity_variation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='touractivity',
            options={'get_latest_by': 'modified', 'ordering': ('-modified', '-created')},
        ),
        migrations.RemoveField(
            model_name='touractivity',
            name='invite_reason',
        ),
        migrations.RemoveField(
            model_name='touractivity',
            name='title',
        ),
        migrations.AlterField(
            model_name='touractivity',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
