from django.shortcuts import render
from django.http import HttpResponse
from .models import Album

# Create your views here.
def hello(request):
    html = ''
    all_albums = Album.objects.all()
    for alb in all_albums:
        url = '/music/' + str(alb.id) + '/'
        html += '<a href="' + url + '">' + alb.album_title +'</a>'
    return HttpResponse(html)

def detail(request, album_id):
    return HttpResponse("<h1>The selected album is : " + album_id)
