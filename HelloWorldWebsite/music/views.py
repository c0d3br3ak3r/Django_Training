from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
from django.template import loader

# Create your views here.
def hello(request):
    all_albums = Album.objects.all()
    mytemplate = loader.get_template('music/index.html')
    context = {
        'all_albs' : all_albums
    }

    return HttpResponse(mytemplate.render(context,request))

def detail(request, album_id):
    return HttpResponse("<h1>The selected album is : " + album_id)
