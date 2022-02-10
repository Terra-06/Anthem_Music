from django.contrib import admin
from .models import User, Music, Playlist

# Register your models here.
admin.site.register(User)
admin.site.register(Music)
admin.site.register(Playlist)
