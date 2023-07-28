import os

from django.views.generic import ListView
from django.conf import settings
from django.shortcuts import render
from .models import Video


# Create your views here.
def indexview(request):
    return render(request, 'index.html')


class VideoListView(ListView):
    model = Video
    template_name = 'video_list.html'
    context_object_name = 'videos'
