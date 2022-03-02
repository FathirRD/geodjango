# from django.contrib import admin
from django.contrib.gis import admin

from .forms             import WorldBorderForm
from .models            import WorldBorder


class WorldBorderAdm(admin.OSMGeoAdmin):
    form            = WorldBorderForm
    list_display    = [
        'name',
        'fips'
    ]

admin.site.register(WorldBorder, WorldBorderAdm)     # Use OSM to provide map (use .GeoModelAdmin for default django gis map)