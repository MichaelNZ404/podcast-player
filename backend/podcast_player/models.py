from django.db import models

class Genre(models.Model):
    itunes_id = models.CharField(max_length=30)
    url = models.URLField()
    name = models.CharField(max_length=60)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Podcast(models.Model):
    itunes_id = models.CharField(max_length=30),
    genre = models.ManyToManyField(Genre)
    url = models.URLField()
    artist_name = models.CharField(max_length=30)
    release_date = models.DateField()
    name = models.CharField(max_length=60)
    artwork_url = models.URLField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
