import pytest

from django.core.management import call_command
from podcast_player.models import Podcast, Genre
from podcast_player.serializers import ItunesPodcastSerializer
from datetime import date

class TestItunesSerializer:
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
    def test_itunes_serialize(self, podcast_fixture, expected_json_fixture):
        serialized_podcast = ItunesPodcastSerializer(podcast_fixture).data
        assert serialized_podcast == expected_json_fixture

    @pytest.mark.django_db
    def test_itunes_deserialize(self, podcast_fixture, expected_json_fixture):
        deserialized_podcast = ItunesPodcastSerializer(data=expected_json_fixture)
        assert deserialized_podcast.is_valid()
        