import os

from django.views.generic import ListView
from django.conf import settings
from django.shortcuts import render
from .models import Video


# Create your views here.
def indexview(request):
    return render(request, 'index.html')


def course_lecture(request):
    return render(request, 'course_lecture.html')


def accountview(request):
    return render(request, 'account.html')


class VideoListView(ListView):
    model = Video
    template_name = 'templates/streaming_app/video_list.html'
    context_object_name = 'videos'
