from django.contrib.auth.models import User, Group
from rest_framework import serializers
from podcast_player.models import Podcast, Genre


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PodcastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Podcast
        fields = ['name', 'itunes_id', 'url', 'artist_name', 'release_date', 'artwork_url']


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'itunes_id', 'url']

class DeepPodcastSerializer(serializers.HyperlinkedModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = Podcast
        fields = ['name', 'itunes_id', 'genres', 'url', 'artist_name', 'release_date', 'artwork_url']

class DeepGenreSerializer(serializers.HyperlinkedModelSerializer):
    podcast_set = PodcastSerializer(many=True, read_only=True)
    class Meta:
        model = Podcast
        fields = ['name', 'itunes_id', 'url', 'podcast_set']