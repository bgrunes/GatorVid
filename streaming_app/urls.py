from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexview, name='index'),
    path('course/<str:course_code>/', views.course_lecture, name='course'),
    path('account/', views.accountview, name='account'),
]