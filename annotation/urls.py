from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'annotation'
urlpatterns = [
    path('', views.index, name='index'),
    path('error', views.error, name='error'),
    path('add_annotation', views.add_annotation, name='add_annotation'),
    path('add_video', views.add_video, name='add_video'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
