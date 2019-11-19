import pusher
from django.shortcuts import render
# Create your views here.


pusher_client = pusher.Pusher(
    app_id='902827',
    key='c2b186d3fa112a5a5061',
    secret='5aa98840fee3a5b1c93c',
    cluster='ap2',
    ssl=False
)


def index(request):
    pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})
    return render(request, "myapp/index.html")
