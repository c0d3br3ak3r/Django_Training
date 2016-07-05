from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Album,Song
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

    return render(request, "music/detail.html", { 'curr_album' : curr_album })


def makeFav(request, album_id):
    curr_album = get_object_or_404(Album, pk=album_id)
    try :
        selected_song = curr_album.song_set.get(pk=request.POST['song'])
    except (KeyError , Song.DoesNotExist):
        return render(request, 'music/detail.html', { 'curr_album' : curr_album, 'error_message': 'You did not select a valid song' })
    else :
        selected_song.isFavorite = True
        selected_song.save()
        return render(request, 'music/detail.html', { 'curr_album' : curr_album})
