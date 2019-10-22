from django import forms

from .models import OpenStreetMaps


class OpenStreetMapsForm(forms.ModelForm):

    class Meta:
        fields = ('location', 'latitude', 'longitude', )
        model = OpenStreetMaps

