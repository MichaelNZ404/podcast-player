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
    podcasts = PodcastSerializer(many=True, read_only=True, source='podcast_set')
    class Meta:
        model = Podcast
        fields = ['name', 'itunes_id', 'url', 'podcasts']

class ItunesGenreSerializer(serializers.HyperlinkedModelSerializer):
    ''' This serializer mimics the format of the itunes top 100 json '''
    genreId = serializers.IntegerField(source='itunes_id')
    class Meta:
        model = Genre
        fields = ['genreId', 'name', 'url']

class ItunesPodcastSerializer(serializers.HyperlinkedModelSerializer):
    ''' This serializer mimics the format of the itunes top 100 json '''
    artistName = serializers.CharField(source='artist_name')
    id = serializers.IntegerField(source='itunes_id')
    releaseDate = serializers.DateField(source='release_date')
    kind = serializers.SerializerMethodField('get_kind')
    artworkUrl100 = serializers.URLField(source='artwork_url')
    genres = ItunesGenreSerializer(many=True, read_only=True)

    class Meta:
        model = Podcast
        fields = ['artistName', 'id', 'releaseDate', 'name', 'kind', 'artworkUrl100', 'genres', 'url']

    def get_kind(self, obj):
        return 'podcast'