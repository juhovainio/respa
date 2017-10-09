# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 15:55
from __future__ import unicode_literals

from django.db import migrations, models
import resources.models.unit


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0055_add_can_make_reservations_perm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='time_zone',
            field=models.CharField(default=resources.models.unit._get_default_timezone, max_length=50, verbose_name='Time zone'),
        ),
    ]