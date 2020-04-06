from django.urls import path
from . import views

app_name = 'mq'

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /mq/5/
    path('<int:id>/', views.detail, name='detail'),
    # ex: /mq/5/send
    path('<int:id>/send/', views.send, name='send'),
]

