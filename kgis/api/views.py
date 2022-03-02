from django.shortcuts   import render

# from rest_framework     import generics, viewsets, permissions

# from kgis.models        import Perangkat, DataSaved
# from .serializers       import DataSavedSerailzer

# class DataMonitorAPIViews(
#         generics.ListCreateAPIView,
#         viewsets.GenericViewSet
#     ):

#     permission_classes          = [permissions.AllowAny]
#     serializer_class            = DataSavedSerailzer

#     def get_queryset(self):
#         perangkat   = self.kwargs['nperangkat']
#         qs          = DataSaved.objects.filter(perangkat=perangkat)
#         return qs
    
#     def perform_create(self, serializer):
#         serializer.save(perangkat=self.request.perangkat)

def index(request):
    return render(request, 'status/index.html')

def room(request, room_name):
    return render(request, 'status/room.html', {
        'room_name': room_name
    })