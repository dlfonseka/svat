# Generated by Django 3.2 on 2021-04-16 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0002_auto_20210416_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_upload_timestamp',
            field=models.DateTimeField(blank=True),
        ),
    ]
