from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'annotation'
urlpatterns = [
    path('', views.index, name='index'),
    path('error', views.error, name='error'),
    path('add_point_annotation', views.add_point_annotation, name='add_point_annotation'),
    path('add_segment_annotation', views.add_segment_annotation, name='add_segment_annotation'),
    path('add_video', views.add_video, name='add_video'),
    path('add_tools', views.add_tools, name='add_tools'),
    path('output_csv', views.output_csv, name='output_csv'),
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
