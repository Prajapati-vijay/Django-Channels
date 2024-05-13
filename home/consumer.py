from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json


class TestConsumer(WebsocketConsumer):
    
    def connect(self):
        # pass
        self.room_name = "test_consumer"
        self.room_group_name= "test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
           self.room_group_name,
            self.channel_name  
        )  
        self.accept()
        self.send(text_data=json.dumps({
            'status': 'connected to websocket'
        }))
  
    def receive(self,text_data):
        print(text_data)
        
     
    def disconnect(self,code):
          
          self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )
          print("Websocket disconnected")
 
    def send_data(self,event):
        print(event) 
        data=json.loads(event.get('value'))
        self.send(text_data=json.dumps({"payload":data}))        

