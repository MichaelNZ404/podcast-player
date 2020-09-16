from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from podcast_player import views

router = routers.DefaultRouter()

router.register(r'podcasts', views.PodcastViewSet)
router.register(r'genres', views.GenreViewSet)
router.register(r'deep_podcasts', views.DeepPodcastViewSet)
router.register(r'deep_genres', views.DeepGenreViewSet)
router.register(r'itunes', views.ItunesViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
