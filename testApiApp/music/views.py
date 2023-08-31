from .models import Song, Album, Album_To_Song, Author
from .serializers import AlbumSerializer, AuthorSerializer, AlbumCreateSerializer, AuthorCreateSerializer, SongCreateSerializer, ConnectAlbumSongSerializer

from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class CreateMixin(GenericViewSet, mixins.CreateModelMixin):
    pass


class MainViewSet(ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer



class AlbumCreateViewSet(CreateMixin):
    queryset = Album.objects.all()
    serializer_class = AlbumCreateSerializer
    

class SongCreateViewSet(CreateMixin):
    queryset = Song.objects.all()
    serializer_class = SongCreateSerializer


class AuthorCreateViewSet(CreateMixin):
    queryset = Author.objects.all()
    serializer_class = AuthorCreateSerializer
    

class SongToAlbumCreateViewSet(CreateMixin):
    queryset = Album_To_Song.objects.all()
    serializer_class = ConnectAlbumSongSerializer
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        song = Song.objects.filter(name=serializer.validated_data['song']).first()
        album = Album.objects.filter(name=serializer.validated_data['album']).first()
        try:
            if song.author != album.author:
                print("Не совпадает")
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except AttributeError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        #print(f"{song}, {album}")
        query_by_albums = Album_To_Song.objects.filter(album = album).all()
        
        if query_by_albums.count() != 0:
            serializer.validated_data['number'] = query_by_albums.count() + 1
        else:
            serializer.validated_data['number'] = 1
            
        check = query_by_albums.filter(
            song=song,
            )
        #print(check)
        if len(check) != 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            #print(serializer.data)
            
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            print('Success')
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    