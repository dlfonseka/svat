# Generated by Django 3.2 on 2021-05-03 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0008_auto_20210503_0420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_upload_timestamp',
        ),
    ]
