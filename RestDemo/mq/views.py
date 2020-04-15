from django.shortcuts import get_object_or_404, render
from .models import MQChannel

from mq_events.send_receive import SendReceiveAPI
from django.http import HttpResponseRedirect
from django.urls import reverse

#def mqchannels(request):
    #return HttpResponse("You're at the mqchannels index. You can access the following MQ Channels: ")
# Create your views here.

def index(request):
    mqchannel_list = MQChannel.objects.order_by('created')
    context = {'mqchannel_list': mqchannel_list}
    return render(request, 'mq/index.html', context)

def detail(request, id):
    mqchannel = get_object_or_404(MQChannel, pk=id)
    mq_channel = SendReceiveAPI().subscribe_mqchannel(mqchannel)    
    return render(request, 'mq/detail.html', {'mqchannel': mq_channel})

def send(request, id):
    input_message = request.POST.get('message', 'fake message input text')
    
    print("input message = " + input_message)
    print("channel_id = " + str(id))
    mqchannel = get_object_or_404(MQChannel, pk=id)
    SendReceiveAPI().send_mqchannel(mqchannel, input_message)
    #mqchannel_list = MQChannel.objects.order_by('created')
    #context = {'mqchannel_list': mqchannel_list}
    return HttpResponseRedirect(reverse('mq:index')) 