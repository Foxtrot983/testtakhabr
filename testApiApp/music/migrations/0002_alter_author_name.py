# Generated by Django 4.2.4 on 2023-08-31 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
