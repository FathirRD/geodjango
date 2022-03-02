from django.contrib.gis import forms
from .models            import Area, Perangkat, DataSaved


class KGISForm(forms.ModelForm):
   class Meta:
        model   = Area
        fields  = '__all__'

class PerangkatForm(forms.ModelForm):
   class Meta:
        model   = Perangkat
        fields  = '__all__'

class DataSavedForm(forms.ModelForm):
   class Meta:
        model   = DataSaved
        fields  = '__all__'