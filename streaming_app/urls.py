from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexview, name='index'),
    path('courses', views.indexview, name='courses'),
    path('courses/<str:course_code>', views.course_lecture, name='course'),
    path('account/', views.accountview, name='account'),
    path('login/', views.loginview, name="login")
]