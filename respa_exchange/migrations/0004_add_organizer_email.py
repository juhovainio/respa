# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('respa_exchange', '0003_related_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchangereservation',
            name='organizer_email',
            field=models.EmailField(blank=True, db_index=True, editable=False, max_length=250),
        ),
    ]