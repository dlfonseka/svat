from django import forms
from .models import Video, Tools, Annotation
from django.core.exceptions import ValidationError
from django.conf import settings
import os

class AnnotationForm(forms.ModelForm):
    class Meta:
        model = Annotation
        exclude = []

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        exclude = []

    def clean_video(self):
        vid = self.cleaned_data['video']
        limit = 5 * 1024 * 1024 * 1024

        if vid.size > limit:
            raise ValidationError('File too large. Size should not exceed 5 Gb.')
        if vid.name in os.listdir(settings.MEDIA_ROOT):
            raise ValidationError('Video already uploaded.')
        return vid

class ToolsForm(forms.ModelForm):
    class Meta:
        model = Tools
        exclude = []