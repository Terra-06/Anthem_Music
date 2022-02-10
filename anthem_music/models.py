from django.db import models
from django.conf import settings

# Create your models here.


class User(models.Model):
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='users')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Music(models.Model):
    artist_name = models.CharField(max_length=250)
    album_name = models.CharField(max_length=250)
    album_image = models.ImageField(
        upload_to='music', height_field='100', width_field='100', max_length=100)
    track_name = models.CharField(max_length=250)
    genre = models.TextField()

    def __str__(self):
        return self.name


class Playlist(models.Model):
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='playlists')
    user_name = models.CharField(max_length=250)
    artist_name = models.CharField(max_length=200)
    album_name = models.CharField(max_length=200)
    track_name = models.CharField(max_length=250)
    track_file = models.FileField(upload_to='playlist', max_length=200)
    album_image = models.ImageField(
        upload_to='playlist', height_field='100', width_field='100', max_length=100)

    def __str__(self):
        return self.name
