from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from podcast_player.serializers import UserSerializer, GroupSerializer, PodcastSerializer, GenreSerializer, DeepPodcastSerializer, DeepGenreSerializer
from podcast_player.models import Podcast, Genre


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class DeepPodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = DeepPodcastSerializer

class DeepGenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = DeepGenreSerializer