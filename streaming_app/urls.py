from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('<str:course_code>/', views.course_lecture, name='course'),
    path('<str:course_code>/video/', views.video_view, name='video'),
    path('account/', views.account_view, name='account'),
    path('<str:name>/', views.club_view, name='club'),
]