from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.hello, name='helloname'),

    #/music/id
    url(r'^(?P<album_id>[0-9]*)/$', views.detail, name='detail' ) #Note that the / is required at the end.

]
