from rest_framework import serializers
from .models import Author, Album, Song, Album_To_Song

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response

@swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING),
        },
        required=['name'],
    ),
)

class SongSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Song
        fields = ['name', ]


class SongAlbumSerializer(serializers.ModelSerializer):
    song = SongSerializer(Song.objects.all())
    class Meta:
        model = Album_To_Song
        fields = ['number', 'song']


class AlbumSerializer(serializers.ModelSerializer):
    songs = SongAlbumSerializer(many=True)
    
    class Meta:
        model = Album
        fields = ['name', 'date', 'songs']


class AuthorSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True)
    
    class Meta:
        model = Author
        fields = ['name', 'albums']



class AuthorCreateSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        return Author.objects.create(**validated_data)
    
    class Meta:
        model = Author
        fields = ['name',]


class AlbumCreateSerializer(serializers.ModelSerializer):
    author = serializers.CharField()
    
    def create(self, validated_data):
        print(validated_data)
        author = Author.objects.filter(name=validated_data['author']).first()
        validated_data['author'] = author
        
        if validated_data['author'] == None:
            raise serializers.ValidationError
        
        return Album.objects.create(**validated_data)

    class Meta:
        model = Album
        fields = ['name', 'date', 'author']


class SongCreateSerializer(serializers.ModelSerializer):
    author = serializers.CharField() 
    
    def create(self, validated_data):
        #author = Author.objects.filter(name=dict(validated_data['author'])['name']).first()
        #validated_data['author'] = author

        validated_data['author'] = Author.objects.filter(name=validated_data['author']).first()
        if validated_data['author'] == None:
            raise serializers.ValidationError
        print(validated_data)
        return Song.objects.create(**validated_data)
    
    class Meta:
        model = Song
        fields = ['name', 'author']


class ConnectAlbumSongSerializer(serializers.ModelSerializer):
    song = serializers.CharField()
    album = serializers.CharField()
    
    def create(self, validated_data):        
        validated_data['album'] = Album.objects.filter(name=validated_data['album']).first()
        validated_data['song'] = Song.objects.filter(name=validated_data['song']).first()
        
        #if validated_data['author'] == None or validated_data['song'] == None:
        #    raise serializers.ValidationError
        
        return Album_To_Song.objects.create(**validated_data)
    
    class Meta:
        model = Album_To_Song
        fields = ['song', 'album']
        
        
"""
{
  "song": "TestCreateSong",
  "album": "TestCreateAlbum"
}

"""