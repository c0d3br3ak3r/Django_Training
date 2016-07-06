from django.conf.urls import url
from django.contrib import admin
from . import views
app_name="booking"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^checkSlots/$', views.checkSlots, name='checkSlots'),
    url(r'^bookslots/$', views.bookslots, name='bookslots')
]
