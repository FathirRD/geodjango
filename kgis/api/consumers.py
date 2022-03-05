import json

from datetime import datetime

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db                import database_sync_to_async

from djangochannelsrestframework            import generics, mixins

from kgis.models    import DataSaved, Perangkat
from .serializers   import DataSavedSerializer, PerangkatSerializer


class PerangkatMonitorConsumer(AsyncWebsocketConsumer):
    
    daftar_perangkat    = Perangkat.objects.all()
    groups              = [perangkat.nperangkat for perangkat in daftar_perangkat]

    async def connect(self):
        perangkat       = self.scope["url_route"]["kwargs"]["perangkat"]
        self.monitor    = f'monitor_{perangkat}'

        if(perangkat not in self.groups):
            await self.close()

        await self.channel_layer.group_add(
            self.monitor,
            self.channel_name
        )

        await self.accept()

    '''
    # Process message from Client
    # TODO
    []
    '''
    async def receive(self, text_data):
        text_data_json  = json.loads(text_data)

        message         = text_data_json['message']
        data            = text_data_json['data']
        saved_data      = None

        try:
            timestamp = datetime.fromtimestamp(text_data_json['request_id'])
        except: 
            timestamp = None

        if("foto" in data):
            payload   = {
                'perangkat': data['p_id'],
                'suhu': data['suhu'],
                'muka_air': data['muka_air'],
                'kelembapan': data['kelembapan'],
                'tegangan': data['tegangan'],
                'foto': data['foto'],
                'timestamp2': timestamp,
                'latlong': {
                    'latitude': data['latitude'],
                    'longitude': data['longitude']
                }
            }
            
            saved_data = await self.save_data(data=payload)
            data.pop('foto')
        
        await self.channel_layer.group_send(
            self.monitor, {
                'type': 'log_msg',
                'message': message,
                'data': data,
                'saved': saved_data
            }
        )

    # Receive message from room group
    async def log_msg(self, event):
        message     = event['message']
        saved       = event['saved']
        data        = event['data']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'data': data,
        }))

        if(saved):
            await self.send(text_data=json.dumps({
                'message': "Saving data to database..",
                'data': saved
            }))

    @database_sync_to_async
    def save_data(self, data):
        serializer  = DataSavedSerializer(data=data)
        if(serializer.is_valid(raise_exception=True)):
            new_data = serializer.create(serializer.validated_data)
            return DataSavedSerializer(new_data).data
        return 'Fail to save'

class DataMonitorConsumer(
        generics.GenericAsyncAPIConsumer,
        mixins.ListModelMixin,
    ):

    serializer_class    = DataSavedSerializer
    queryset            = DataSaved.objects.all()

class PerangkatConsumer(
        generics.GenericAsyncAPIConsumer,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin
    ):

    serializers_class   = PerangkatSerializer
    queryset            = Perangkat.objects.all()