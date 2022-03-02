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
        await self.accept()

    '''
    # Process message from Client
    # TODO
    []
    '''
    async def receive(self, text_data):
        text_data_json  = json.loads(text_data)
        message         = text_data_json['data']
        perangkat       = text_data_json['perangkat']
        saved_data      = None

        try:
            timestamp = datetime.fromtimestamp(text_data_json['request_id'])
        except: 
            timestamp = ""

        if(message['foto']):
            data        = {
                'perangkat': message['p_id'],
                'suhu': message['suhu'],
                'muka_air': message['muka_air'],
                'kelembapan': message['kelembapan'],
                'tegangan': message['tegangan'],
                'foto': message['foto'],
                'timestamp2': timestamp,
                'latlong': {
                    'latitude': message['latitude'],
                    'longitude': message['longitude']
                }
            }
            
            saved_data = await self.save_data(data=data)

        message.pop('p_id')
        message.pop('foto')

        await self.channel_layer.group_send(
            perangkat, {
                'type': 'log_msg',
                'message': message,
                'perangkat': perangkat,
                'saved': saved_data if saved_data else None
            }
        )

    # Receive message from room group
    async def log_msg(self, event):
        message     = event['message']
        perangkat   = event['perangkat']
        saved       = event['saved']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'perangkat': perangkat
        }))

        if(saved):
            await self.send(text_data=json.dumps({
                'message': saved,
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
        mixins.CreateModelMixin
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