import time
from stomp import Connection, ConnectionListener, PrintingListener

class TestMQDestinations(object):
    
    def printIncrementsByOne(self, i):
        if(i<10):
            print(i)
            i += 1
            self.printIncrementsByOne(i)
            
    def getMessagesFromMQChannel(self, messageToPost):
        class MyListener(ConnectionListener):
            def __init__(self, conn):
                self.conn = conn
                
            def on_error(self, headers, message):
                print('received an error "%s"' % message)
        
            def on_message(self, headers, message):
                print('received a message "%s"' % message)
                for x in range(10):
                    print(x)
                    time.sleep(1)
                print('processed message')
        
            def on_disconnected(self):
                print('disconnected')
                connect_and_subscribe(self.conn)
                
        def connect_and_subscribe(conn):
            conn.connect('admin', 'admin', wait=True)
            conn.subscribe(destination='/queue/restdemo_queue', id=1, ack='auto')
        
        hosts = [('127.0.0.1', 61613)]
        conn = Connection(host_and_ports=hosts)
        conn.set_listener('', PrintingListener())
        #conn.set_listener('', MyListener(conn))
        conn.connect('admin', 'admin', wait=True)        
        conn.subscribe(destination='/queue/restdemo_queue', id=1, ack='auto')        
        conn.send(body=messageToPost, destination='/queue/restdemo_queue')
            
        time.sleep(2)
        conn.disconnect()
            
if __name__ == '__main__':
    TestMQDestinations().printIncrementsByOne(0)
    TestMQDestinations().getMessagesFromMQChannel("This is the message posted to the restdemo_queue")