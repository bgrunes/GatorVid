from django.urls import path
from . import views

app_name = "GatorVid Streaming"
urlpatterns = [
	path("", views.indexview, name="index"),
	path("/videos/", views.VideoListView.as_view(), name="videos")
]