import os

from django.views.generic import ListView
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import Video, Course


# Create your views here.
def indexview(request):
    courses = Course.objects.all()
    context = {"courses": courses}
    return render(request, 'index.html', context)


def course_lecture(request, course_code):
    course = get_object_or_404(Course, course_code=course_code)
    return render(request, 'course_lecture.html', {"course": course})


def accountview(request):
    return render(request, 'account.html')


class VideoListView(ListView):
    model = Video
    template_name = 'templates/streaming_app/video_list.html'
    context_object_name = 'videos'
