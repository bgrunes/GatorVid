# Generated by Django 4.2.3 on 2023-08-02 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streaming_app', '0003_club_remove_video_video_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='course',
        ),
        migrations.RemoveField(
            model_name='video',
            name='description',
        ),
        migrations.RemoveField(
            model_name='video',
            name='title',
        ),
        migrations.RemoveField(
            model_name='video',
            name='uploaded_at',
        ),
    ]
