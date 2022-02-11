
from django import forms
from .models import Playlist


class PlaylistForm(forms.ModelForm):

    class Meta:
        model = Playlist
        fields = ('artist_name', 'album_name',
                  'track_name', 'track_file', 'album_image')
