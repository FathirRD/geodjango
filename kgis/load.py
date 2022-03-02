from pathlib                    import Path
from django.contrib.gis.utils   import LayerMapping
from .models                    import Area

area_mapping = {
    'kdppum': 'KDPPUM',
    'namobj': 'NAMOBJ',
    'remark': 'REMARK',
    'kdpbps': 'KDPBPS',
    'fcode': 'FCODE',
    'luaswh': 'LUASWH',
    'uupp': 'UUPP',
    'srs_id': 'SRS_ID',
    'lcode': 'LCODE',
    'metadata': 'METADATA',
    'kdebps': 'KDEBPS',
    'kdepum': 'KDEPUM',
    'kdcbps': 'KDCBPS',
    'kdcpum': 'KDCPUM',
    'kdbbps': 'KDBBPS',
    'kdbpum': 'KDBPUM',
    'wadmkd': 'WADMKD',
    'wiadkd': 'WIADKD',
    'wadmkc': 'WADMKC',
    'wiadkc': 'WIADKC',
    'wadmkk': 'WADMKK',
    'wiadkk': 'WIADKK',
    'wadmpr': 'WADMPR',
    'wiadpr': 'WIADPR',
    'tipadm': 'TIPADM',
    'shape_leng': 'SHAPE_Leng',
    'shape_area': 'SHAPE_Area',
    'geom': 'MULTIPOLYGON25D',
}

area_shp = Path(__file__).resolve().parent / 'data' / 'ADMINISTRASIKABUPATEN_AR_50K.shp'

def run(verbose=True):
    lm = LayerMapping(Area, area_shp, area_mapping, transform=True)
    lm.save(strict=True, verbose=verbose)