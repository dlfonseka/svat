from django import forms
from .models import Video, Tools, PointAnnotation, SegmentAnnotation
from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils.text import get_valid_filename
import os

class PointAnnotationForm(forms.ModelForm):
    class Meta:
        model = PointAnnotation
        exclude = ['point_annotation_video']

class SegmentAnnotationForm(forms.ModelForm):
    class Meta:
        model = SegmentAnnotation
        exclude = ['segment_annotation_video']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        exclude = []

    def clean_video(self):
        vid = self.cleaned_data['video']
        limit = 5 * 1024 * 1024 * 1024
        vid.name = get_valid_filename(vid.name)
        if vid.size > limit:
            raise ValidationError('File too large. Size should not exceed 5 Gb.')
        if vid.name in os.listdir(settings.MEDIA_ROOT):
            raise ValidationError('Video already uploaded.')
        return vid

class ToolsForm(forms.ModelForm):
    class Meta:
        model = Tools
        exclude = []

    def clean_tools_file(self):
        tf = self.cleaned_data['tools_file']
        tf.name = get_valid_filename(tf.name)
        return tf