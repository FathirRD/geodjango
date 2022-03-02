from django.contrib.gis import forms
from .models            import WorldBorder


class WorldBorderForm(forms.ModelForm):
   class Meta:
        model   = WorldBorder
        fields  = '__all__'