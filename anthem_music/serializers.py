from rest_framework import serializers
from .models import User, Music, Playlist


class UserSerializer(serializers.HyperlinkedModelSerializer):
    users = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name',
                  'user_name', 'email', 'password')


class MusicSerializer(serializers.HyperlinkedModelSerializer):
    songs = serializers.HyperlinkedRelatedField(
        view_name='song_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Music
        fields = ('artist_name', 'album_name',
                  'album_image', 'track_name', 'genre',)


class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    playlists = serializers.HyperlinkedRelatedField(
        view_name='music_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Playlist
        fields = ('id', 'user_name', 'artist_name', 'album_name',
                  'track_name', 'track_file', 'album_image')
