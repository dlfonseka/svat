from django.core.exceptions import ValidationError
from .models import Video

def file_size(file):
    #gets Django File object
    limit = 5 * 1024 * 1024 * 1024
    if file.size > limit:
        raise ValidationError('File too large. Size should not exceed 5 Gb.')

def video_exists(file):
    #gets Django File object
    if file.name in Video.objects.all():
        raise ValidationError('Video exists in database. Select video from dropdown or change filename and reupload.')

    
