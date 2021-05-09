from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.urls import reverse
from datetime import datetime
from .models import Tools, Video, PointAnnotation, SegmentAnnotation
from .forms import PointAnnotationForm, SegmentAnnotationForm, VideoForm, ToolsForm
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required
import csv
import os

@login_required
def index(request):   
    point_annotation_model_form = PointAnnotationForm()
    segment_annotation_model_form = SegmentAnnotationForm()     
    video_model_form = VideoForm()
    video_list = Video.objects.all()
    tools_model_form = ToolsForm()
    try:
        available_video = Video.objects.get(video=[f for f in os.listdir(settings.MEDIA_ROOT) if f != 'tools'][0])
        annotation_list = list(PointAnnotation.objects.filter(point_annotation_video=available_video)) + \
                            list(SegmentAnnotation.objects.filter(segment_annotation_video=available_video)) #TODO: change this concatenation to merge
        annotation_list.sort(key=lambda t: t.point_annotation_timestamp if 'point_annotation_timestamp' in str(t._meta.get_fields()) else t.segment_annotation_starttime)
    except (Video.DoesNotExist, IndexError, Video.MultipleObjectsReturned) as e:
        available_video = None
    try:
        tools = [t.get_tools() for t in Tools.objects.filter(tools_video=available_video)][-1]
    except:
        tools = None
    try:
        if not Video.objects.all().exists():
            for f in [f for f in os.listdir(settings.MEDIA_ROOT) if f != 'tools']:
                os.remove(os.path.join(settings.MEDIA_ROOT, f))
    except:
        pass

    if available_video:
        context = {
            'annotation_list': annotation_list,
            'point_annotation_model_form': point_annotation_model_form,
            'segment_annotation_model_form': segment_annotation_model_form,
            'video_model_form': video_model_form,
            'tools_model_form': tools_model_form,
            'video_list': video_list,
            'tools': tools,
            'available_video': available_video,
        }
    else:
        context = {
            'point_annotation_model_form': point_annotation_model_form,
            'segment_annotation_model_form': segment_annotation_model_form,
            'video_model_form': video_model_form,
            'tools_model_form': tools_model_form,
        }
    return render(request, 'annotation/index.html', context)

@login_required
def add_point_annotation(request):
    if request.method == 'POST':
        aForm = PointAnnotationForm(request.POST) 
        print(aForm)
        if aForm.is_valid():
            indicator = aForm.cleaned_data['point_annotation_video_indicator']
            Video.objects.filter(video=indicator)[0].set_timestamp(aForm.cleaned_data['point_annotation_timestamp'])
            aForm.save()
            return redirect('annotation:index')
        else:
            point_annotation_errors = aForm.errors
            point_annotation_model_form = PointAnnotationForm()
            context = {'point_annotation_errors': point_annotation_errors, 'point_annotation_model_form': point_annotation_model_form}
            return render(request, 'annotation/index.html', context)

@login_required
def add_segment_annotation(request):
    if request.method == 'POST':
        aForm = SegmentAnnotationForm(request.POST) 
        if aForm.is_valid():
            indicator = aForm.cleaned_data['segment_annotation_video_indicator']
            Video.objects.filter(video=indicator)[0].set_timestamp(aForm.cleaned_data['segment_annotation_endtime'])
            aForm.save()
            return redirect('annotation:index')
        else:
            segment_annotation_errors = aForm.errors
            segment_annotation_model_form = SegmentAnnotationForm()
            context = {'segment_annotation_errors': segment_annotation_errors, 'segment_annotation_model_form': segment_annotation_model_form}
            return render(request, 'annotation/index.html', context)

@login_required
def add_video(request):
    if request.method == 'POST':
        vForm = VideoForm(request.POST, request.FILES)
        if vForm.is_valid():
            #NOTE: review this delete process
            for f in [f for f in os.listdir(settings.MEDIA_ROOT) if f != 'tools']:
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

@login_required
def add_tools(request):
    if request.method == 'POST':
        tForm = ToolsForm(request.POST, request.FILES)
        if tForm.is_valid():
            toolspath = os.path.join(settings.MEDIA_ROOT, 'tools')
            for f in os.listdir(toolspath):
                os.remove(os.path.join(toolspath, f))
            tForm.save()
            return redirect('annotation:index')
        else:
            tools_errors = tForm.errors
            tools_model_form = ToolsForm()
            context = {'tools_errors': tools_errors, 'tools_model_form': tools_model_form}
            return render(request, 'annotation/error.html', context)

@login_required
def output_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response


@login_required
def error(request):
    context = {}
    return render(request, 'annotation/error.html')