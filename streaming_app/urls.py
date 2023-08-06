from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.index_view, name='index'),
    path('account/', views.account_view, name='account'),
    path('<str:course_code>/', views.course_lecture, name='course'),
    path('<str:course_code>/video/', views.video_view, name='video'),
    path('<str:course_code>/video/quiz/', views.quiz, name='video_quiz'),
    path('<str:name>/', views.club_view, name='club'),
]