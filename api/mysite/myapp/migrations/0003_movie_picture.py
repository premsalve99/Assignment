# Generated by Django 3.2 on 2021-06-21 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_movie_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='pictures'),
        ),
    ]
