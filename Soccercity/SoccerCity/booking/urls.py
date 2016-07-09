from django.conf.urls import url
from django.contrib import admin
from . import views
app_name="booking"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^renderslots/$', views.renderSlots, name='renderSlots'),
    url(r'^bookslots/$', views.bookslots, name='bookslots'),
    url(r'^confirmation/$', views.confirmBooking, name='confirmBooking')
]
