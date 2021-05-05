from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from datetime import datetime
from django.conf import settings
import os
import csv
import json
from io import StringIO

class Video(models.Model):
    video = models.FileField() #validators=[FileExtensionValidator(allowed_extensions=['mp4, mov'])]
    video_timestamp = models.FloatField(null=True)

    def __str__(self):
        return self.video.name

class Tools(models.Model):
    tools = models.CharField(max_length=1000, null=True, blank=True) #TODO: is this right
    tools_video = models.ForeignKey('Video', on_delete=models.CASCADE, null=True, blank=True) #TODO: review this to see if correct delete method
    tools_file = models.FileField(upload_to='tools', null=True)

    def set_tools(self, t):
        self.tools = json.dumps(t)

    def get_tools(self):
        return json.loads(self.tools)

    def save(self, *args, **kwargs):
        read_tools_file = self.tools_file.read().decode('utf-8')
        tools = read_tools_file.rstrip('\n') .split(',')
        self.set_tools(tools)
        super(Tools, self).save(*args, **kwargs) #Call the "real" save() method.

class Annotation(models.Model):
    annotation_video = models.ForeignKey('Video', on_delete=models.CASCADE, null=True, blank=True) #TODO: discuss delete method
    annotation_tool = models.CharField(max_length=200, blank=True) #TODO: is this behavior correct? if toolset deleted, then just replace toolset with null?   
    annotation_text = models.CharField(max_length=200, blank=True)
    annotation_detail = models.CharField(max_length=400, blank=True)
    #annotation_start_time = models.DateTimeField(default = datetime.now()) #make mandatory
    #annotation_duration = models.DurationField(blank=True) #make optional
    annotation_timestamp = models.FloatField(null=True)
    def __str__(self):
        return self.annotation_text

