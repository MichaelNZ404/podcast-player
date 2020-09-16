from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from podcast_player import serializers
from podcast_player.models import Podcast, Genre


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = serializers.PodcastSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = serializers.GenreSerializer

class DeepPodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = serializers.DeepPodcastSerializer

class DeepGenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = serializers.DeepGenreSerializer

class ItunesViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = serializers.ItunesPodcastSerializer