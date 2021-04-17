from django import forms
from .models import Video, Tools, Annotation

class AnnotationForm(forms.ModelForm):
    class Meta:
        model = Annotation
        exclude = []

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        exclude = []