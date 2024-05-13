from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from djangoproj.views import send_sse_event,update_product_event
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    accept=models.BooleanField(default=False)
    user=models.IntegerField(default=None, blank=True, null=True)  

    def __str__(self):
        return self.name


@receiver(post_save, sender=Product)
def product_created(sender, created,instance, **kwargs):
    if created:
        channel_layer=get_channel_layer()
        print(instance.id)  
        ids=[3,4,5]
        data= {"id":instance.id,"type":ids}  
        async_to_sync(channel_layer.group_send)(
        'test_consumer_group',{
            'type' : 'send_data',
             'value': json.dumps(data)
        }
        )
        print("Singal called")
    # send_sse_event("created",instance.id)      




