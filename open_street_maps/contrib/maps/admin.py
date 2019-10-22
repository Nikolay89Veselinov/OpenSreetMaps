from django.contrib import admin

from .models import OpenStreetMaps


@admin.register(OpenStreetMaps)
class OpenStreetMapsAdmin(admin.ModelAdmin):
    list_display = ('location', 'latitude', 'longitude')
# Register your models here.


