from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.urls import reverse
from datetime import datetime
from .models import Annotation, Tools, Video
from .forms import AnnotationForm, VideoForm


#def index(request):

# class IndexView(generic.ListView):
    
#     template_name = 'annotation/index.html'
#     context_object_name = 'annotation_list'

#     def get_queryset(self):
#         return Annotation.objects.order_by('-annotation_start_time')

def index(request):
    annotation_model_form = AnnotationForm()
    video_model_form = VideoForm()
    annotation_list = Annotation.objects.all()
    video_list = Video.objects.all()
    context = {
        'annotation_list': annotation_list,
        'annotation_model_form': annotation_model_form,
        'video_model_form': video_model_form,
        'video_list': video_list
    }
    return render(request, 'annotation/index.html', context)

def add_annotation(request):
    if request.method == 'POST':
        aForm = AnnotationForm(request.POST)  
        if aForm.is_valid():
            aForm.save()
            return redirect('annotation:index')
        else:
            annotation_error = aForm.errors
            annotation_model_form = AnnotationForm()
            context = {'annotation_errors': annotation_errors, 'annotation_model_form': annotation_model_form}
            return render(request, 'annotation/index.html', context)

def add_video(request):
    if request.method == 'POST':
        vForm = VideoForm(request.POST, request.FILES)
        print('Video FORM \n', vForm)
        if vForm.is_valid():
            vForm.save()
            return redirect('annotation:index')
        else:
            video_errors = vForm.errors
            video_model_form = VideoForm()
            context = {'video_errors': video_errors, 'video_model_form': video_model_form}
            return render(request, 'annotation/index.html', context)


    # if not Video.objects.order_by('video_upload_timestamp'):
    #     return HttpResponseBadRequest('No video uploaded to annotate.')
    # print('vid', Video.objects.order_by('video_upload_timestamp')[0])
    # instance = Annotation()

    # #instance.annotation_video = Video.objects.order_by('video_upload_timestamp')[0] #TODO: is it ok to assume we can just use the most recently upladed video? i suppose so if we only ever store one video
    # #instance.annotation_tools = models.ForeignKey(Tools, on_delete='SET_NULL') #FIXME: how tf do we do this? 
    # instance.annotation_text = request.POST['annotation_text']
    # instance.annotation_detail = request.POST['annotation_detail']
    # instance.annotation_start_time = request.POST['annotation_start_time']
    # #instance.annotation_duration = request.POST['annotation_duration']
    # instance.save()

    # return HttpResponseRedirect(reverse('annotation:index')) #TODO: make sure this redirect doesn't interfere with video reload


#def submit(request, annotation_id):
#    annotation = get_object_or_404(Question, pk=annotation_id)


# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'

#     def get_queryset(self):
#         return Question.objects.order_by('-pub_date')[:5]

# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'

# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {'question':  question, 'error_message':'You didn\'t select a choice'})
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#     return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     return render(request, 'polls/index.html', context)
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question':question})
