# Generated by Django 3.2 on 2021-04-16 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annotation',
            name='annotation_duration',
        ),
        migrations.RemoveField(
            model_name='annotation',
            name='annotation_tools',
        ),
        migrations.RemoveField(
            model_name='annotation',
            name='annotation_video',
        ),
        migrations.AlterField(
            model_name='annotation',
            name='annotation_detail',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='annotation_start_time',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='annotation_text',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]