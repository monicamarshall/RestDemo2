import time
from stomp import Connection
from django.test import TestCase

class TestMQ(TestCase):
    queue_messageReceived = []
    topic_messageReceived = []
    
    def setUp(self):
        pass 

    def tearDown(self):
        pass
    
    def connect_and_subscribe(self, conn):
        conn.connect('admin', 'admin', wait=True)
        conn.subscribe(destination='/queue/restdemo_queue', id=1, ack='auto')
        
    def test_subscribe_send_Queue(self):
        
        class MyListener():
            
            def __init__(self):
                print("MyListener __init__")
                   
            def on_error(self, message):
                print('received an error "%s"' % message)
        
            def on_message(self, message):
                print('received a message on queue"%s"' % message)
                TestMQ.queue_messageReceived.append(message)
                for x in range(2):
                    print(x)
                    time.sleep(1)
        
            def on_disconnected(self):
                print('disconnected')
                #connect_and_subscribe(self.conn)  
 
        print("test_subscribe_send_Queue()")      
        hosts = [('127.0.0.1', 61613)]
        conn1 = Connection(host_and_ports=hosts)
        conn2 = Connection(host_and_ports=hosts)
        queue_listener1 = MyListener
        queue_listener2 = MyListener
        conn1.set_listener('', queue_listener1)
        conn2.set_listener('', queue_listener2)
        conn1.connect('admin', 'admin', wait=True) 
        conn2.connect('admin', 'admin', wait=True)       
        conn1.subscribe(destination='/queue/restdemo_queue', id=1, ack='auto')    
        conn2.subscribe(destination='/queue/restdemo_queue', id=1, ack='auto')     
        conn1.send(body='This is a message sent to restdemo_queue in test case', destination='/queue/restdemo_queue')
            
        time.sleep(4)
        conn1.disconnect()
        conn2.disconnect()
        #for i in range( len(TestMQ.queue_messageReceived)):
            #print("TestMQ.messageReceived = " + TestMQ.queue_messageReceived[i])
        self.assertEqual(str(TestMQ.queue_messageReceived[0]), 'This is a message sent to restdemo_queue in test case')
        self.assertEqual(len(TestMQ.queue_messageReceived), 1)        
        
    def test_subscribe_send_Topic(self):
        
        class MyListener():
            
            def __init__(self):
                #hosts = [('127.0.0.1', 61613)]
                #conn = Connection(host_and_ports=hosts)
                #self.conn = conn
                print("MyListener __init__")
                   
            def on_error(self, message):
                print('received an error "%s"' % message)
        
            def on_message(self, message):
                print('received a message on topic "%s"' % message)
                TestMQ.topic_messageReceived.append(message)
                for x in range(2):
                    print(x)
                    time.sleep(1)
                    
        
            def on_disconnected(self):
                print('disconnected')
                #connect_and_subscribe(self.conn)  
 
        print("test_subscribe_send_Topic()")      
        hosts = [('127.0.0.1', 61613)]
        conn1 = Connection(host_and_ports=hosts)
        conn2 = Connection(host_and_ports=hosts)
        topic_listener1 = MyListener
        topic_listener2 = MyListener
        conn1.set_listener('', topic_listener1)
        conn2.set_listener('', topic_listener2)
        conn1.connect('admin', 'admin', wait=True)
        conn2.connect('admin', 'admin', wait=True)        
        conn1.subscribe(destination='/topic/restdemo_topic', id=1, ack='auto')   
        conn2.subscribe(destination='/topic/restdemo_topic', id=1, ack='auto')     
        conn1.send(body='This is a message sent to restdemo_topic from test case', destination='/topic/restdemo_topic')
            
        time.sleep(4)
        conn1.disconnect()
        conn2.disconnect()
        #for i in range( len(TestMQ.topic_messageReceived)):
            #print("TestMQ.messageReceived = " + TestMQ.topic_messageReceived[i])        
        self.assertEqual(len(TestMQ.topic_messageReceived), 2)

