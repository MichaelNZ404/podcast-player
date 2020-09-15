from django.db import models

class Genre(models.Model):
    itunes_id = models.IntegerField()
    url = models.URLField(max_length=500)
    name = models.CharField(max_length=120)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Podcast(models.Model):
    itunes_id = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    url = models.URLField(max_length=500)
    artist_name = models.CharField(max_length=120)
    release_date = models.DateField()
    name = models.CharField(max_length=120)
    artwork_url = models.URLField(max_length=500)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
