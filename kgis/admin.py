from django.contrib.gis import admin

from .forms             import KGISForm, PerangkatForm, DataSavedForm
from .models            import Area, Perangkat, DataSaved


class KGISAdm(admin.OSMGeoAdmin):
    form            = KGISForm
    list_display    = [
        '__str__',
        'wadmkk',
        'wadmpr'
    ]

class PerangkatAdm(admin.OSMGeoAdmin):
    form            = PerangkatForm
    list_display    = [
        'id',
        'nperangkat',
        'added_at'
    ]

class DataSavedAdm(admin.OSMGeoAdmin):
    form            = PerangkatForm
    list_display    = [
        'id',
        'perangkat',
    ]

admin.site.register(Area, KGISAdm) 
admin.site.register(Perangkat, PerangkatAdm) 
admin.site.register(DataSaved, DataSavedAdm) 