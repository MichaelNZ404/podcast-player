import pytest

from django.core.management import call_command
from podcast_player.models import Podcast, Genre
from podcast_player.serializers import PodcastSerializer, GenreSerializer
from datetime import date
from rest_framework.test import APIClient

class TestItunesView:
    @pytest.fixture
    def genre_fixture(self):
        return Genre.objects.create(
            itunes_id=1,
            url="http://foobar.com",
            name='Comedy'
        )

    @pytest.fixture
    def podcast_fixture(self, genre_fixture):
        p = Podcast.objects.create(
            itunes_id=1,
            url="http://foobar.com",
            artist_name='Bob',
            release_date=date.fromisoformat('2019-12-04'),
            name="A Podcast",
            artwork_url="http://foobar.com"
        )
        p.genres.add(genre_fixture)
        return p

    @pytest.fixture
    def expected_json_fixture(self):
        return {
            'name': 'A Podcast',
            'id': 1,
            'url': 'http://foobar.com',
            'kind': 'podcast',
            'artistName': 'Bob',
            'releaseDate': '2019-12-04',
            'artworkUrl100': 'http://foobar.com',
            'genres': [
                {
                    'genreId': 1,
                    'name': 'Comedy',
                    'url': 'http://foobar.com'
                }
            ]
        }

    @pytest.mark.django_db
    def test_itunes_get(self, podcast_fixture, expected_json_fixture):
        client = APIClient()
        response = client.get('/itunes/')
        assert dict(response.data[0]) == expected_json_fixture
        