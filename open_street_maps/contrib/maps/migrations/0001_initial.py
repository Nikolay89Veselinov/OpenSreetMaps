# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-10-22 09:37
from __future__ import unicode_literals

from django.db import migrations, models
import osm_field.fields
import osm_field.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OpenStreetMaps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', osm_field.fields.OSMField(lat_field='latitude', lon_field='longitude')),
                ('latitude', osm_field.fields.LatitudeField(validators=[osm_field.validators.validate_latitude])),
                ('longitude', osm_field.fields.LongitudeField(validators=[osm_field.validators.validate_longitude])),
            ],
        ),
    ]