from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter


router = SimpleRouter()


router.register('main', views.MainViewSet, basename='main')
router.register('albumcreate', views.AlbumCreateViewSet, basename='album-create')
router.register('songcreate', views.SongCreateViewSet, basename='song-create')
router.register('authorcreate', views.AuthorCreateViewSet, basename='author-create')
router.register('connectdata', views.SongToAlbumCreateViewSet, basename='connection-create')


urlpatterns = [
 #   path('album-create', views.AlbumCreateViewSet.as_view())
    
] + router.urls