from django.contrib import admin
from .models import Course, Video, Club


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


class VideoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["title", "description"]}),
        ("Video Information", {"fields": ["video_id"]}),
    ]

    list_display = ["title", "video_id"]


# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Video, VideoAdmin)
