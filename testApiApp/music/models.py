from django.db import models

    

class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name

class Album(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='albums')
    name = models.CharField(max_length=255, unique=True)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.author.name} | {self.name} | {self.date}"

class Song(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='song')
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return f"{self.author.name} - {self.name}"
    

class Album_To_Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='song')
    number = models.IntegerField()
    
    class Meta:
        ordering = ['number']

    def __str__(self):
        return f'{self.song.name} ({self.album.name})'
