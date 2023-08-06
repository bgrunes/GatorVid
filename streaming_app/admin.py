from django.contrib import admin
from .models import Course, Club, Question, Choice


# Custom admin layout for adding new courses
class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Basic Information", {"fields": ["name", "course_code", "description"]}),
        ("Date information", {"fields": ["start_date", "end_date"]}),
    ]

    list_display = ["name", "course_code", "start_date", "end_date"]


class ClubAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name", "purpose"]}),
        ("Announcements and Events", {"fields": ["announcements", "events"]}),
        ("Contact Info", {"fields": ["email"]}),
    ]

    list_display = ["name", "events"]


# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Question)
admin.site.register(Choice)
