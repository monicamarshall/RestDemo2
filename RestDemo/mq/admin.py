from django.contrib import admin

from .models import MQChannel
from .models import MQMessage

admin.site.register(MQChannel)
admin.site.register(MQMessage)