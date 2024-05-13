# Django-Channels

Django Channels is a third-party library for Django, which extends its abilities beyond handling HTTP requests to include handling WebSockets, background tasks, and other asynchronous protocols. WebSockets allow for full-duplex communication between the client (usually a web browser) and the server, enabling real-time interactions such as chat applications, notifications, and live updates.

Clone this repo:

``` git clone https://github.com/Prajapati-vijay/Django-Channels.git ```


## Install requirements.txt

``` 
pip install -r requirements.txt 
```

## Run make migrations and migrate command

```
python manage.py makemigrations

python manage.py migrate ```

Now run this server:

```
python manage.py runserver ```

You will see that the ASGI server will be running instead of the normal WSGI server.

Now connect to ws://127.0.0.1:8000/ws/test/  
