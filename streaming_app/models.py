# Author: Brandon Grunes

from datetime import timezone, datetime
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


class Question(models.Model):
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    is_correct_answer = models.TextField()

    def __str__(self):
        return self.choice_text
