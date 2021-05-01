from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.urls import reverse
from datetime import datetime
from .models import Annotation, Tools, Video
from .forms import AnnotationForm, VideoForm


GLOBAL_TIMESTAMP = 0 #I am so sorry to every programming teacher I've ever had

def index(request):
    annotation_model_form = AnnotationForm()
    video_model_form = VideoForm()
    annotation_list = Annotation.objects.all()
    video_list = Video.objects.all()
    most_recent_video = Video.objects.last()
    context = {
        'annotation_list': annotation_list,
        'annotation_model_form': annotation_model_form,
        'video_model_form': video_model_form,
        'video_list': video_list,
        'most_recent_video': most_recent_video,
        'timestamp': GLOBAL_TIMESTAMP
    }
    return render(request, 'annotation/index.html', context)

def add_annotation(request):
    if request.method == 'POST':
        aForm = AnnotationForm(request.POST)  
        if aForm.is_valid():
            global GLOBAL_TIMESTAMP
            GLOBAL_TIMESTAMP = aForm.cleaned_data['annotation_timestamp']
            aForm.save()
            return redirect('annotation:index')
        else:
            annotation_errors = aForm.errors
            annotation_model_form = AnnotationForm()
            context = {'annotation_errors': annotation_errors, 'annotation_model_form': annotation_model_form}
            return render(request, 'annotation/index.html', context)

def add_video(request):
    if request.method == 'POST':
        vForm = VideoForm(request.POST, request.FILES)
        if vForm.is_valid():
            vForm.save()
            return redirect('annotation:index')
            #context = {'video': Video.objects.last()}
            #return render(request, 'annotation/index.html', context)
        else:
            video_errors = vForm.errors
            video_model_form = VideoForm()
            context = {'video_errors': video_errors, 'video_model_form': video_model_form}
            return render(request, 'annotation/index.html', context)