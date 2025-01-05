from django.contrib import admin
from .models import Subject, ClassRoom, TeacherProfile

# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'credit_hours')
    search_fields = ('code', 'name')

@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade_level', 'capacity')
    list_filter = ('grade_level',)
    search_fields = ('name',)

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name', 'email')
    filter_horizontal = ('subjects',)
