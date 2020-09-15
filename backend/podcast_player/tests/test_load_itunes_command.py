import pytest

from django.core.management import call_command
from podcast_player.models import Podcast, Genre

@pytest.mark.django_db
def test_itunes_output():
    assert Podcast.objects.count() == 0
    call_command('load_itunes', 'us-top-100-podcasts.json')
    assert Podcast.objects.count() == 100