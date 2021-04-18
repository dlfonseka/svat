from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
import datetime


class Video(models.Model):
    video = models.FileField() #validators=[FileExtensionValidator(allowed_extensions=['mp4, mov'])]#TODO: fix this filepath, TODO: add more allowed file extensions
    video_upload_timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.video.name

class Tools(models.Model):
    tools = models.JSONField() #TODO: is this right

class Annotation(models.Model):
      #annotation_video = models.ForeignKey(Video, on_delete=models.CASCADE, blank=True) #DISCUSS: delete annotation if video object deleted from database
      #annotation_tools = models.ForeignKey(Tools, on_delete=models.PROTECT, blank=True) #DISCUSS: is this behavior correct? if toolset deleted, then just replace toolset with null?   
      annotation_text = models.CharField(max_length=200, blank=True)
      annotation_detail = models.CharField(max_length=400, blank=True)
      annotation_start_time = models.DateTimeField(blank=True) #make mandatory
      #annotation_duration = models.DurationField(blank=True) #make optional

      def __str__(self):
          return self.annotation_text

