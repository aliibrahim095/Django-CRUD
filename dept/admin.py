from django.contrib import admin
from .models import *
# Register your models here.


class StudentFormat(admin.ModelAdmin):
    fieldsets = (["Students Details", {'fields': ["fname", "lname", "age"]}], [
                 "Track Details", {'fields': ["std_track"]}])
    list_display = ['fname', 'lname', 'age', 'is_graduated', 'std_track']
    list_filter = ['std_track']
    search_fields = ['fname', 'std_track__name'] 


class StackedInlineStudent(admin.StackedInline):
    model = Student
    extra = 3


class TrackFormat(admin.ModelAdmin):
    inlines = [StackedInlineStudent]
    list_display = ['name']


admin.site.register(Track, TrackFormat)
admin.site.register(Student, StudentFormat)
