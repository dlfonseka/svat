# Generated by Django 3.2 on 2021-05-05 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0012_rename_video_tools_tools_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tools',
            name='tools',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
