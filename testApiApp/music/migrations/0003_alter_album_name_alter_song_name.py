# Generated by Django 4.2.4 on 2023-08-31 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_alter_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
