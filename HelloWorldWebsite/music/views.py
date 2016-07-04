from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Album
from django.template import loader

# Create your views here.
def hello(request):
    all_albums = Album.objects.all()
    # mytemplate = loader.get_template('music/index.html')
    # context = {
    #     'all_albs' : all_albums
    # }
    # return HttpResponse(mytemplate.render(context,request))

    #Instead of above , we can use render() function which is lot cleaner
    context = { 'all_albs' : all_albums }
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    try:
        curr_album = Album.objects.get(pk=album_id)
    except:
        raise Http404("Oops! Not Found ! Better luck next time.") #returning 404 when no such album exists
        
    return render(request, "music/detail.html", { 'album_title' : curr_album.album_title })
