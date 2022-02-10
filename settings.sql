-- settings.sql
CREATE DATABASE anthem_music;
CREATE USER anthem_music_user WITH PASSWORD 'anthem_music';
GRANT ALL PRIVILEGES ON DATABASE anthem_music TO anthem_music_user;