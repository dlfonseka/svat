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

    def set_timestamp(self, time):
        self.video_timestamp = time
        self.save()

class Tools(models.Model):
    tools = models.CharField(max_length=1000, null=True, blank=True) #TODO: is this right
    tools_video = models.ForeignKey('Video', on_delete=models.CASCADE, null=True, blank=True) #TODO: review this to see if correct delete method
    tools_file = models.FileField(upload_to='tools', null=True)
    tools_video_indicator = models.CharField(max_length=200, null=True, blank=True)

    def set_tools(self, t):
        self.tools = json.dumps(t)

    def get_tools(self):
        return json.loads(self.tools)

    def save(self, *args, **kwargs):
        read_tools_file = self.tools_file.read().decode('utf-8')
        tools = read_tools_file.rstrip('\n') .split(',')
        self.set_tools(tools)
        self.tools_video = Video.objects.filter(video=self.tools_video_indicator)[0]
        super(Tools, self).save(*args, **kwargs) #Call the "real" save() method.

class PointAnnotation(models.Model):
    point_annotation_video = models.ForeignKey('Video', on_delete=models.CASCADE, null=True, blank=True) #TODO: discuss delete method
    point_annotation_tool = models.CharField(max_length=200, blank=True) #TODO: is this behavior correct? if toolset deleted, then just replace toolset with null?   
    point_annotation_timestamp = models.FloatField(null=True)
    point_annotation_video_indicator = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.point_annotation_tool

    def save(self, *args, **kwargs):
        self.point_annotation_video = Video.objects.filter(video=self.point_annotation_video_indicator)[0]
        super(PointAnnotation, self).save(*args, **kwargs) #Call the "real" save() method.

class SegmentAnnotation(models.Model):
    segment_annotation_video = models.ForeignKey('Video', on_delete=models.CASCADE, null=True, blank=True) #TODO: discuss delete method
    segment_annotation_text = models.CharField(max_length=200, blank=True)
    segment_annotation_starttime = models.FloatField(null=True)
    segment_annotation_endtime = models.FloatField(null=True)
    segment_annotation_video_indicator = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.segment_annotation_text

    def save(self, *args, **kwargs):
        self.segment_annotation_video = Video.objects.filter(video=self.segment_annotation_video_indicator)[0]
        super(SegmentAnnotation, self).save(*args, **kwargs) #Call the "real" save() method.


