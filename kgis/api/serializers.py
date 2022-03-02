from rest_framework     import serializers

from drf_extra_fields.fields        import Base64ImageField
from drf_extra_fields.geo_fields    import PointField

from kgis.models    import Perangkat, DataSaved

class PerangkatSerializer(serializers.ModelSerializer):

    class Meta:
        model   = Perangkat
        fields  = '__all__'

class DataSavedSerializer(serializers.ModelSerializer):

    foto        = Base64ImageField(required=True)
    latlong     = PointField(required=False)
    
    class Meta:
        model   = DataSaved
        fields  = '__all__'