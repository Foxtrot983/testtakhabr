# Generated by Django 4.2.4 on 2023-08-31 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song', to='music.author')),
            ],
        ),
        migrations.CreateModel(
            name='Album_To_Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='music.album')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song', to='music.song')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.AddField(
            model_name='album',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='music.author'),
        ),
    ]