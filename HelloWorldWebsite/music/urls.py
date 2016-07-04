from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.hello, name='helloname'),
]
