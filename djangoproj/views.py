from django.http import HttpResponse,StreamingHttpResponse
import requests
import time
from django.core.cache import cache
from django.utils import timezone
import json
# from django_eventstream import send_event
# from django_eventstream.models import Message



def home(request):
    re=requests.get("https://www.storesofindia.com/store/api-v1/address/")
    return HttpResponse(re) 


def sse(request):
    # Check if the count exists in the cache

    # Set response headers for SSE
    response = StreamingHttpResponse(event_stream(), content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    cache.clear()   
    return response

# Function to send SSE events
def event_stream():
    while True:

        
        if cache.get('Data'):
            print("Inside created yield")
            d=json.dumps(cache.get('Data'))
            for i in range(0,5):

                yield 'data: {}\n\n'.format(d) 
            cache.delete('Data')
        

        continue  

        # Send event every 5 seconds # Send event every 5 seconds

def sse_update(request):
    # Check if the count exists in the cache

    # Set response headers for SSE
    response = StreamingHttpResponse(event_stream_update(), content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    cache.clear()
    return response

# Function to send SSE events
def event_stream_update():
    while True:
        # Increment the count for each event
        # Store the updated count in the cache
        # yield 'data: {}\n\n'.format('Server Time: {}, Hello, world!'.format(server_time))  
        if cache.get('Update'):
            print("Inside Update yield")
            yield 'data: {}\n\n'.format("Updated") 
            cache.clear()
            break       

        continue  



def send_sse_event(event_name, data):

    # send_event("my-event", "message", {"text": "Hey this is test"}, channel="test")  
    # # Convert data to JSON format 
    # print("data added successfully")
    cache.set('Data',data) 
   

def update_product_event():
    print("Data updated")
    cache.set('Update',True)