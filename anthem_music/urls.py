from django.urls import path
from . import views

urlpatterns = [
    path('', views.music_list, name='music_list'),
    path('playlists/<int:pk>', views.playlist_detail, name='playlist_detail'),
    path('playlists/<int:pk>/delete',
         views.playlist_delete, name='playlist_delete'),
    path(
        'playlists/new/<str:new_artist_name><str:new_album_name><str:new_track_name><str:new_album_image><str:new_genre>',
        views.playlist_create, name='playlist_create')

]
