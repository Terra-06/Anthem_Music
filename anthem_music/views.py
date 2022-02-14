from django.http import JsonResponse
from .models import Music, Playlist
from django.shortcuts import redirect
from .forms import ListForm

# Create your views here.


def playlist(request):
    playlist = Music.objects.all().values(
        'artist_name',
        'album_name',
        'album_image',
        'track_name',
        'genre')
    playlist = playlist(music)
    return JsonResponse(playlist, safe=False)


def playlist_detail(request, pk):
    playlist = Music.objects.get(id=pk)
    data = {
        'artist_name': playlist.artist_name, 'album_name': playlist.album_name, 'album_image': playlist.album_image, 'track_name': playlist.track_name, 'genre': playlist.genre, }
    return JsonResponse(data, safe=False)


def playlist_create(request, new_artist_name, new_album_name, new_album_image, new_track_name, new_genre):
    playlist = Music.objects.create(
        artist_name=playlist.artist_name, album_name=playlist.album_name, album_image=playlist.album_image, track_name=playlist.track_name, genre=playlist.genre)
    return redirect('playlist')


def playlist_delete(request, pk):
    Playlist.objects.get(id=pk).delete()
    return redirect('playlist')
