from django.contrib import admin
from .models import Course, Video, Club


# Custom admin layout for adding new courses
class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Basic Information", {"fields": ["name", "course_code", "description"]}),
        ("Date information", {"fields": ["start_date", "end_date"]}),
    ]

    list_display = ["name", "course_code", "start_date", "end_date"]


# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Club)
admin.site.register(Video)
