from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from datetime import datetime
from django.conf import settings
import os

class Video(models.Model):
    video = models.FileField() #validators=[FileExtensionValidator(allowed_extensions=['mp4, mov'])]
    video_timestamp = models.FloatField(null=True)

    def __str__(self):
        return self.video.name

class Tools(models.Model):
    tools = models.TextField() #TODO: is this right
    video = models.ForeignKey('Video', on_delete=models.CASCADE, null=True, blank=True)

class Annotation(models.Model):
    annotation_video = models.ForeignKey('Video', on_delete=models.CASCADE, null=True, blank=True) #DISCUSS: delete annotation if video object deleted from database
    #annotation_tools = models.ForeignKey(Tools) #DISCUSS: is this behavior correct? if toolset deleted, then just replace toolset with null?   
    annotation_text = models.CharField(max_length=200, blank=True)
    annotation_detail = models.CharField(max_length=400, blank=True)
    #annotation_start_time = models.DateTimeField(default = datetime.now()) #make mandatory
    #annotation_duration = models.DurationField(blank=True) #make optional
    annotation_timestamp = models.FloatField(null=True)
    def __str__(self):
        return self.annotation_text

