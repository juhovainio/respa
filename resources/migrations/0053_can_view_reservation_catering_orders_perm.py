# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-15 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0052_add_can_access_reservation_comments_perm'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unit',
            options={'ordering': ('name',), 'permissions': (('can_approve_reservation', 'Can approve reservation'), ('can_view_reservation_access_code', 'Can view reservation access code'), ('can_view_reservation_extra_fields', 'Can view reservation extra fields'), ('can_access_reservation_comments', 'Can access reservation comments'), ('can_view_reservation_catering_orders', 'Can view reservation catering orders')), 'verbose_name': 'unit', 'verbose_name_plural': 'units'},
        ),
    ]
