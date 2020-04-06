from stomp import *

from mq.models import MQMessage
from mq.models import MQChannel
import time


class SendReceiveAPI:
    read_messages_global = []
    def __init__(self, host='127.0.0.1', port=61613, user='admin', password='admin'):
        # localhost is only for demo purposes, to make the app run when you are not connected
        # in a real application the euro dollar rate will be given by a distant API
        # to run the demo, copy the euro_dollar_rate.json file in your web folder
        self.host, self.port, self.user, self.password = host, port, user, password
    
    def subscribe_mqchannel(self, mqchannel):
        
        class MyListener():
            
            def __init__(self):                
                print("MyListener __init__")
                   
            def on_error(self, message):
                print('received an error "%s"' % message)
        
            def on_message(self, headers, message):
                print('MyListener:\nreceived a message "{}"\n'.format(message))                         
                SendReceiveAPI.read_messages_global.append(message) 
                print('In on_message() read_messages_global = ' + str(read_messages_global))
                print('In on_message() size of read_messages_global = ' + str(len(SendReceiveAPI.read_messages_global)))
            def on_disconnected(self):
                print('disconnected')
                #connect_and_subscribe(self.conn)                 
        
        print("subscribe_mqchannel() = mqchannel_name = " + str(mqchannel.mqchannel_name)) 
        hosts = [('127.0.0.1', 61613)]
        conn = Connection(host_and_ports=hosts)
        conn.set_listener('my_listener', MyListener())
        conn.connect('admin', 'admin', wait=True)
        conn.subscribe(destination=mqchannel.mqchannel_name, id=1, ack='auto')
        time.sleep(4)
        conn.disconnect()     
        for message in SendReceiveAPI.read_messages_global:
            print('message = ' + message)
            mqmessage = MQMessage.objects.create(mqchannel_id = mqchannel, message_text = message)
            mqmessage.save()
            SendReceiveAPI.read_messages_global = []
        return mqchannel; 
         
    def send_mqchannel(self, mqchannel, message):
        print("send_mqchannel() = mqchannel_name = " + str(mqchannel.mqchannel_name)) 
        hosts = [('127.0.0.1', 61613)]
        conn = Connection(host_and_ports=hosts)
        conn.connect('admin', 'admin', wait=True)
        print("about to send a message " + message)
        conn.send(body=message, destination=mqchannel.mqchannel_name)
        print("Message sent ") 
        conn.disconnect()  
   

