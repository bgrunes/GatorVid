import os

from django.views.generic import ListView
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import Video, Course, Club
from googleapiclient.discovery import build


# Create your views here.
def index_view(request):
    courses = Course.objects.all()
    context = {"courses": courses}
    return render(request, 'index.html', context)


def course_lecture(request, course_code):
    course = get_object_or_404(Course, course_code=course_code)
    return render(request, 'course_lecture.html', {"course": course})


def club_view(request, name):
    club = get_object_or_404(Club, name=name)
    return render(request, 'club.html', {"club": club})


def account_view(request):
    return render(request, 'account.html')


def video_view(request, course_code):
    course = get_object_or_404(Course, course_code=course_code)
    api_key = 'AIzaSyA9Iic_AumZRw-apwb7aq6090hMfMeqHAQ'
    video_id = 'HLCq5M_7DR4'

    youtube = build('youtube', 'v3', developerKey=api_key)
    page_token = None
    comments = []

    response = youtube.videos().list(
        part='snippet',
        id=video_id,
    ).execute

    if response['items']:
        video_info = response['items'][0]['snippet']
        title = video_info['title']
        description = video_info['description']
    else:
        title = None
        description = None

    response1 = youtube.commentThreads().list(
        part='snippet',
        videoId='HLCq5M_7DR4',
        textFormat='plainText',
        maxResults=10,  # Can adjust the value of comments
        pageToken=page_token,
    ).execute()

    for item in response1['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        username = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
        comments.append((username, comment))

    next_page_token = response1.get('nextPageToken')

    context = {
        'title': title,
        'description': description,
        'comments': comments,
        'next_page_token': next_page_token,
        'video_id': video_id,
        'course': course
    }

    return render(request, 'video.html', context)
