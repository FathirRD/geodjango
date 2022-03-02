from django.contrib.gis         import admin
from django.urls                import path, include
from django.conf                import settings
from django.conf.urls.static    import static

urlpatterns = [
    path('api/', include('kgis.api.urls', namespace='status-api')),
    
    path('admin/',      admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL,   document_root=settings.MEDIA_ROOT)