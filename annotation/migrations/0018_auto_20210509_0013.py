# Generated by Django 3.2 on 2021-05-09 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0017_auto_20210508_2330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='segmentannotation',
            old_name='segment_annotation_timestamp',
            new_name='egment_annotation_endtime',
        ),
        migrations.RemoveField(
            model_name='pointannotation',
            name='point_annotation_text',
        ),
        migrations.RemoveField(
            model_name='segmentannotation',
            name='segment_annotation_tool',
        ),
        migrations.AddField(
            model_name='segmentannotation',
            name='segment_annotation_starttime',
            field=models.FloatField(null=True),
        ),
        migrations.DeleteModel(
            name='Annotation',
        ),
    ]
