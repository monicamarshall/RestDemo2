from django.db import models


class MQChannel(models.Model):
    MQCHANNEL_TYPE = (
       ('queue', ('Point to Point model')),
       ('topic', ('Pub Sub model'))
    )
    id = models.AutoField(primary_key=True)
    mqchannel_name = models.CharField(max_length=20)
    mqchannel_type = models.CharField(
        choices=MQCHANNEL_TYPE, 
        default='queue', 
        max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('created', )
        db_table = u'"restdemo\".\"mqchannel"'
    def __str__(self):
        return self.mqchannel_name
    

        
class MQMessage(models.Model):
    MESSAGE_TYPE = (
       ('text/plain', ('text/plain')),
       ('application/xml', ('application/xml')),
       ('application/json',('application/json')),
       #('text/html', _('text/html')),
       #('image/gif', _('image/gif')),
       #('image/jpeg', _('image/jpeg')),
    )
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    message_text = models.CharField(max_length=500)    
    message_type = models.CharField(
       max_length=100,
       choices=MESSAGE_TYPE,
       default='text/plain',
    )
    mqchannel_id = models.ForeignKey(MQChannel, on_delete=models.CASCADE)
    class Meta:
        ordering = ('created', )
        db_table = u'"restdemo\".\"mqmessage"'
    
    def __str__(self):
        return self.message_text
        
