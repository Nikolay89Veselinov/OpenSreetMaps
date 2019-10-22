from django.db import models

from osm_field.fields import LatitudeField, LongitudeField, OSMField


class OpenStreetMaps(models.Model):
    location = OSMField(lat_field='latitude', lon_field='longitude')
    latitude = LatitudeField()
    longitude = LongitudeField()
