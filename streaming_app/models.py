from django.db import models
from googleapiclient.discovery import build


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=120)
    course_code = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    # Need to add Video Files when API is introduced

    def __str__(self):
        return self.name


# Clubs and Organizations Object
class Club(models.Model):
    name = models.CharField(max_length=100)
    purpose = models.TextField()
    email = models.EmailField()
    announcements = models.TextField()
    events = models.TextField()

    # Need to add Video Files when API is introduced

    def __str__(self):
        return self.name


class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=100)
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
