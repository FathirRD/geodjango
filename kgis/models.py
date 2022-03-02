from datetime               import datetime
from tabnanny import verbose

from django.contrib.gis.db  import models

class Perangkat(models.Model):
    nperangkat  = models.CharField(verbose_name="Nama Perangkat",max_length=50)
    added_at    = models.DateTimeField(auto_now_add=True,)

    class Meta:
        verbose_name        = 'Perangkat'
        verbose_name_plural = 'Daftar Perangkat'

    def __str__(self) -> str:
        return self.nperangkat

def fotodir(instance, filename):
    return f'{datetime.date(datetime.now())}/{instance.perangkat}/{filename}'

class DataSaved(models.Model):
    perangkat   = models.ForeignKey(Perangkat, on_delete=models.CASCADE)
    suhu        = models.FloatField(verbose_name="Suhu Ruangan")
    muka_air    = models.FloatField(verbose_name="Ketinggian Muka Air")
    kelembapan  = models.FloatField(verbose_name="Kelembapan Udara")
    tegangan    = models.FloatField(verbose_name="Tegangan Baterai Perangkat")
    foto        = models.FileField(verbose_name="Foto Kamera Perangkat", upload_to=fotodir)
    timestamp   = models.DateTimeField(verbose_name="Timestamp Server", auto_now_add=True)
    timestamp2  = models.DateTimeField(verbose_name="Timestamp Perangkat", blank=True, null=True)
    latlong     = models.PointField(verbose_name="Lokasi Perangkat",srid=4326, blank=True, null=True)

    class Meta:
        verbose_name        = 'Data Saved'
        verbose_name_plural = 'Data Saved Logs'

    def __str__(self) -> str:
        return str(self.timestamp)
    
class Area(models.Model):
    kdppum      = models.CharField(max_length=2)
    namobj      = models.CharField(max_length=50)
    remark      = models.CharField(max_length=250, null=True)
    kdpbps      = models.CharField(max_length=2, null=True)
    fcode       = models.CharField(max_length=50, null=True)
    luaswh      = models.FloatField()
    uupp        = models.CharField(max_length=50, null=True)
    srs_id      = models.CharField(max_length=50, null=True)
    lcode       = models.CharField(max_length=50)
    metadata    = models.CharField(max_length=50, null=True)
    kdebps      = models.CharField(max_length=50, null=True)
    kdepum      = models.CharField(max_length=50, null=True)
    kdcbps      = models.CharField(max_length=50, null=True)
    kdcpum      = models.CharField(max_length=50, null=True)
    kdbbps      = models.CharField(max_length=50, null=True)
    kdbpum      = models.CharField(max_length=50, null=True)
    wadmkd      = models.CharField(max_length=50, null=True)
    wiadkd      = models.CharField(max_length=50, null=True)
    wadmkc      = models.CharField(max_length=50, null=True)
    wiadkc      = models.CharField(max_length=50, null=True)
    wadmkk      = models.CharField(max_length=50, null=True)
    wiadkk      = models.CharField(max_length=50, null=True)
    wadmpr      = models.CharField(max_length=50, null=True)
    wiadpr      = models.CharField(max_length=50, null=True)
    tipadm      = models.BigIntegerField()
    shape_leng  = models.FloatField()
    shape_area  = models.FloatField()
    geom        = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.namobj

