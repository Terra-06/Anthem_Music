# Generated by Django 4.0.2 on 2022-02-09 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=250)),
                ('album_name', models.CharField(max_length=250)),
                ('album_image', models.ImageField(height_field='100', upload_to='music', width_field='100')),
                ('track_name', models.CharField(max_length=250)),
                ('genre', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('user_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=250)),
                ('password', models.CharField(max_length=255)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=250)),
                ('artist_name', models.CharField(max_length=200)),
                ('album_name', models.CharField(max_length=200)),
                ('track_name', models.CharField(max_length=250)),
                ('track_file', models.FileField(max_length=200, upload_to='playlist')),
                ('album_image', models.ImageField(height_field='100', upload_to='playlist', width_field='100')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]