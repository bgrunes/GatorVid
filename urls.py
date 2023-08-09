# Author: Brandon Grunes

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.index_view, name='index'),
    path('account/', views.account_view, name='account'),
    path('club/', views.club_view, name='club'),
    path('bard/', views.bard_view, name='bard'),
    path('<str:course_code>/', views.course_lecture, name='course'),
    path('<str:course_code>/video/', views.video_view, name='video'),
    path('<str:course_code>/video/quiz/', views.quiz, name='video_quiz'),
]