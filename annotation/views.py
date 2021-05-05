from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.urls import reverse
from datetime import datetime
from .models import Annotation, Tools, Video
from .forms import AnnotationForm, VideoForm, ToolsForm
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os

def index(request):   
    annotation_model_form = AnnotationForm()
    video_model_form = VideoForm()
    video_list = Video.objects.all()
    try:
        available_video = Video.objects.get(video=os.listdir(settings.MEDIA_ROOT)[0])
        annotation_list = Annotation.objects.filter(annotation_video=available_video)
    except (Video.DoesNotExist, IndexError, Video.MultipleObjectsReturned) as e:
        available_video = None

    if available_video:
        context = {
            'annotation_list': annotation_list,
            'annotation_model_form': annotation_model_form,
            'video_model_form': video_model_form,
            'video_list': video_list,
            'available_video': available_video,
        }
    else:
        context = {
            'annotation_model_form': annotation_model_form,
            'video_model_form': video_model_form,
        }
    return render(request, 'annotation/index.html', context)

def add_annotation(request):
    if request.method == 'POST':
        aForm = AnnotationForm(request.POST) 
        if aForm.is_valid():
            aForm.cleaned_data['annotation_video'].video_timestamp = aForm.cleaned_data['annotation_timestamp']
            aForm.cleaned_data['annotation_video'].save()
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
            #NOTE: review this delete process
            for f in os.listdir(settings.MEDIA_ROOT):
                os.remove(os.path.join(settings.MEDIA_ROOT, f))
            if vForm.cleaned_data['video'].name in [ff.video.name for ff in Video.objects.all()]:
                path = default_storage.save(os.path.join(settings.MEDIA_ROOT, vForm.cleaned_data['video'].name), 
                                            ContentFile(vForm.cleaned_data['video'].read()))
                return redirect('annotation:index')
            vForm.save()
            return redirect('annotation:index')
        else:
            video_errors = vForm.errors
            video_model_form = VideoForm()
            context = {'video_errors': video_errors, 'video_model_form': video_model_form}
            return render(request, 'annotation/error.html', context)

def add_tools(request):
    if request.method == 'POST':
        tForm = ToolsForm(request.POST, request.FILES)
        if tForm.is_valid():
            tForm.save()
            return redirect('annotation:index')
        else:
            tools_errors = tForm.errors
            tools_model_form = ToolsForm()
            context = {'tools_errors': tools_errors, 'tools_model_form': tools_model_form}
            return render(request, 'annotation/error.html', context)

def error(request):
    context = {}
    return render(request, 'annotation/error.html')