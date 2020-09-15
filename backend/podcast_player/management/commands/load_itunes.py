import json 

from django.core.management.base import BaseCommand
from podcast_player.models import Podcast, Genre


class Command(BaseCommand):
    help = 'Loads a json file with the format of a top 100 itunes podcast file'

    def add_arguments(self, parser):
        parser.add_argument('itunes_file')

    def handle(self, **options):
        with open(options['itunes_file']) as json_file:
            json_data = json.load(json_file)
            for itunes_podcast in json_data['feed']['results']:
                podcast_obj = Podcast.objects.create(
                    itunes_id = itunes_podcast['id'],
                    url = itunes_podcast['url'],
                    artist_name = itunes_podcast['artistName'] ,
                    release_date = itunes_podcast['releaseDate'],
                    name =  itunes_podcast['name'],
                    artwork_url = itunes_podcast['artworkUrl100']
                )
                for itunes_genre in itunes_podcast['genres']:
                    genre_obj = Genre.objects.get_or_create(
                        itunes_id=itunes_genre['genreId'],
                        url=itunes_genre['url'], 
                        name=itunes_genre['name']
                    )
                    podcast_obj.genres.add(genre_obj[0])
